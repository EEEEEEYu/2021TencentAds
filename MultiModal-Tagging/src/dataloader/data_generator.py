import os
import sys
import random
import numpy as np
import yaml
import linecache
import importlib
from tomorrow3 import threads

class Data_Generator:
    
    def __init__(self,
                 data_config):
        self.data_config = data_config
        self.shuffle = self.data_config['shuffle']
        self.feature_config = self.data_config['preprocess_config']['feature']
        self.feature_num_per_sample = len(self.feature_config)  # video, audio, text, image，长度为4，即每个样本有四个特征
        self.label_config = self.data_config['preprocess_config']['label']
        self.label_num_per_sample = len(self.label_config)  # 1个属性
        self.index_to_input_name = {}
        self.label_num_dict = {}
        input_index = -1
        self.dname_string_list = []  # str2list
        self.dtype_string_list = []
        self.data_shape_list = []
        for tmp_config in [self.feature_config, self.label_config]:  # 依次遍历特征配置文件和标签配置文件
            for data_part in tmp_config:  # temp_config:[{}]
                name = data_part['name']  # 'video,video_frames_num,idx'
                shape = data_part['shape']  # [[300,1024], [],[]]
                input_index += 1
                self.index_to_input_name[input_index] = name  # 将输入索引映射到name
                dtype_str = data_part['dtype']  # 'float32,int32,string'
                output_name_spt = name.split(',')  # ['video', 'video_frame', 'idx']
                output_dtype_spt = dtype_str.split(',')  # ['float32', 'int32', string]
                self.dname_string_list += output_name_spt
                self.dtype_string_list += output_dtype_spt
                self.data_shape_list +=shape
        # self.dname_string_list:['video', 'video_frame', 'idx', 'audio', 'audio_frames_num', 'image', 'text']
        # self.dtype_string_list:[float32, int32, string, float32, int32, float32, int64]
        # self.data_shape_list:[[300,1024], [],[],[300,128],[],[224,224,3],[128]]

        # +1 blank line for seperate    4 + 1 + 1
        self.data_num_per_sample = self.feature_num_per_sample + self.label_num_per_sample + 1
        print('self.data_num_per_sample:{}'.format(self.data_num_per_sample), )

        print('\n开始调入训练集数据\n')
        self.train_data_source_list = self.data_config['train_data_source_list']  # as a {{}}
        for source_name in self.train_data_source_list:  # source_name = train799 as a {}  遍历键值
            fn = self.train_data_source_list[source_name]['file']  # preprocessing脚本生成文件  actually is a 文件路径
            sample_count = self.fn_sample_count(fn)  # 计算训练样本数量  4500
            print('Train Source sample_count: ',source_name,sample_count)
            self.train_data_source_list[source_name]['sample_count'] = sample_count  # 样本数量赋值
            batch_size = self.train_data_source_list[source_name]['batch_size']  # 从配置文件中去除batch_size  32
            batch_num = max(1, sample_count // batch_size)  # 计算训练batch数量  140  notice:batch_size=32  //向下取整
            print('Train Source batch_num: ',source_name,batch_num)
            self.train_data_source_list[source_name]['batch_num'] = batch_num  # batch数量赋值

        print('\n开始调入验证集数据\n')
        self.valid_data_source_list = self.data_config['valid_data_source_list']
        for source_name in self.valid_data_source_list:
            fn = self.valid_data_source_list[source_name]['file']
            sample_count = self.fn_sample_count(fn)  # 计算验证样本数量  500
            print('Valid Source: ', source_name,sample_count)
            self.valid_data_source_list[source_name]['sample_count'] = sample_count
            batch_size = self.valid_data_source_list[source_name]['batch_size']
            batch_num = max(1, sample_count // batch_size)
            print('Valid Source batch_num: ',source_name,batch_num)
            self.valid_data_source_list[source_name]['batch_num'] = batch_num


        print('\n数据调入完毕，开始执行预处理\n')
        self.train_preprocess = self.get_preprocess_function(is_training=True)  # tuple
        self.valid_preprocess = self.get_preprocess_function(is_training=False)

    def fn_sample_count(self, fn):
        line_count = 0
        for l in open(fn):  # 打开train.txt文件按行读取，正常情况下每个样本对应5行
            line_count += 1
        assert line_count % self.data_num_per_sample == 0, "line_count: {} , data_num_per_sample: {}".format(line_count, self.data_num_per_sample)  # 如果不能整除样本数(error occurs)，执行该语句
        sample_count = line_count / self.data_num_per_sample  # 计算样本数量
        sample_count = int(sample_count)
        return sample_count  # 返回样本数量

    def get_single_sample_gen(self, data_source, preprocess_function, clip_batch=True):
        filename = data_source['file']
        count = data_source['sample_count']
        batch_size = data_source['batch_size']
        if clip_batch:
           count = count - (count%batch_size)
        while True:
            index_lst = list(range(0, count))
            if self.shuffle:
               random.shuffle(index_lst)
            result_list_queue = []
            for i in index_lst:
                return_list = []
                for line_i in range(self.data_num_per_sample*i+1,
                               self.data_num_per_sample*(i+1)):
                    line = linecache.getline(filename, line_i)
                    line = line.strip('\r\n')
                    return_list.append(line)
                result_list = preprocess_function(*return_list)
                result_list_queue.append(result_list)

                if len(result_list_queue) == 50:
                   for result_list in result_list_queue:
                       yield result_list.result()
                   result_list_queue = []
            
            for result_list in result_list_queue:
               yield result_list.result()
            result_list_queue = []
            
    def get_batch_generator(self, generator,batch_num, batch_size, return_dict=True):
        batch_sample_list = []
        for _ in range(batch_num*batch_size):
            sample = generator.__next__()
            batch_sample_list.append(sample)
            if len(batch_sample_list) == batch_size:
               batch_sample = []
               data_size = len(batch_sample_list[0])
               for data_i in range(data_size):
                   data_i_batch = []
                   for batch_i in range(batch_size):
                       data_i_batch.append(batch_sample_list[batch_i][data_i])
                   data_i_batch = np.array(data_i_batch)
                   batch_sample.append(data_i_batch)
               if return_dict:
                  batch_sample = {name:data for name,data in zip(self.dname_string_list,batch_sample)}
               yield batch_sample
               batch_sample_list = []

    def get_train_sample_generator(self):
        self.train_source_generator = {}
        for source_name in self.train_data_source_list:
            self.train_source_generator[source_name] = self.get_single_sample_gen(self.train_data_source_list[source_name],
                                                                                  self.train_preprocess)

        while True:
            for source_name in self.train_data_source_list:
                source_batch_size = self.train_data_source_list[source_name]['batch_size']
                for _ in range(source_batch_size):
                    return_list = self.train_source_generator[source_name].__next__()
                    yield return_list

    def get_valid_sample_generator_dict(self):
        self.valid_source_generator_dict = {}
        for source_name in self.valid_data_source_list:
            generator = self.get_single_sample_gen(self.valid_data_source_list[source_name],
                                                   self.valid_preprocess)
            source_batch_num = self.valid_data_source_list[source_name]['batch_num']
            source_batch_size = self.valid_data_source_list[source_name]['batch_size']
            self.valid_source_generator_dict[source_name] = self.get_batch_generator(generator=generator,
                                                                           batch_num=source_batch_num,
                                                                           batch_size=source_batch_size)
        return self.valid_source_generator_dict

    def get_preprocess_function(self,is_training):  # 预处理函数
        root = self.data_config['preprocess_root']  # 加载预处理根目录src/dataloader/preprocess/
        sys.path.append(root)  # 将预处理根目录添加到系统路径
        index_to_preprocess = []  # 预处理对应索引

        print('\n导入训练部分预处理模块\n')
        for data_part in self.feature_config:  # ['video', 'audio', 'text', 'image']
            package_name, preprocess_class_name = data_part['class'].split('.')  # 'frames_npy_preprocess.Preprocess'->'frames_npy_preprocess', 'Preprocess'
            if 'extra_args' in data_part:  # 检测是否有额外参数
                init_args = data_part['extra_args']  # 这在168行处生效，导入Preprocess类需要确定额外参数
            else:
                init_args = {}  # 没有的话初始化一个字典
            init_args['is_training'] = is_training  # 训练部分为True, 验证部分为False
            preprocess_module = importlib.import_module(package_name)  # 动态导入预处理模块，因为要视遍历到的样本特征来确定
            Preprocess_Class = getattr(preprocess_module, preprocess_class_name)  # Preprocess_Class = Class(Preprocess)
            preprocess_instance = Preprocess_Class(**init_args)  # 对Preprocess_Class类初始化得到类preprocess_instance
            index_to_preprocess.append(preprocess_instance)  # 将该类添加到列表index_to_preprocess中
        # index_to_preprocess: [Class(Preprocess) in frames_npy_preprocess, Class(Preprocess) in frames_npy_preprocess, ..in text_preprocess, ..in image_preprocess]

        print('\n导入验证部分预处理模块\n')
        for data_part in self.label_config:  # [{}]
            package_name, preprocess_class_name = data_part['class'].split('.')  # 'label_preprocess.Preprocess_label_sparse_to_dense' --> 'label_preprocess', 'Preprocess_label_sparse_to_dense'
            if 'extra_args' in data_part:
                init_args = data_part['extra_args']
            else:
                init_args = {}
            preprocess_module = importlib.import_module(package_name)
            Preprocess_Class = getattr(preprocess_module, preprocess_class_name)
            preprocess_instance = Preprocess_Class(**init_args)
            name = data_part['name']
            self.label_num_dict[name] = preprocess_instance.label_num
            index_to_preprocess.append(preprocess_instance)
        self.index_to_preprocess = index_to_preprocess
        # self.index_to_preprocess = [Class(Preprocess) in frames_npy_preprocess, Class(Preprocess) in frames_npy_preprocess, ..in text_preprocess, ..in image_preprocess, Preprocess_label_sparse_to_dense in label_preprocess]
        
        print('\n将预处理模块整合成元组\n')
        @threads(20)  # threads 并行计算
        def preprocess_fn(*args):  # 将参数处理成元组
            preprocess_data_list = []  # 初始化一个预处理数据列表
            for index, data in enumerate(args):
                preprocess_data = self.index_to_preprocess[index](data)  # self.index_to_preprocess是类，相当于类声明，data本身作为参数-->将这些data转换为对应的类
                if isinstance(preprocess_data,np.ndarray):  # 判断对象类型与参数二是否一致
                   preprocess_data_list.append(preprocess_data)
                elif isinstance(preprocess_data, tuple):
                   for preprocess_data_element in preprocess_data:
                       preprocess_data_list.append(preprocess_data_element)
            return tuple(preprocess_data_list)  # 返回为data组成的元组

        return preprocess_fn


if __name__ == '__main__':
   import argparse
   import time
   #import cProfile

   parser = argparse.ArgumentParser()
   parser.add_argument('--data_config',type=str)
   args = parser.parse_args()

   data_config = yaml.load(open(args.data_config))
   data_generator =  Data_Generator(data_config = data_config['DatasetConfig'])
   train_sample_generator =  data_generator.get_train_sample_generator()
   def train():
       time_list_sum = 0
       time_count = 0
       for _ in range(10):
           start_time = time.time()
           sample = train_sample_generator.__next__()
           end_time = time.time()
           time_list_sum += (end_time-start_time)
           time_count += 1
           print(time_count,np.mean(time_list_sum)/time_count)
           for x,output_name in zip(sample,data_generator.dname_string_list):
               print(x, output_name)

   def valid():
       valid_sample_generator_dict =  data_generator.get_valid_sample_generator_dict()
       for source_name,generator in valid_sample_generator_dict.items():
           for sample in generator:
               for output_name, x in sample.items():
                   print('valid', output_name,x)
   #cProfile.run('test()')
   #print(data_config)
   train()
   valid()
   train()
   valid()
