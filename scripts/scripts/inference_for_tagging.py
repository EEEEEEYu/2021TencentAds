#encoding: utf-8
import sys,os
sys.path.append(os.getcwd())
import glob
import tensorflow.compat.v1 as tf
import numpy as np
import cv2
import argparse
import time
import traceback
import json
import utils.tokenization as tokenization
from utils.train_util import get_label_name_dict
from src.feats_extract.multimodal_feature_extract import MultiModalFeatureExtract

#################Inference Utils#################
tokokenizer = tokenization.FullTokenizer(vocab_file='pretrained/bert/chinese_L-12_H-768_A-12/vocab.txt')
class TaggingModel():  # 输入参数是config字典
    def __init__(self, configs):
        tag_id_file = configs.get('tag_id_file', None)  # 返回指定键的值 equals to   tag_id_file = config['tag_id_file']
        model_pb = configs.get('model_pb', None)
        if tag_id_file is None:
            raise  # 手动异常  报错Error
        else:
            self.label_name_dict = get_label_name_dict(tag_id_file, None)  # 返回到一个字典  label_name_dict:{'label': int(id)}
        if model_pb is None:
            raise
        else:  # 产生一个sess变量和一个signature变量
            config = tf.ConfigProto(allow_soft_placement=True)  # 允许tensorflow自动分配设备
            config.gpu_options.allow_growth = True  # 用于动态申请显存，从少到多慢慢增加gpu容量
            self.sess = tf.Session(config=config)  # tf.Session 三个参数：target graph config
            meta_graph_def = tf.saved_model.loader.load(self.sess, [tf.saved_model.tag_constants.SERVING], model_pb)  # 加载一个保存的模型
            signature_def = meta_graph_def.signature_def  # A dictionary mapping signature names to functions.
            self.signature = signature_def[tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]  # key: tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY

        batch_size = configs.get('video_feats_extractor_batch_size', 8)  # 默认值是8 actually新创建Key: video_feats_extractor_batch_size  提取特征
        imgfeat_extractor = configs.get('imgfeat_extractor', 'Youtube8M')  # 默认是string: 'Youtube8M'  as  图像特征提取器
        self.feat_extractor = MultiModalFeatureExtract(batch_size=batch_size, imgfeat_extractor= imgfeat_extractor, 
                             extract_video = True, extract_audio = True, extract_text = False)  # 特征提取器 as a class

    def image_preprocess(self, image, rescale=224):
        #resize to 224 and normlize to 0-1, then perform f(x)= 2*(x-0.5)
        if isinstance(image, type(None)):
          print("WARNING: test input image is None")
          return np.zeros((rescale, rescale, 3))
        if image.shape[0] !=rescale:
          image = cv2.resize(image, (rescale, rescale))
        image = 2*(image/(np.max(image)+1e-10) - 0.5)
        return image

    def text_preprocess(self, txt,max_len=128):
        tokens = ['[CLS]'] + tokokenizer.tokenize(txt)
        ids = tokokenizer.convert_tokens_to_ids(tokens)
        ids = ids[:max_len]
        ids = ids + [0]*(max_len-len(ids))
        return ids


    def preprocess(self, feat_dict, max_frame_num=300):
        ret_dict = {}
        for feat_type in feat_dict:
            if feat_type=='video':
                feats = np.zeros((max_frame_num, len(feat_dict['video'][0])))
                valid_num = min(max_frame_num, len(feat_dict['video']))
                feats[:valid_num] = feat_dict['video']
            elif feat_type=='audio':
                feats = np.zeros((max_frame_num, len(feat_dict['audio'][0])))
                valid_num = min(max_frame_num, len(feat_dict['audio']))
                feats[:valid_num] = feat_dict['audio']
            elif feat_type=='text':
                feats = self.text_preprocess(feat_dict['text'], 128)
            elif feat_type == 'image':
                feats = self.image_preprocess(feat_dict['image'])
            else:
                raise
            ret_dict[feat_type] = feats
        return ret_dict

    def load_multimodal_feat(self, test_file, feat_dir):
        assert os.path.exists(feat_dir)
        feat_dict = {}
        # load video feat
        video_id = os.path.basename(test_file).split('.m')[0]
        feat_dict['video'] = np.load(os.path.join(feat_dir,'video_npy' ,'Youtube8M', 'tagging', video_id + '.npy'))
        feat_dict['audio'] = np.load(os.path.join(feat_dir, 'audio_npy', 'Vggish', 'tagging', video_id + '.npy'))
        feat_dict['image'] = cv2.imread(os.path.join(feat_dir, 'image_jpg','tagging', video_id + '.jpg'), 1)
        feat_dict['text'] = open(os.path.join(feat_dir, 'text_txt', 'tagging', video_id + '.txt')).read()
        return feat_dict

    def inference(self, test_file, load_feat=False, feat_dir=None):
        tf.reset_default_graph()
        with self.sess.as_default() as sess:
            if load_feat == False:
                start_time = time.time()
                feat_dict = self.feat_extractor.extract_feat(test_file, save=False)
                end_time = time.time()
                print("feature extract cost time: {} sec".format(end_time -start_time))
            else:
                feat_dict = self.load_multimodal_feat(test_file, feat_dir)

            if 'text' in feat_dict:
#                print(feat_dict['text'])
                pass
            else:
                feat_dict['text'] = ""
            feat_dict_preprocess = self.preprocess(feat_dict)
            feed_dict ={}
            
            # Get input tensor.
            for key in feat_dict:
                if key in self.signature.inputs:
                  feed_dict[self.signature.inputs[key].name] = [feat_dict_preprocess[key]]
                
            if 'video_frames_num' in self.signature.inputs:
                feed_dict[self.signature.inputs['video_frames_num'].name] = [len(feat_dict['video'])]
            if 'audio_frames_num' in self.signature.inputs:
                feed_dict[self.signature.inputs['audio_frames_num'].name] = [len(feat_dict['audio'])]
                
            # Get output tensor.
            class_indexes = self.signature.outputs['class_indexes'].name
            predictions = self.signature.outputs['predictions'].name
            #video_embedding = self.signature.outputs['video_embedding'].name #(Optional)
            
            start_time = time.time()
            class_indexes,predictions = sess.run([class_indexes,predictions], feed_dict)  # 
            end_time = time.time()
            
            print("multi-modal tagging model forward cost time: {} sec".format(end_time -start_time))


            labels=[self.label_name_dict[index] for index in class_indexes[0]]
            scores = predictions[0]

        return labels, scores

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_pb', default='checkpoints/ds/export/step_10000_0.6879',type=str)  # 模型路径
    parser.add_argument('--tag_id_file', default='dataset/dict/tag-id-deconstruction_b0.txt')  # label_id.txt 标签对应到id
    parser.add_argument('--test_dir', default='../SceneSeg/data/ad300/video')  # 视频测试集
    parser.add_argument('--postfix', default='.mp4', type=str, help='test file type')  # 后缀是.mp4
    parser.add_argument('--load_feat', type=int, default=1) # 加载预训练的特征 编号为1
    parser.add_argument('--feat_dir', type=str, default=None) # 视频特征目录, 不同按照固定目录格式存放  /tagging/tagging_dataset_test_5k
    parser.add_argument('--top_k', type=int, default=20)  # 取得分最高的前20个特征
    parser.add_argument('--output', default="results/result_for_vis.txt", type=str) #用于可视化文件
#    parser.add_argument('--output_json', default="results/outjson.txt", type=str) #用于模型精度评估
    parser.add_argument('--output_json', default="results/output.json", type=str)
    args = parser.parse_args()
    
    configs={'tag_id_file': args.tag_id_file, 'model_pb': args.model_pb}  # 把模型和标签表整合到一个字典里
    model = TaggingModel(configs)  # 加载模型 as a class
    test_files = glob.glob(args.test_dir+'/*'+args.postfix)  # 返回所有匹配的文件路径列表 list
    test_files.sort()  # 排序
    output_result = {}  # 输出as dictionary  will be saved as a .json document
    
    #clean temp file
    if os.path.exists(args.output):  # 如果存在result_for_vis.txt，清楚，用于初始化
        os.remove(args.output)

    index = 1
    for test_file in test_files:  # 遍历测试集中每一个(视频)文件
        print(index)
        index += 1
        print(test_file)  # 路径+文件名 as string
        try:
          labels, scores = model.inference(test_file, args.load_feat, args.feat_dir)  # 输入文件路径 load_feat==1 feat_dir==tagging/tagging_dataset_test_5k  finally,一个视频得到标签和分数
        except:  # 异常代码块 if遇到异常
          print(traceback.format_exc())

        if args.output_json is not None:
            cur_output = {}
            output_result[test_file.split("/")[-1]] = cur_output
            cur_output["result"] = [{"labels": labels[:args.top_k], "scores": ["%.2f" % scores[i] for i in range(args.top_k)]}]
            print(cur_output)
#            print(output_result)

        if args.output is not None:
            with open(args.output, 'a+') as f:
                video_id = test_file.split('/')[-1].split('.')[0]
                scores = [scores[i] for i in range(args.top_k)]
                f.write("{}\t{}\n".format(video_id, "\t".join(["{}##{:.3f}".format(labels[i], scores[i]) for i in range(len(scores))])))
        print("-"*100)
    
    print("json begins")
    print(args.output_json)
    with open(args.output_json, 'w', encoding="utf-8") as f:
        json.dump(output_result, f, ensure_ascii=False, indent = 4)
    print("Done")