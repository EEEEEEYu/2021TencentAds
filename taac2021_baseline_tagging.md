# 腾讯广告算法大赛 2021: 多模态视频广告标签
* 赛道二: 多模态视频广告标签（Multimodal Video Ads Tagging）  
    * 赛题简介: 对于给定的测试视频样本，通过算法预测出视频在呈现形式、场景、风格等三个维度上的标签，使用Global Average Precision(GAP)进行评分。  
* 官网报名 - https://algo.qq.com/  

# 赛题解析

## 赛题说明

多模态视频广告标签是一种多模式学习任务，旨在通过理解包括视频、音频、文本等在内的多模态信息来预测语义标签。具体地，对于我们给定的视频广告，参赛者需要从4个维度来预测视频标签: 呈现、场景、样式、叙述。  
![avatar](tagging.png)
如上图所示，每个视频广告样本都包含视频和音频，还可以通过OCR和ASR提取出文本信息。基于这些特征作为输入，使用多模态标签学习来预测标签。  
* 补充说明: 允许参赛者使用外部训练数据优化模型，包括合成数据以及其它公共数据集。此外，参赛者也可以使用NLP纠错、知识图谱和其它策略进行优化。

## 评估指标

对于每个广告视频，您将提交一份预测标签及其对应的置信度得分的列表。  
评估采用具有最高k(i)的预测标签，其中i为索引，每个视频在每个索引下的置信度得分，然后将每个预测和置信度得分视为一长串的全局数据中的单个数据点预测，以计算上述各方面的所有预测和所有视频的平均精度。如果提交视频具有k(i)个预测（标记/置信对），并按其置信度得分排序，则GAP
$$
GAP = \sum_{i=1}^{3} \sum_{j=1}^{k(i)} p(j)\Delta r(j)
$$

## 提交格式

提交结果文件为json格式，示例如下:  

```json
{
    "03121d15e3cb0354c478576ec12c1f56.mp4": {
        "result": [{
                "labels": ["情景剧","BGM","办公室","人行道","悬念","中景","特写","现代","背景交代","疑问悬念","附加赠礼","游戏界面","红包","游戏原声","手机屏幕","轻快","产品展示","金币/红包激动","服务优势","品牌强化","行动指引"],
                "scores": [0.9, 0.8, 0.5, 0.5, ...]
                  }]
        }
    ...
}
```

# 数据说明

初赛阶段会提供初赛数据集，参赛者在报名成功后，可在腾讯云TI-ONE中启动一个Notebook，初赛数据集已经预置在了/home/tione/notebook/algo-2021/dataset/目录下。  
* 腾讯云TI-ONE如何启动一个Notebook - https://cloud.tencent.com/document/product/851/44434  
* /home/tione/notebook/algo-2021/dataset/目录是只读目录，为了提升性能或便于数据处理，用户可以在/home/tione/notebook/目录下新建文件夹dataset，并将/home/tione/notebook/algo-2021/dataset/下的内容复制到/home/tione/notebook/dataset/下

初赛数据集的目录结构如下:  
```
- dataset/
    - label_id.txt                                                  // 标签字典文件，每一行是(标签名称, 标签编号)
    - structuring/
        - GroundTruth/                                              // structuring任务的训练集标注信息和数据集文件
            - datafile/                                             // structuring任务的训练集数据集文件，包括训练集（datafile/train.txt, shuffle后的90%）与验证集（datafile/val.txt, shuffle后的10%）
                - train.txt
                - val.txt
            - structuring_tagging_info.txt                          // structuring任务训练集标注信息（csv格式）
            - train5k.txt                                           // structuring任务训练集标注信息（json格式）
        - structuring_dataset_test_5k/                              // structuring任务测试集特征信息
            - aud_feat/
            - aud_wav/
            - shot_keyf/
            - shot_split_video/
            - shot_stats/
            - shot_txt/
        - structuring_dataset_train_5k/                             // structuring任务训练集特征信息
            - aud_feat/
            - labels/
            - meta/
            - place_feat/
            - shot_stats/
            - shot_txt/ 
        - train5k_split_video/                                      // 切分后的视频
        - train5k_split_video_feats/                                // 切分后的视频特征，包括视频特征、音频特征、封面图、文本特征等
    - tagging/
        - GroundTruth/                                              // tagging任务的训练集标注信息和数据集文件
            - datafile/                                             // tagging任务的训练集数据集文件，包括训练集（datafile/train.txt，shuffle后的90%）与验证集（datafile/val.txt，shuffle后的10%），每一个样本包括6行，依次是video_npy、audio_npy、封面图、文本信息、多标签标注信息（文本）、空行
                - train.txt
                - val.txt
            - tagging_info.txt                                      // tagging任务的训练集标注信息（csv格式）
        - tagging_dataset_test_5k/                                  // 测试集的特征文件
            - audio_npy/Vggish/tagging/                             // 音频特征: 测试集视频的音频特征文件（.npy）
            - image_jpg/tagging/                                    // 封面图: 测试集视频的封面图文件
            - text_txt/tagging/                                     // 文本特征: 测试集视频的文本特征，包括视频广告的OCR结果、ASR结果等
            - video_npy/Youtube8M/tagging/                          // 视频特征: 测试集视频的视频特征文件（.npy）
        - tagging_dataset_train_5k/                                 // 训练集的特征文件
            - audio_npy/Vggish/tagging/                             // 音频特征: 训练集视频的音频特征文件（.npy）
            - image_jpg/tagging/                                    // 封面图: 训练集视频的封面图文件
            - text_txt/tagging/                                     // 文本特征: 训练集视频的文本特征，包括视频广告的OCR结果、ASR结果等
            - video_npy/Youtube8M/tagging/                          // 视频特征: 训练集视频的视频特征文件（.npy）
    - videos/
        - test_5k_A/                                                // 测试集原始视频文件（.mp4）
        - train_5k_A/                                               // 训练集原始视频文件（.mp4）
```

## （彩蛋）数据展示

借助TI-ONE Notebook，您可以方便地展示数据集中的数据，包括视频、图片等，以帮助进一步分析。  
以下代码片段，给出了一个简单的示例（相信你已经能感受到Notebook的强大了，尽情探索Notebook的数据展示与分析功能吧）: 


```python
import os

dataset_root = './VideoStructuring/dataset/'

# ########## get train_5k_A video file lists
videos_train_5k_A_dir = os.path.join(dataset_root, 'videos/train_5k_A')
videos_train_5k_A_files = [os.path.join(videos_train_5k_A_dir, f) for f in os.listdir(videos_train_5k_A_dir) if os.path.isfile(os.path.join(videos_train_5k_A_dir, f))]

print("videos_train_5k_A_dir= {}".format(videos_train_5k_A_dir))
print("len(videos/train_5k_A)= {}".format(len(videos_train_5k_A_files)))

# ########## display
from IPython.display import display, HTML

# video
test_video_path = videos_train_5k_A_files[3000]
print(test_video_path)
print(os.path.exists(test_video_path))
html_str = '''
<video controls width=\"500\" height=\"500\" src=\"{}\">animation</video>
'''.format(test_video_path)
print(html_str)
display(HTML(html_str))
```

# Baseline

为了让参赛者更快速地熟悉赛题，我们提供了一个baseline，帮助参赛者们理解赛题，并开拓思路。   

参赛者在报名成功后，可在腾讯云TI-ONE中启动一个Notebook，tagging任务的baseline已经预置在了/home/tione/notebook/algo-2021/baseline/tagging/VideoStructuring/目录下。  
* 腾讯云TI-ONE如何启动一个Notebook - https://cloud.tencent.com/document/product/851/44434
* /home/tione/notebook/algo-2021/baseline/tagging/VideoStructuring/目录是只读目录，为了提升性能或便于数据处理，用户可以在/home/tione/notebook/目录下新建文件夹VideoStructuring，并将/home/tione/notebook/algo-2021/baseline/tagging/VideoStructuring/下的内容复制到/home/tione/notebook/VideoStructuring/下

Baseline（/home/tione/notebook/VideoStructuring/）的目录结构如下:  
```
- VideoStructuring/
    - MultiModal-Tagging/                              // tagging任务相关的代码
        - configs/
        - dataset/
        - pretrained/
        - scripts/
        - src/
        - utils/
        - ReadMe.md
        - requirment.txt
    - SceneSeg/                                        // Scene Segmentation相关的代码
        - lgss/
        - pre/
        - run/
        - ReadMe.md
    - init.sh                                          // 初始化脚本，需要执行 ./init.sh run 初始化环境
    - run.sh                                           // 运行脚本，seg_train、tag_train、test等步骤都封装成了脚本，可通过 ./run.sh 脚本执行相关任务，使用 ./run.sh help 了解如何使用
    - ReadMe.md
```


```python
!cp -r -d /home/tione/notebook/algo-2021/baseline/tagging/* /home/tione/notebook/
```

本Notebook原始路径为/home/tione/notebook/algo-2021/baseline/tagging/taac2021_baseline_tagging.ipynb，不可写。  
完成上述复制后，/home/tione/notebook/目录下应该有文件夹VideoStructuring/、taac2021_baseline_tagging.ipynb、tagging.png等文件。  
可重新打开/home/tione/notebook/taac2021_baseline_tagging.ipynb，此文件可写。  

## 环境准备

Baseline代码运行所需要的环境可以直接运行 init.sh 进行准备  
注意: init.sh 中的 JupyterRoot 需要更改为 VideoStructuring 文件夹所在的目录  


```python
!cd ~/notebook/VideoStructuring && sudo chmod a+x ./init.sh && ./init.sh run
```

    CONDA_CONFIG_ROOT_PREFIX= root_prefix: /opt/conda
    CONDA_ROOT= /opt/conda
    TAAC2021_ENV= taac2021
    JUPYTER_ROOT= /home/tione/notebook
    Hit:1 http://mirrors.tencentyun.com/ubuntu bionic InRelease
    Hit:2 http://mirrors.tencentyun.com/ubuntu bionic-security InRelease
    Hit:3 http://mirrors.tencentyun.com/ubuntu bionic-updates InRelease
    Reading package lists... Done                     
    Reading package lists... Done
    Building dependency tree       
    Reading state information... Done
    apt-utils is already the newest version (1.6.12ubuntu0.2).
    0 upgraded, 0 newly installed, 0 to remove and 126 not upgraded.
    Reading package lists... Done
    Building dependency tree       
    Reading state information... Done
    libsndfile1-dev is already the newest version (1.0.28-4ubuntu0.18.04.1).
    ffmpeg is already the newest version (7:3.4.8-0ubuntu0.2).
    0 upgraded, 0 newly installed, 0 to remove and 126 not upgraded.
    Collecting package metadata (current_repodata.json): done
    Solving environment: done
    
    
    ==> WARNING: A newer version of conda exists. <==
      current version: 4.7.12
      latest version: 4.9.2
    
    Please update conda by running
    
        $ conda update -n base conda
    
    
    
    ## Package Plan ##
    
      environment location: /opt/conda/envs/taac2021
    
      added / updated specs:
        - ipykernel
        - python=3.7
    
    
    The following NEW packages will be INSTALLED:
    
      _libgcc_mutex      conda-forge/linux-64::_libgcc_mutex-0.1-conda_forge
      _openmp_mutex      conda-forge/linux-64::_openmp_mutex-4.5-1_gnu
      backcall           conda-forge/noarch::backcall-0.2.0-pyh9f0ad1d_0
      backports          conda-forge/noarch::backports-1.0-py_2
      backports.functoo~ conda-forge/noarch::backports.functools_lru_cache-1.6.1-py_0
      ca-certificates    conda-forge/linux-64::ca-certificates-2020.12.5-ha878542_0
      certifi            conda-forge/linux-64::certifi-2020.12.5-py37h89c1867_1
      decorator          conda-forge/noarch::decorator-4.4.2-py_0
      ipykernel          conda-forge/linux-64::ipykernel-5.5.0-py37h888b3d9_1
      ipython            conda-forge/linux-64::ipython-7.21.0-py37h888b3d9_0
      ipython_genutils   conda-forge/noarch::ipython_genutils-0.2.0-py_1
      jedi               conda-forge/linux-64::jedi-0.18.0-py37h89c1867_2
      jupyter_client     conda-forge/noarch::jupyter_client-6.1.12-pyhd8ed1ab_0
      jupyter_core       conda-forge/linux-64::jupyter_core-4.7.1-py37h89c1867_0
      ld_impl_linux-64   conda-forge/linux-64::ld_impl_linux-64-2.35.1-hea4e1c9_2
      libffi             conda-forge/linux-64::libffi-3.3-h58526e2_2
      libgcc-ng          conda-forge/linux-64::libgcc-ng-9.3.0-h2828fa1_18
      libgomp            conda-forge/linux-64::libgomp-9.3.0-h2828fa1_18
      libsodium          conda-forge/linux-64::libsodium-1.0.18-h36c2ea0_1
      libstdcxx-ng       conda-forge/linux-64::libstdcxx-ng-9.3.0-h6de172a_18
      ncurses            conda-forge/linux-64::ncurses-6.2-h58526e2_4
      openssl            conda-forge/linux-64::openssl-1.1.1j-h7f98852_0
      parso              conda-forge/noarch::parso-0.8.1-pyhd8ed1ab_0
      pexpect            conda-forge/noarch::pexpect-4.8.0-pyh9f0ad1d_2
      pickleshare        conda-forge/noarch::pickleshare-0.7.5-py_1003
      pip                conda-forge/noarch::pip-21.0.1-pyhd8ed1ab_0
      prompt-toolkit     conda-forge/noarch::prompt-toolkit-3.0.18-pyha770c72_0
      ptyprocess         conda-forge/noarch::ptyprocess-0.7.0-pyhd3deb0d_0
      pygments           conda-forge/noarch::pygments-2.8.1-pyhd8ed1ab_0
      python             conda-forge/linux-64::python-3.7.10-hffdb5ce_100_cpython
      python-dateutil    conda-forge/noarch::python-dateutil-2.8.1-py_0
      python_abi         conda-forge/linux-64::python_abi-3.7-1_cp37m
      pyzmq              conda-forge/linux-64::pyzmq-22.0.3-py37h336d617_1
      readline           conda-forge/linux-64::readline-8.0-he28a2e2_2
      setuptools         conda-forge/linux-64::setuptools-49.6.0-py37h89c1867_3
      six                conda-forge/noarch::six-1.15.0-pyh9f0ad1d_0
      sqlite             conda-forge/linux-64::sqlite-3.35.2-h74cdb3f_0
      tk                 conda-forge/linux-64::tk-8.6.10-h21135ba_1
      tornado            conda-forge/linux-64::tornado-6.1-py37h5e8e339_1
      traitlets          conda-forge/noarch::traitlets-5.0.5-py_0
      wcwidth            conda-forge/noarch::wcwidth-0.2.5-pyh9f0ad1d_2
      wheel              conda-forge/noarch::wheel-0.36.2-pyhd3deb0d_0
      xz                 conda-forge/linux-64::xz-5.2.5-h516909a_1
      zeromq             conda-forge/linux-64::zeromq-4.3.4-h9c3ff4c_0
      zlib               conda-forge/linux-64::zlib-1.2.11-h516909a_1010
    
    
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    #
    # To activate this environment, use
    #
    #     $ conda activate taac2021
    #
    # To deactivate an active environment, use
    #
    #     $ conda deactivate
    
    # conda environments:
    #
    base                     /opt/conda
    JupyterSystemEnv         /opt/conda/envs/JupyterSystemEnv
    mxnet_py2                /opt/conda/envs/mxnet_py2
    mxnet_py3                /opt/conda/envs/mxnet_py3
    python2                  /opt/conda/envs/python2
    python3                  /opt/conda/envs/python3
    pytorch_py2              /opt/conda/envs/pytorch_py2
    pytorch_py3              /opt/conda/envs/pytorch_py3
    taac2021              *  /opt/conda/envs/taac2021
    tensorflow2_py3          /opt/conda/envs/tensorflow2_py3
    tensorflow_py2           /opt/conda/envs/tensorflow_py2
    tensorflow_py3           /opt/conda/envs/tensorflow_py3
    
    Installed kernelspec taac2021 in /home/tione/.local/share/jupyter/kernels/taac2021
    Looking in indexes: http://mirrors.tencentyun.com/pypi/simple
    Collecting pyyaml
      Downloading http://mirrors.tencentyun.com/pypi/packages/7a/a5/393c087efdc78091afa2af9f1378762f9821c9c1d7a22c5753fb5ac5f97a/PyYAML-5.4.1-cp37-cp37m-manylinux1_x86_64.whl (636 kB)
    [K     |████████████████████████████████| 636 kB 10.7 MB/s eta 0:00:01
    [?25hCollecting tqdm
      Downloading http://mirrors.tencentyun.com/pypi/packages/f8/3e/2730d0effc282960dbff3cf91599ad0d8f3faedc8e75720fdf224b31ab24/tqdm-4.59.0-py2.py3-none-any.whl (74 kB)
    [K     |████████████████████████████████| 74 kB 25.6 MB/s eta 0:00:01
    [?25hCollecting munch
      Downloading http://mirrors.tencentyun.com/pypi/packages/cc/ab/85d8da5c9a45e072301beb37ad7f833cd344e04c817d97e0cc75681d248f/munch-2.5.0-py2.py3-none-any.whl (10 kB)
    Collecting resampy
      Using cached resampy-0.2.2-py3-none-any.whl
    Collecting soundfile
      Downloading http://mirrors.tencentyun.com/pypi/packages/eb/f2/3cbbbf3b96fb9fa91582c438b574cff3f45b29c772f94c400e2c99ef5db9/SoundFile-0.10.3.post1-py2.py3-none-any.whl (21 kB)
    Collecting moviepy==1.0.3
      Using cached moviepy-1.0.3-py3-none-any.whl
    Collecting gast==0.2.2
      Using cached gast-0.2.2-py3-none-any.whl
    Requirement already satisfied: ipython in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from -r requirement.txt (line 8)) (7.21.0)
    Collecting jupyter
      Downloading http://mirrors.tencentyun.com/pypi/packages/83/df/0f5dd132200728a86190397e1ea87cd76244e42d39ec5e88efd25b2abd7e/jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
    Collecting matplotlib
      Downloading http://mirrors.tencentyun.com/pypi/packages/23/3d/db9a6b3c83c9511301152dbb64a029c3a4313c86eaef12c237b13ecf91d6/matplotlib-3.3.4-cp37-cp37m-manylinux1_x86_64.whl (11.5 MB)
    [K     |████████████████████████████████| 11.5 MB 1.5 MB/s eta 0:00:011
    [?25hCollecting pandas
      Downloading http://mirrors.tencentyun.com/pypi/packages/f3/d4/3fe3b5bf9886912b64ef040040aec356fa48825e5a829a84c2667afdf952/pandas-1.2.3-cp37-cp37m-manylinux1_x86_64.whl (9.9 MB)
    [K     |████████████████████████████████| 9.9 MB 22.0 MB/s eta 0:00:01
    [?25hCollecting xlrd
      Downloading http://mirrors.tencentyun.com/pypi/packages/a6/0c/c2a72d51fe56e08a08acc85d13013558a2d793028ae7385448a6ccdfae64/xlrd-2.0.1-py2.py3-none-any.whl (96 kB)
    [K     |████████████████████████████████| 96 kB 20.8 MB/s eta 0:00:01
    [?25hCollecting openpyxl
      Downloading http://mirrors.tencentyun.com/pypi/packages/39/08/595298c9b7ced75e7d23be3e7596459980d63bc35112ca765ceccafbe9a4/openpyxl-3.0.7-py2.py3-none-any.whl (243 kB)
    [K     |████████████████████████████████| 243 kB 78.9 MB/s eta 0:00:01
    [?25hCollecting tomorrow3
      Downloading http://mirrors.tencentyun.com/pypi/packages/83/df/9d1a0e45d25804bc88896000c875b846e8adbd406c923d305cc09d62bbed/tomorrow3-1.2.2-py3-none-any.whl (2.2 kB)
    Requirement already satisfied: decorator<5.0,>=4.0.2 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from moviepy==1.0.3->-r requirement.txt (line 6)) (4.4.2)
    Collecting numpy
      Downloading http://mirrors.tencentyun.com/pypi/packages/70/8a/064b4077e3d793f877e3b77aa64f56fa49a4d37236a53f78ee28be009a16/numpy-1.20.1-cp37-cp37m-manylinux2010_x86_64.whl (15.3 MB)
    [K     |████████████████████████████████| 15.3 MB 1.3 MB/s eta 0:00:011  |█████████████▌                  | 6.5 MB 22.1 MB/s eta 0:00:01
    [?25hCollecting imageio-ffmpeg>=0.2.0
      Downloading http://mirrors.tencentyun.com/pypi/packages/89/0f/4b49476d185a273163fa648eaf1e7d4190661d1bbf37ec2975b84df9de02/imageio_ffmpeg-0.4.3-py3-none-manylinux2010_x86_64.whl (26.9 MB)
    [K     |████████████████████████████████| 26.9 MB 394 kB/s eta 0:00:011
    [?25hCollecting proglog<=1.0.0
      Using cached proglog-0.1.9-py3-none-any.whl
    Collecting requests<3.0,>=2.8.1
      Downloading http://mirrors.tencentyun.com/pypi/packages/29/c1/24814557f1d22c56d50280771a17307e6bf87b70727d975fd6b2ce6b014a/requests-2.25.1-py2.py3-none-any.whl (61 kB)
    [K     |████████████████████████████████| 61 kB 14.6 MB/s eta 0:00:01
    [?25hCollecting imageio<3.0,>=2.5
      Downloading http://mirrors.tencentyun.com/pypi/packages/6e/57/5d899fae74c1752f52869b613a8210a2480e1a69688e65df6cb26117d45d/imageio-2.9.0-py3-none-any.whl (3.3 MB)
    [K     |████████████████████████████████| 3.3 MB 20.9 MB/s eta 0:00:01
    [?25hCollecting pillow
      Downloading http://mirrors.tencentyun.com/pypi/packages/1f/6d/b719ae8e21660a6a962636896dc4b7d657ef451a3ab941516401846ac5cb/Pillow-8.1.2-cp37-cp37m-manylinux1_x86_64.whl (2.2 MB)
    [K     |████████████████████████████████| 2.2 MB 10.9 MB/s eta 0:00:01
    [?25hRequirement already satisfied: certifi>=2017.4.17 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from requests<3.0,>=2.8.1->moviepy==1.0.3->-r requirement.txt (line 6)) (2020.12.5)
    Collecting chardet<5,>=3.0.2
      Downloading http://mirrors.tencentyun.com/pypi/packages/19/c7/fa589626997dd07bd87d9269342ccb74b1720384a4d739a1872bd84fbe68/chardet-4.0.0-py2.py3-none-any.whl (178 kB)
    [K     |████████████████████████████████| 178 kB 21.7 MB/s eta 0:00:01
    [?25hCollecting urllib3<1.27,>=1.21.1
      Downloading http://mirrors.tencentyun.com/pypi/packages/09/c6/d3e3abe5b4f4f16cf0dfc9240ab7ce10c2baa0e268989a4e3ec19e90c84e/urllib3-1.26.4-py2.py3-none-any.whl (153 kB)
    [K     |████████████████████████████████| 153 kB 21.8 MB/s eta 0:00:01
    [?25hCollecting idna<3,>=2.5
      Downloading http://mirrors.tencentyun.com/pypi/packages/a2/38/928ddce2273eaa564f6f50de919327bf3a00f091b5baba8dfa9460f3a8a8/idna-2.10-py2.py3-none-any.whl (58 kB)
    [K     |████████████████████████████████| 58 kB 14.6 MB/s eta 0:00:01
    [?25hRequirement already satisfied: pygments in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from ipython->-r requirement.txt (line 8)) (2.8.1)
    Requirement already satisfied: jedi>=0.16 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from ipython->-r requirement.txt (line 8)) (0.18.0)
    Requirement already satisfied: pexpect>4.3 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from ipython->-r requirement.txt (line 8)) (4.8.0)
    Requirement already satisfied: backcall in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from ipython->-r requirement.txt (line 8)) (0.2.0)
    Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from ipython->-r requirement.txt (line 8)) (3.0.18)
    Requirement already satisfied: traitlets>=4.2 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from ipython->-r requirement.txt (line 8)) (5.0.5)
    Requirement already satisfied: pickleshare in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from ipython->-r requirement.txt (line 8)) (0.7.5)
    Requirement already satisfied: setuptools>=18.5 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from ipython->-r requirement.txt (line 8)) (49.6.0.post20210108)
    Requirement already satisfied: parso<0.9.0,>=0.8.0 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from jedi>=0.16->ipython->-r requirement.txt (line 8)) (0.8.1)
    Requirement already satisfied: ptyprocess>=0.5 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from pexpect>4.3->ipython->-r requirement.txt (line 8)) (0.7.0)
    Requirement already satisfied: wcwidth in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython->-r requirement.txt (line 8)) (0.2.5)
    Requirement already satisfied: ipython-genutils in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from traitlets>=4.2->ipython->-r requirement.txt (line 8)) (0.2.0)
    Collecting jupyter-console
      Downloading http://mirrors.tencentyun.com/pypi/packages/59/cd/aa2670ffc99eb3e5bbe2294c71e4bf46a9804af4f378d09d7a8950996c9b/jupyter_console-6.4.0-py3-none-any.whl (22 kB)
    Collecting notebook
      Downloading http://mirrors.tencentyun.com/pypi/packages/5d/86/8f951abc6ac651a75a059d2b77fe99fa5df80bf4dc4700c126a0bee486b8/notebook-6.3.0-py3-none-any.whl (9.5 MB)
    [K     |████████████████████████████████| 9.5 MB 78.0 MB/s eta 0:00:01
    [?25hCollecting qtconsole
      Downloading http://mirrors.tencentyun.com/pypi/packages/22/4d/94cb45a6f0c25a2693f7c8c0fe0814c3f52ba0f9c920ad75104005b31d42/qtconsole-5.0.3-py3-none-any.whl (119 kB)
    [K     |████████████████████████████████| 119 kB 122.0 MB/s eta 0:00:01
    [?25hRequirement already satisfied: ipykernel in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from jupyter->-r requirement.txt (line 9)) (5.5.0)
    Collecting ipywidgets
      Downloading http://mirrors.tencentyun.com/pypi/packages/11/53/084940a83a8158364e630a664a30b03068c25ab75243224d6b488800d43a/ipywidgets-7.6.3-py2.py3-none-any.whl (121 kB)
    [K     |████████████████████████████████| 121 kB 116.0 MB/s eta 0:00:01
    [?25hCollecting nbconvert
      Downloading http://mirrors.tencentyun.com/pypi/packages/13/2f/acbe7006548f3914456ee47f97a2033b1b2f3daf921b12ac94105d87c163/nbconvert-6.0.7-py3-none-any.whl (552 kB)
    [K     |████████████████████████████████| 552 kB 85.8 MB/s eta 0:00:01
    [?25hCollecting cycler>=0.10
      Downloading http://mirrors.tencentyun.com/pypi/packages/f7/d2/e07d3ebb2bd7af696440ce7e754c59dd546ffe1bbe732c8ab68b9c834e61/cycler-0.10.0-py2.py3-none-any.whl (6.5 kB)
    Collecting kiwisolver>=1.0.1
      Downloading http://mirrors.tencentyun.com/pypi/packages/d2/46/231de802ade4225b76b96cffe419cf3ce52bbe92e3b092cf12db7d11c207/kiwisolver-1.3.1-cp37-cp37m-manylinux1_x86_64.whl (1.1 MB)
    [K     |████████████████████████████████| 1.1 MB 76.8 MB/s eta 0:00:01
    [?25hCollecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3
      Downloading http://mirrors.tencentyun.com/pypi/packages/8a/bb/488841f56197b13700afd5658fc279a2025a39e22449b7cf29864669b15d/pyparsing-2.4.7-py2.py3-none-any.whl (67 kB)
    [K     |████████████████████████████████| 67 kB 15.4 MB/s eta 0:00:01
    [?25hRequirement already satisfied: python-dateutil>=2.1 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from matplotlib->-r requirement.txt (line 10)) (2.8.1)
    Requirement already satisfied: six in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from cycler>=0.10->matplotlib->-r requirement.txt (line 10)) (1.15.0)
    Collecting et-xmlfile
      Using cached et_xmlfile-1.0.1-py3-none-any.whl
    Collecting pytz>=2017.3
      Downloading http://mirrors.tencentyun.com/pypi/packages/70/94/784178ca5dd892a98f113cdd923372024dc04b8d40abe77ca76b5fb90ca6/pytz-2021.1-py2.py3-none-any.whl (510 kB)
    [K     |████████████████████████████████| 510 kB 21.3 MB/s eta 0:00:01
    [?25hCollecting scipy>=0.13
      Downloading http://mirrors.tencentyun.com/pypi/packages/75/91/ee427c42957f8c4cbe477bf4f8b7f608e003a17941e509d1777e58648cb3/scipy-1.6.2-cp37-cp37m-manylinux1_x86_64.whl (27.4 MB)
    [K     |████████████████████████████████| 27.4 MB 844 kB/s eta 0:00:011
    [?25hCollecting numba>=0.32
      Downloading http://mirrors.tencentyun.com/pypi/packages/92/e8/4f67aa44b86333528e04dc8820f7e8058753582d8a0867324a2b818ef516/numba-0.53.0-cp37-cp37m-manylinux2014_x86_64.whl (3.4 MB)
    [K     |████████████████████████████████| 3.4 MB 49.6 MB/s eta 0:00:01
    [?25hCollecting llvmlite<0.37,>=0.36.0rc1
      Downloading http://mirrors.tencentyun.com/pypi/packages/54/25/2b4015e2b0c3be2efa6870cf2cf2bd969dd0e5f937476fc13c102209df32/llvmlite-0.36.0-cp37-cp37m-manylinux2010_x86_64.whl (25.3 MB)
    [K     |████████████████████████████████| 25.3 MB 443 kB/s eta 0:00:011
    [?25hCollecting cffi>=1.0
      Downloading http://mirrors.tencentyun.com/pypi/packages/97/2d/cd29c79f2eb1384577d0662f23c89d29621152f14bef8c6b25747785744b/cffi-1.14.5-cp37-cp37m-manylinux1_x86_64.whl (402 kB)
    [K     |████████████████████████████████| 402 kB 37.8 MB/s eta 0:00:01
    [?25hCollecting pycparser
      Downloading http://mirrors.tencentyun.com/pypi/packages/ae/e7/d9c3a176ca4b02024debf82342dab36efadfc5776f9c8db077e8f6e71821/pycparser-2.20-py2.py3-none-any.whl (112 kB)
    [K     |████████████████████████████████| 112 kB 20.5 MB/s eta 0:00:01
    [?25hRequirement already satisfied: jupyter-client in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from ipykernel->jupyter->-r requirement.txt (line 9)) (6.1.12)
    Requirement already satisfied: tornado>=4.2 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from ipykernel->jupyter->-r requirement.txt (line 9)) (6.1)
    Collecting jupyterlab-widgets>=1.0.0
      Downloading http://mirrors.tencentyun.com/pypi/packages/18/b5/3473d275e3b2359efdf5768e9df95537308b93a31ad94fa92814ac565826/jupyterlab_widgets-1.0.0-py3-none-any.whl (243 kB)
    [K     |████████████████████████████████| 243 kB 77.7 MB/s eta 0:00:01
    [?25hCollecting widgetsnbextension~=3.5.0
      Downloading http://mirrors.tencentyun.com/pypi/packages/6c/7b/7ac231c20d2d33c445eaacf8a433f4e22c60677eb9776c7c5262d7ddee2d/widgetsnbextension-3.5.1-py2.py3-none-any.whl (2.2 MB)
    [K     |████████████████████████████████| 2.2 MB 88.5 MB/s eta 0:00:01
    [?25hCollecting nbformat>=4.2.0
      Downloading http://mirrors.tencentyun.com/pypi/packages/13/1d/59cbc5a6b627ba3b4c0ec5ccc82a9002e58b324e2620a4929b81f1f8d309/nbformat-5.1.2-py3-none-any.whl (113 kB)
    [K     |████████████████████████████████| 113 kB 99.5 MB/s eta 0:00:01
    [?25hRequirement already satisfied: jupyter-core in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from nbformat>=4.2.0->ipywidgets->jupyter->-r requirement.txt (line 9)) (4.7.1)
    Collecting jsonschema!=2.5.0,>=2.4
      Downloading http://mirrors.tencentyun.com/pypi/packages/c5/8f/51e89ce52a085483359217bc72cdbf6e75ee595d5b1d4b5ade40c7e018b8/jsonschema-3.2.0-py2.py3-none-any.whl (56 kB)
    [K     |████████████████████████████████| 56 kB 91.0 MB/s  eta 0:00:01
    [?25hCollecting pyrsistent>=0.14.0
      Using cached pyrsistent-0.17.3-cp37-cp37m-linux_x86_64.whl
    Collecting importlib-metadata
      Downloading http://mirrors.tencentyun.com/pypi/packages/80/5d/0bbca82b16e01313cf0343167d4cfb90f6fade747cd4d10d368094b2883a/importlib_metadata-3.7.3-py3-none-any.whl (12 kB)
    Collecting attrs>=17.4.0
      Downloading http://mirrors.tencentyun.com/pypi/packages/c3/aa/cb45262569fcc047bf070b5de61813724d6726db83259222cd7b4c79821a/attrs-20.3.0-py2.py3-none-any.whl (49 kB)
    [K     |████████████████████████████████| 49 kB 12.1 MB/s eta 0:00:01
    [?25hCollecting argon2-cffi
      Downloading http://mirrors.tencentyun.com/pypi/packages/e0/d7/5da06217807106ed6d7b4f5ccb8ec5e3f9ec969217faad4b5d1af0b55101/argon2_cffi-20.1.0-cp35-abi3-manylinux1_x86_64.whl (97 kB)
    [K     |████████████████████████████████| 97 kB 105.4 MB/s eta 0:00:01
    [?25hCollecting Send2Trash>=1.5.0
      Downloading http://mirrors.tencentyun.com/pypi/packages/49/46/c3dc27481d1cc57b9385aff41c474ceb7714f7935b1247194adae45db714/Send2Trash-1.5.0-py3-none-any.whl (12 kB)
    Collecting prometheus-client
      Downloading http://mirrors.tencentyun.com/pypi/packages/f4/7e/ef341c67ed43ad2e39633a35c28b77bc555f9572f4df4fee11c2b467db00/prometheus_client-0.9.0-py2.py3-none-any.whl (53 kB)
    [K     |████████████████████████████████| 53 kB 12.9 MB/s eta 0:00:01
    [?25hCollecting terminado>=0.8.3
      Downloading http://mirrors.tencentyun.com/pypi/packages/c9/cf/55051993a27eca8df8ff7362a0c98dded6fc6f66b6e322513fde3d195cda/terminado-0.9.3-py3-none-any.whl (14 kB)
    Collecting jinja2
      Downloading http://mirrors.tencentyun.com/pypi/packages/7e/c2/1eece8c95ddbc9b1aeb64f5783a9e07a286de42191b7204d67b7496ddf35/Jinja2-2.11.3-py2.py3-none-any.whl (125 kB)
    [K     |████████████████████████████████| 125 kB 21.2 MB/s eta 0:00:01
    [?25hRequirement already satisfied: pyzmq>=17 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from notebook->jupyter->-r requirement.txt (line 9)) (22.0.3)
    Collecting zipp>=0.5
      Downloading http://mirrors.tencentyun.com/pypi/packages/0f/8c/715c54e9e34c0c4820f616a913a7de3337d0cd79074dd1bed4dd840f16ae/zipp-3.4.1-py3-none-any.whl (5.2 kB)
    Collecting typing-extensions>=3.6.4
      Downloading http://mirrors.tencentyun.com/pypi/packages/60/7a/e881b5abb54db0e6e671ab088d079c57ce54e8a01a3ca443f561ccadb37e/typing_extensions-3.7.4.3-py3-none-any.whl (22 kB)
    Collecting MarkupSafe>=0.23
      Downloading http://mirrors.tencentyun.com/pypi/packages/c2/37/2e4def8ce3739a258998215df907f5815ecd1af71e62147f5eea2d12d4e8/MarkupSafe-1.1.1-cp37-cp37m-manylinux2010_x86_64.whl (33 kB)
    Collecting mistune<2,>=0.8.1
      Downloading http://mirrors.tencentyun.com/pypi/packages/09/ec/4b43dae793655b7d8a25f76119624350b4d65eb663459eb9603d7f1f0345/mistune-0.8.4-py2.py3-none-any.whl (16 kB)
    Collecting entrypoints>=0.2.2
      Downloading http://mirrors.tencentyun.com/pypi/packages/ac/c6/44694103f8c221443ee6b0041f69e2740d89a25641e62fb4f2ee568f2f9c/entrypoints-0.3-py2.py3-none-any.whl (11 kB)
    Collecting pandocfilters>=1.4.1
      Using cached pandocfilters-1.4.3-py3-none-any.whl
    Collecting bleach
      Downloading http://mirrors.tencentyun.com/pypi/packages/f0/46/2bbd92086a4c6f051214cb48df6d9132b5f32c5e881d3f4991b16ec7e499/bleach-3.3.0-py2.py3-none-any.whl (283 kB)
    [K     |████████████████████████████████| 283 kB 7.6 MB/s eta 0:00:01
    [?25hCollecting nbclient<0.6.0,>=0.5.0
      Downloading http://mirrors.tencentyun.com/pypi/packages/22/a6/f3a01a5c1a0e72d1d064f33d4cd9c3a782010f48f48f47f256d0b438994a/nbclient-0.5.3-py3-none-any.whl (82 kB)
    [K     |████████████████████████████████| 82 kB 11.4 MB/s eta 0:00:01
    [?25hCollecting testpath
      Downloading http://mirrors.tencentyun.com/pypi/packages/1b/9e/1a170feaa54f22aeb5a5d16c9015e82234275a3c8ab630b552493f9cb8a9/testpath-0.4.4-py2.py3-none-any.whl (163 kB)
    [K     |████████████████████████████████| 163 kB 17.0 MB/s eta 0:00:01
    [?25hCollecting defusedxml
      Downloading http://mirrors.tencentyun.com/pypi/packages/07/6c/aa3f2f849e01cb6a001cd8554a88d4c77c5c1a31c95bdf1cf9301e6d9ef4/defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
    Collecting jupyterlab-pygments
      Downloading http://mirrors.tencentyun.com/pypi/packages/a8/6f/c34288766797193b512c6508f5994b830fb06134fdc4ca8214daba0aa443/jupyterlab_pygments-0.1.2-py2.py3-none-any.whl (4.6 kB)
    Collecting nest-asyncio
      Downloading http://mirrors.tencentyun.com/pypi/packages/52/e2/9b37da54e6e9094d2f558ae643d1954a0fa8215dfee4fa261f31c5439796/nest_asyncio-1.5.1-py3-none-any.whl (5.0 kB)
    Collecting async-generator
      Downloading http://mirrors.tencentyun.com/pypi/packages/71/52/39d20e03abd0ac9159c162ec24b93fbcaa111e8400308f2465432495ca2b/async_generator-1.10-py3-none-any.whl (18 kB)
    Collecting packaging
      Downloading http://mirrors.tencentyun.com/pypi/packages/3e/89/7ea760b4daa42653ece2380531c90f64788d979110a2ab51049d92f408af/packaging-20.9-py2.py3-none-any.whl (40 kB)
    [K     |████████████████████████████████| 40 kB 18.1 MB/s eta 0:00:01
    [?25hCollecting webencodings
      Downloading http://mirrors.tencentyun.com/pypi/packages/f4/24/2a3e3df732393fed8b3ebf2ec078f05546de641fe1b667ee316ec1dcf3b7/webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
    Collecting qtpy
      Downloading http://mirrors.tencentyun.com/pypi/packages/cd/fd/9972948f02e967b691cc0ca1f26124826a3b88cb38f412a8b7935b8c3c72/QtPy-1.9.0-py2.py3-none-any.whl (54 kB)
    [K     |████████████████████████████████| 54 kB 17.5 MB/s eta 0:00:01
    [?25hInstalling collected packages: zipp, typing-extensions, pyrsistent, importlib-metadata, attrs, pyparsing, jsonschema, webencodings, pycparser, packaging, nest-asyncio, nbformat, MarkupSafe, async-generator, testpath, pandocfilters, nbclient, mistune, jupyterlab-pygments, jinja2, entrypoints, defusedxml, cffi, bleach, terminado, Send2Trash, prometheus-client, nbconvert, argon2-cffi, notebook, widgetsnbextension, urllib3, tqdm, qtpy, pillow, numpy, llvmlite, jupyterlab-widgets, idna, chardet, scipy, requests, qtconsole, pytz, proglog, numba, kiwisolver, jupyter-console, ipywidgets, imageio-ffmpeg, imageio, et-xmlfile, cycler, xlrd, tomorrow3, soundfile, resampy, pyyaml, pandas, openpyxl, munch, moviepy, matplotlib, jupyter, gast
    Successfully installed MarkupSafe-1.1.1 Send2Trash-1.5.0 argon2-cffi-20.1.0 async-generator-1.10 attrs-20.3.0 bleach-3.3.0 cffi-1.14.5 chardet-4.0.0 cycler-0.10.0 defusedxml-0.7.1 entrypoints-0.3 et-xmlfile-1.0.1 gast-0.2.2 idna-2.10 imageio-2.9.0 imageio-ffmpeg-0.4.3 importlib-metadata-3.7.3 ipywidgets-7.6.3 jinja2-2.11.3 jsonschema-3.2.0 jupyter-1.0.0 jupyter-console-6.4.0 jupyterlab-pygments-0.1.2 jupyterlab-widgets-1.0.0 kiwisolver-1.3.1 llvmlite-0.36.0 matplotlib-3.3.4 mistune-0.8.4 moviepy-1.0.3 munch-2.5.0 nbclient-0.5.3 nbconvert-6.0.7 nbformat-5.1.2 nest-asyncio-1.5.1 notebook-6.3.0 numba-0.53.0 numpy-1.20.1 openpyxl-3.0.7 packaging-20.9 pandas-1.2.3 pandocfilters-1.4.3 pillow-8.1.2 proglog-0.1.9 prometheus-client-0.9.0 pycparser-2.20 pyparsing-2.4.7 pyrsistent-0.17.3 pytz-2021.1 pyyaml-5.4.1 qtconsole-5.0.3 qtpy-1.9.0 requests-2.25.1 resampy-0.2.2 scipy-1.6.2 soundfile-0.10.3.post1 terminado-0.9.3 testpath-0.4.4 tomorrow3-1.2.2 tqdm-4.59.0 typing-extensions-3.7.4.3 urllib3-1.26.4 webencodings-0.5.1 widgetsnbextension-3.5.1 xlrd-2.0.1 zipp-3.4.1
    Looking in indexes: http://mirrors.tencentyun.com/pypi/simple
    Collecting tensorflow-gpu==1.14
      Downloading http://mirrors.tencentyun.com/pypi/packages/32/67/559ca8408431c37ad3a17e859c8c291ea82f092354074baef482b98ffb7b/tensorflow_gpu-1.14.0-cp37-cp37m-manylinux1_x86_64.whl (377.1 MB)
    [K     |████████████████████████████████| 377.1 MB 224 kB/s eta 0:00:0101    |███████████▍                    | 133.9 MB 429 kB/s eta 0:09:27     |█████████████████▌              | 206.0 MB 513 kB/s eta 0:05:34��█████████████████████          | 259.1 MB 1.0 MB/s eta 0:01:54████▋         | 266.0 MB 186.6 MB/s eta 0:00:01��        | 274.8 MB 71 kB/s eta 0:23:45��        | 281.6 MB 71 kB/s eta 0:22:11��█████████████████       | 293.3 MB 137 kB/s eta 0:10:11     |██████████████████████████████  | 354.6 MB 287 kB/s eta 0:01:193 MB 371 kB/s eta 0:00:29
    [?25hCollecting opencv-python
      Downloading http://mirrors.tencentyun.com/pypi/packages/0f/13/192104516c4a3d92dc6b5e106ffcfbf0fe35f3c4faa49650205ff652af72/opencv_python-4.5.1.48-cp37-cp37m-manylinux2014_x86_64.whl (50.4 MB)
    [K     |████████████████████████████████| 50.4 MB 216 kB/s eta 0:00:011     |█████████████████████████████▊  | 46.9 MB 352 kB/s eta 0:00:11
    [?25hCollecting torch
      Downloading http://mirrors.tencentyun.com/pypi/packages/94/99/5861239a6e1ffe66e120f114a4d67e96e5c4b17c1a785dfc6ca6769585fc/torch-1.8.0-cp37-cp37m-manylinux1_x86_64.whl (735.5 MB)
    [K     |████████████████████████████████| 735.5 MB 153 kB/s eta 0:00:0131    |████████▉                       | 203.6 MB 131 kB/s eta 1:07:34     |███████████▍                    | 261.6 MB 342 kB/s eta 0:23:05     |████████████████▎               | 374.6 MB 45.7 MB/s eta 0:00:08��█▏            | 441.7 MB 58.6 MB/s eta 0:00:06��████████████████████▍          | 491.6 MB 315 kB/s eta 0:12:55     |██████████████████████          | 507.1 MB 336 kB/s eta 0:11:20��████████████████▋       | 566.1 MB 436 kB/s eta 0:06:29 | 606.7 MB 338 kB/s eta 0:06:20    |█████████████████████████████▋  | 681.3 MB 367 kB/s eta 0:02:282 MB 393 kB/s eta 0:01:056 MB 393 kB/s eta 0:00:59███████▏| 716.6 MB 393 kB/s eta 0:00:49███████▍| 721.2 MB 393 kB/s eta 0:00:37
    [?25hCollecting keras-applications>=1.0.6
      Downloading http://mirrors.tencentyun.com/pypi/packages/71/e3/19762fdfc62877ae9102edf6342d71b28fbfd9dea3d2f96a882ce099b03f/Keras_Applications-1.0.8-py3-none-any.whl (50 kB)
    [K     |████████████████████████████████| 50 kB 7.6 MB/s eta 0:00:011
    [?25hCollecting tensorboard<1.15.0,>=1.14.0
      Downloading http://mirrors.tencentyun.com/pypi/packages/91/2d/2ed263449a078cd9c8a9ba50ebd50123adf1f8cfbea1492f9084169b89d9/tensorboard-1.14.0-py3-none-any.whl (3.1 MB)
    [K     |████████████████████████████████| 3.1 MB 10.9 MB/s eta 0:00:01
    [?25hCollecting wrapt>=1.11.1
      Using cached wrapt-1.12.1-cp37-cp37m-linux_x86_64.whl
    Collecting grpcio>=1.8.6
      Downloading http://mirrors.tencentyun.com/pypi/packages/81/6f/6d292b7012abe5dd797259d10a788935bfc96bc6c835f2d529d95f1e388e/grpcio-1.36.1-cp37-cp37m-manylinux2014_x86_64.whl (4.1 MB)
    [K     |████████████████████████████████| 4.1 MB 11.0 MB/s eta 0:00:01
    [?25hRequirement already satisfied: six>=1.10.0 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from tensorflow-gpu==1.14) (1.15.0)
    Collecting absl-py>=0.7.0
      Downloading http://mirrors.tencentyun.com/pypi/packages/92/c9/ef0fae29182d7a867d203f0eff8296b60da92098cc41db33a434f4be84bf/absl_py-0.12.0-py3-none-any.whl (129 kB)
    [K     |████████████████████████████████| 129 kB 20.9 MB/s eta 0:00:01
    [?25hCollecting tensorflow-estimator<1.15.0rc0,>=1.14.0rc0
      Downloading http://mirrors.tencentyun.com/pypi/packages/3c/d5/21860a5b11caf0678fbc8319341b0ae21a07156911132e0e71bffed0510d/tensorflow_estimator-1.14.0-py2.py3-none-any.whl (488 kB)
    [K     |████████████████████████████████| 488 kB 69.8 MB/s eta 0:00:01
    [?25hCollecting google-pasta>=0.1.6
      Downloading http://mirrors.tencentyun.com/pypi/packages/a3/de/c648ef6835192e6e2cc03f40b19eeda4382c49b5bafb43d88b931c4c74ac/google_pasta-0.2.0-py3-none-any.whl (57 kB)
    [K     |████████████████████████████████| 57 kB 13.8 MB/s eta 0:00:01
    [?25hCollecting termcolor>=1.1.0
      Using cached termcolor-1.1.0-py3-none-any.whl
    Collecting astor>=0.6.0
      Downloading http://mirrors.tencentyun.com/pypi/packages/c3/88/97eef84f48fa04fbd6750e62dcceafba6c63c81b7ac1420856c8dcc0a3f9/astor-0.8.1-py2.py3-none-any.whl (27 kB)
    Collecting keras-preprocessing>=1.0.5
      Downloading http://mirrors.tencentyun.com/pypi/packages/79/4c/7c3275a01e12ef9368a892926ab932b33bb13d55794881e3573482b378a7/Keras_Preprocessing-1.1.2-py2.py3-none-any.whl (42 kB)
    [K     |████████████████████████████████| 42 kB 11.1 MB/s eta 0:00:01
    [?25hRequirement already satisfied: gast>=0.2.0 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from tensorflow-gpu==1.14) (0.2.2)
    Requirement already satisfied: numpy<2.0,>=1.14.5 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from tensorflow-gpu==1.14) (1.20.1)
    Requirement already satisfied: wheel>=0.26 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from tensorflow-gpu==1.14) (0.36.2)
    Collecting protobuf>=3.6.1
      Downloading http://mirrors.tencentyun.com/pypi/packages/7d/cc/abf8e30629db7a8b15efb79d4c87e235895d2c636ce7a4ac625cfc816f07/protobuf-3.15.6-cp37-cp37m-manylinux1_x86_64.whl (1.0 MB)
    [K     |████████████████████████████████| 1.0 MB 20.8 MB/s eta 0:00:01
    [?25hCollecting h5py
      Downloading http://mirrors.tencentyun.com/pypi/packages/b3/c5/94e2444eb691f658fb8e3cf6cde3ae29540cf6d9ce76f0561afcdbb89136/h5py-3.2.1-cp37-cp37m-manylinux1_x86_64.whl (4.1 MB)
    [K     |████████████████████████████████| 4.1 MB 78.4 MB/s eta 0:00:01
    [?25hCollecting werkzeug>=0.11.15
      Downloading http://mirrors.tencentyun.com/pypi/packages/cc/94/5f7079a0e00bd6863ef8f1da638721e9da21e5bacee597595b318f71d62e/Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
    [K     |████████████████████████████████| 298 kB 80.0 MB/s eta 0:00:01
    [?25hRequirement already satisfied: setuptools>=41.0.0 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from tensorboard<1.15.0,>=1.14.0->tensorflow-gpu==1.14) (49.6.0.post20210108)
    Collecting markdown>=2.6.8
      Downloading http://mirrors.tencentyun.com/pypi/packages/6e/33/1ae0f71395e618d6140fbbc9587cc3156591f748226075e0f7d6f9176522/Markdown-3.3.4-py3-none-any.whl (97 kB)
    [K     |████████████████████████████████| 97 kB 21.1 MB/s eta 0:00:01
    [?25hRequirement already satisfied: importlib-metadata in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from markdown>=2.6.8->tensorboard<1.15.0,>=1.14.0->tensorflow-gpu==1.14) (3.7.3)
    Requirement already satisfied: typing-extensions in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from torch) (3.7.4.3)
    Collecting cached-property
      Downloading http://mirrors.tencentyun.com/pypi/packages/48/19/f2090f7dad41e225c7f2326e4cfe6fff49e57dedb5b53636c9551f86b069/cached_property-1.5.2-py2.py3-none-any.whl (7.6 kB)
    Requirement already satisfied: zipp>=0.5 in /opt/conda/envs/taac2021/lib/python3.7/site-packages (from importlib-metadata->markdown>=2.6.8->tensorboard<1.15.0,>=1.14.0->tensorflow-gpu==1.14) (3.4.1)
    Installing collected packages: cached-property, werkzeug, protobuf, markdown, h5py, grpcio, absl-py, wrapt, termcolor, tensorflow-estimator, tensorboard, keras-preprocessing, keras-applications, google-pasta, astor, torch, tensorflow-gpu, opencv-python
    Successfully installed absl-py-0.12.0 astor-0.8.1 cached-property-1.5.2 google-pasta-0.2.0 grpcio-1.36.1 h5py-3.2.1 keras-applications-1.0.8 keras-preprocessing-1.1.2 markdown-3.3.4 opencv-python-4.5.1.48 protobuf-3.15.6 tensorboard-1.14.0 tensorflow-estimator-1.14.0 tensorflow-gpu-1.14.0 termcolor-1.1.0 torch-1.8.0 werkzeug-1.0.1 wrapt-1.12.1


如果创建TI-Notebook后，执行过 ./init.sh run，但是关停了实例再重启，由于系统盘上的数据被清空，相应的conda环境和jupyter kernel可能会清空，可运行 ./run.sh fix 进行修复。


```python
!cd ~/notebook/VideoStructuring && sudo chmod a+x ./run.sh && ./run.sh fix
```

## 环境测试

准备好环境后，可以测试一下环境是否准备成功。  
将 notebook 的右上角 kernel 换成 TAAC2021 (taac2021-tagging)，然后执行下述代码，如果是 tf1.14 则说明环境准备成功。


```python
import tensorflow as tf
print(tf.__version__)
```

也可以运行一下下述命令，看看虚拟环境是否正常创建。


```python
!conda info --envs | grep taac2021
```

    taac2021                 /opt/conda/envs/taac2021


## 模型训练

训练模型之前需要链接一下数据集，将VideoStructuring/dataset链接到/home/tione/notebook/algo-2021/dataset

比赛的数据存放在只读共享盘/home/tione/notebook/algo-2021/baseline/dataset/目录中，用户需要先复制到TI-Notebook实例的数据盘（挂载目录为/home/tione/notebook/）中。  


```python
! time cp -r -d /home/tione/notebook/algo-2021/baseline/dataset /home/tione/notebook/
```

训练模型之前需要链接一下数据集，将/home/tione/notebook/dataset/链接到/home/tione/notebook/VideoStructuring/dataset/  


```python
!ln -s /home/tione/notebook/algo-2021/baseline/dataset /home/tione/notebook/VideoStructuring/dataset
```

对于标签预测，需要完成特征提取（./run.sh extract）与数据集生成（./run.sh gt）两项任务。  
为了简化操作，baseline已完成了前置步骤，用户可以直接使用下列脚本进行视频标签模型的训练。  
训练完成后，模型存在于VideoStructuring/MultiModal-Tagging/checkpoints/目录下。  


```python
!cd ~/notebook/VideoStructuring && sudo chmod a+x ./run.sh && ./run.sh train
```

    CONDA_CONFIG_ROOT_PREFIX= root_prefix: /opt/conda
    CONDA_ROOT= /opt/conda
    TAAC2021_ENV= taac2021
    JUPYTER_ROOT= /home/tione/notebook
    CODE_ROOT= /home/tione/notebook/MultiModal-Tagging
    # conda environments:
    #
    base                     /opt/conda
    JupyterSystemEnv         /opt/conda/envs/JupyterSystemEnv
    mxnet_py2                /opt/conda/envs/mxnet_py2
    mxnet_py3                /opt/conda/envs/mxnet_py3
    python2                  /opt/conda/envs/python2
    python3                  /opt/conda/envs/python3
    pytorch_py2              /opt/conda/envs/pytorch_py2
    pytorch_py3              /opt/conda/envs/pytorch_py3
    taac2021              *  /opt/conda/envs/taac2021
    tensorflow2_py3          /opt/conda/envs/tensorflow2_py3
    tensorflow_py2           /opt/conda/envs/tensorflow_py2
    tensorflow_py3           /opt/conda/envs/tensorflow_py3
    
    /home/tione/notebook/MultiModal-Tagging
    Info: TYPE is train
    Info: training with config= /home/tione/notebook/MultiModal-Tagging/config.tagging.yaml
    /opt/conda/envs/taac2021/lib/python3.7/site-packages/tensorflow/python/framework/dtypes.py:516: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
      _np_qint8 = np.dtype([("qint8", np.int8, 1)])
    /opt/conda/envs/taac2021/lib/python3.7/site-packages/tensorflow/python/framework/dtypes.py:517: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
      _np_quint8 = np.dtype([("quint8", np.uint8, 1)])
    /opt/conda/envs/taac2021/lib/python3.7/site-packages/tensorflow/python/framework/dtypes.py:518: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
      _np_qint16 = np.dtype([("qint16", np.int16, 1)])
    /opt/conda/envs/taac2021/lib/python3.7/site-packages/tensorflow/python/framework/dtypes.py:519: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
      _np_quint16 = np.dtype([("quint16", np.uint16, 1)])
    /opt/conda/envs/taac2021/lib/python3.7/site-packages/tensorflow/python/framework/dtypes.py:520: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
      _np_qint32 = np.dtype([("qint32", np.int32, 1)])
    /opt/conda/envs/taac2021/lib/python3.7/site-packages/tensorflow/python/framework/dtypes.py:525: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
      np_resource = np.dtype([("resource", np.ubyte, 1)])
    /opt/conda/envs/taac2021/lib/python3.7/site-packages/tensorboard/compat/tensorflow_stub/dtypes.py:541: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
      _np_qint8 = np.dtype([("qint8", np.int8, 1)])
    /opt/conda/envs/taac2021/lib/python3.7/site-packages/tensorboard/compat/tensorflow_stub/dtypes.py:542: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
      _np_quint8 = np.dtype([("quint8", np.uint8, 1)])
    /opt/conda/envs/taac2021/lib/python3.7/site-packages/tensorboard/compat/tensorflow_stub/dtypes.py:543: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
      _np_qint16 = np.dtype([("qint16", np.int16, 1)])
    /opt/conda/envs/taac2021/lib/python3.7/site-packages/tensorboard/compat/tensorflow_stub/dtypes.py:544: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
      _np_quint16 = np.dtype([("quint16", np.uint16, 1)])
    /opt/conda/envs/taac2021/lib/python3.7/site-packages/tensorboard/compat/tensorflow_stub/dtypes.py:545: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
      _np_qint32 = np.dtype([("qint32", np.int32, 1)])
    /opt/conda/envs/taac2021/lib/python3.7/site-packages/tensorboard/compat/tensorflow_stub/dtypes.py:550: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
      np_resource = np.dtype([("resource", np.ubyte, 1)])
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/src/model/text_head/bert_model.py:5: The name tf.AUTO_REUSE is deprecated. Please use tf.compat.v1.AUTO_REUSE instead.
    
    /home/tione/notebook/MultiModal-Tagging/utils/base_trainer.py:393: YAMLLoadWarning: calling yaml.load() without Loader=... is deprecated, as the default Loader is unsafe. Please read https://msg.pyyaml.org/load for full details.
      config = yaml.load(open(config_path))
    {'ModelConfig': {'model_type': 'NextVladBERT', 'use_modal_drop': True, 'with_embedding_bn': False, 'modal_drop_rate': 0.3, 'with_video_head': True, 'with_audio_head': True, 'with_text_head': True, 'with_image_head': True, 'video_head_type': 'NeXtVLAD', 'video_head_params': {'nextvlad_cluster_size': 128, 'groups': 16, 'expansion': 2, 'feature_size': 1024, 'max_frames': 300}, 'audio_head_type': 'NeXtVLAD', 'audio_head_params': {'nextvlad_cluster_size': 64, 'groups': 16, 'expansion': 2, 'feature_size': 128, 'max_frames': 300}, 'text_head_type': 'BERT', 'text_head_params': {'bert_config': {'attention_probs_dropout_prob': 0.1, 'hidden_act': 'gelu', 'hidden_dropout_prob': 0.1, 'hidden_size': 768, 'initializer_range': 0.02, 'intermediate_size': 3072, 'max_position_embeddings': 512, 'num_attention_heads': 12, 'num_hidden_layers': 12, 'type_vocab_size': 2, 'vocab_size': 21128}, 'bert_emb_encode_size': 1024}, 'image_head_type': 'resnet_v2_50', 'image_head_params': {}, 'fusion_head_type': 'SE', 'fusion_head_params': {'hidden1_size': 1024, 'gating_reduction': 8, 'drop_rate': {'video': 0.8, 'audio': 0.5, 'image': 0.5, 'text': 0.5, 'fusion': 0.8}}, 'tagging_classifier_type': 'LogisticModel', 'tagging_classifier_params': {'num_classes': 267}}, 'OptimizerConfig': {'optimizer': 'AdamOptimizer', 'optimizer_init_params': {}, 'clip_gradient_norm': 1.0, 'learning_rate_dict': {'video': 0.0001, 'audio': 0.0001, 'text': 1e-05, 'image': 0.0001, 'classifier': 0.01}, 'loss_type_dict': {'tagging': 'CrossEntropyLoss'}, 'max_step_num': 10000, 'export_model_steps': 1000, 'learning_rate_decay': 0.1, 'start_new_model': True, 'num_gpu': 1, 'log_device_placement': False, 'gpu_allow_growth': True, 'pretrained_model': {'text_pretrained_model': 'pretrained/bert/chinese_L-12_H-768_A-12/bert_model.ckpt', 'image_pretrained_model': 'pretrained/resnet_v2_50/resnet_v2_50.ckpt'}, 'train_dir': 'checkpoints/tagging_train799'}, 'DatasetConfig': {'batch_size': 32, 'shuffle': True, 'train_data_source_list': {'train799': {'file': '/home/tione/notebook/tagging-dataset/data_files/tagging/Youtube8M-Vggish-tagging_b0/train.txt', 'batch_size': 32}}, 'valid_data_source_list': {'val799': {'file': '/home/tione/notebook/tagging-dataset/data_files/tagging/Youtube8M-Vggish-tagging_b0/val.txt', 'batch_size': 32}}, 'preprocess_root': 'src/dataloader/preprocess/', 'preprocess_config': {'feature': [{'name': 'video,video_frames_num,idx', 'shape': [[300, 1024], [], []], 'dtype': 'float32,int32,string', 'class': 'frames_npy_preprocess.Preprocess', 'extra_args': {'max_frames': 300, 'feat_dim': 1024, 'return_frames_num': True, 'return_idx': True}}, {'name': 'audio,audio_frames_num', 'shape': [[300, 128], []], 'dtype': 'float32,int32', 'class': 'frames_npy_preprocess.Preprocess', 'extra_args': {'max_frames': 300, 'feat_dim': 128, 'return_frames_num': True}}, {'name': 'image', 'shape': [[224, 224, 3]], 'dtype': 'float32', 'class': 'image_preprocess.Preprocess'}, {'name': 'text', 'shape': [[128]], 'dtype': 'int64', 'class': 'text_preprocess.Preprocess', 'extra_args': {'vocab': 'pretrained/bert/chinese_L-12_H-768_A-12/vocab.txt', 'max_len': 128}}], 'label': [{'name': 'tagging', 'dtype': 'float32', 'shape': [[267]], 'class': 'label_preprocess.Preprocess_label_sparse_to_dense', 'extra_args': {'index_dict': '/home/tione/notebook/tagging-dataset/dict/tag-id-tagging.txt'}}]}}}
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/utils/base_trainer.py:403: The name tf.logging.set_verbosity is deprecated. Please use tf.compat.v1.logging.set_verbosity instead.
    
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/utils/base_trainer.py:403: The name tf.logging.INFO is deprecated. Please use tf.compat.v1.logging.INFO instead.
    
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/utils/base_trainer.py:404: The name tf.logging.info is deprecated. Please use tf.compat.v1.logging.info instead.
    
    INFO:tensorflow:/job:master/task:0: Tensorflow version: 1.14.0.
    6
    Train Source sample_count:  train799 720
    Train Source batch_num:  train799 22
    Valid Source:  val799 79
    Valid Source batch_num:  val799 2
    WARNING:tensorflow:From src/dataloader/preprocess/frames_npy_preprocess.py:57: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.
    
    WARNING:tensorflow:From src/dataloader/preprocess/frames_npy_preprocess.py:60: The name tf.ConfigProto is deprecated. Please use tf.compat.v1.ConfigProto instead.
    
    WARNING:tensorflow:From src/dataloader/preprocess/frames_npy_preprocess.py:62: The name tf.Session is deprecated. Please use tf.compat.v1.Session instead.
    
    WARNING:tensorflow:From src/dataloader/preprocess/cnn_preprocessing/inception_preprocessing.py:148: sample_distorted_bounding_box (from tensorflow.python.ops.image_ops_impl) is deprecated and will be removed in a future version.
    Instructions for updating:
    `seed2` arg is deprecated.Use sample_distorted_bounding_box_v2 instead.
    WARNING:tensorflow:From src/dataloader/preprocess/cnn_preprocessing/inception_preprocessing.py:38: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.
    
    WARNING:tensorflow:From src/dataloader/preprocess/cnn_preprocessing/inception_preprocessing.py:228: The name tf.image.resize_images is deprecated. Please use tf.image.resize instead.
    
    WARNING:tensorflow:From src/dataloader/preprocess/tokenization.py:125: The name tf.gfile.GFile is deprecated. Please use tf.io.gfile.GFile instead.
    
    WARNING:tensorflow:From src/dataloader/preprocess/cnn_preprocessing/inception_preprocessing.py:292: The name tf.image.resize_bilinear is deprecated. Please use tf.compat.v1.image.resize_bilinear instead.
    
    WARNING:tensorflow:From /opt/conda/envs/taac2021/lib/python3.7/site-packages/tensorflow/python/data/ops/dataset_ops.py:494: py_func (from tensorflow.python.ops.script_ops) is deprecated and will be removed in a future version.
    Instructions for updating:
    tf.py_func is deprecated in TF V2. Instead, there are two
        options available in V2.
        - tf.py_function takes a python function which manipulates tf eager
        tensors instead of numpy arrays. It's easy to convert a tf eager tensor to
        an ndarray (just call tensor.numpy()) but having access to eager tensors
        means `tf.py_function`s can use accelerators such as GPUs as well as
        being differentiable using a gradient tape.
        - tf.numpy_function maintains the semantics of the deprecated tf.py_func
        (it is not differentiable, and manipulates numpy arrays). It drops the
        stateful argument making all functions stateful.
        
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/src/dataloader/dataloader.py:35: DatasetV1.make_initializable_iterator (from tensorflow.python.data.ops.dataset_ops) is deprecated and will be removed in a future version.
    Instructions for updating:
    Use `for ... in dataset:` to iterate over a dataset. If using `tf.estimator`, return the `Dataset` object directly from your input function. As a last resort, you can use `tf.compat.v1.data.make_initializable_iterator(dataset)`.
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/src/model/video_head/nextvlad.py:45: calling reduce_sum_v1 (from tensorflow.python.ops.math_ops) with keep_dims is deprecated and will be removed in a future version.
    Instructions for updating:
    keep_dims is deprecated, use keepdims instead
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/src/model/text_head/bert_base.py:354: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
    Instructions for updating:
    Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/src/model/text_head/bert_base.py:667: dense (from tensorflow.python.layers.core) is deprecated and will be removed in a future version.
    Instructions for updating:
    Use keras.layers.dense instead.
    WARNING:tensorflow:From /opt/conda/envs/taac2021/lib/python3.7/site-packages/tensorflow/python/ops/init_ops.py:1251: calling VarianceScaling.__init__ (from tensorflow.python.ops.init_ops) with dtype is deprecated and will be removed in a future version.
    Instructions for updating:
    Call initializer instance with the dtype argument instead of passing it to the constructor
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/src/model/text_head/bert_model.py:19: batch_normalization (from tensorflow.python.layers.normalization) is deprecated and will be removed in a future version.
    Instructions for updating:
    Use keras.layers.BatchNormalization instead.  In particular, `tf.control_dependencies(tf.GraphKeys.UPDATE_OPS)` should not be used (consult the `tf.keras.layers.batch_normalization` documentation).
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/utils/export_model.py:81: build_tensor_info (from tensorflow.python.saved_model.utils_impl) is deprecated and will be removed in a future version.
    Instructions for updating:
    This function will only be available through the v1 compatibility library as tf.compat.v1.saved_model.utils.build_tensor_info or tf.compat.v1.saved_model.build_tensor_info.
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/utils/export_model.py:35: The name tf.train.Saver is deprecated. Please use tf.compat.v1.train.Saver instead.
    
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! modal_name_list: ['video', 'audio', 'text', 'image']
    INFO:tensorflow:/job:master/task:0: Removing existing train directory.
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/utils/base_trainer.py:359: The name tf.gfile.DeleteRecursively is deprecated. Please use tf.io.gfile.rmtree instead.
    
    INFO:tensorflow:No GPUs found. Training on CPU.
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/utils/train_util.py:21: The name tf.train.AdamOptimizer is deprecated. Please use tf.compat.v1.train.AdamOptimizer instead.
    
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/utils/base_trainer.py:97: The name tf.train.exponential_decay is deprecated. Please use tf.compat.v1.train.exponential_decay instead.
    
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/utils/base_trainer.py:102: The name tf.summary.scalar is deprecated. Please use tf.compat.v1.summary.scalar instead.
    
    WARNING:tensorflow:Large dropout rate: 0.8 (>0.5). In TensorFlow 2.x, dropout() uses dropout rate instead of keep_prob. Please ensure that this is intended.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/src/model/models/nextvlad_bert.py:98: The name tf.summary.histogram is deprecated. Please use tf.compat.v1.summary.histogram instead.
    
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    WARNING:tensorflow:Large dropout rate: 0.8 (>0.5). In TensorFlow 2.x, dropout() uses dropout rate instead of keep_prob. Please ensure that this is intended.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    WARNING:tensorflow:From /opt/conda/envs/taac2021/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
    Instructions for updating:
    Use tf.where in 2.0, which has the same broadcast rule as np.where
    tower/video/fully_connected/weights:0
    tower/video/fully_connected/biases:0
    tower/video/fully_connected_1/weights:0
    tower/video/fully_connected_1/biases:0
    tower/video/cluster_weights:0
    tower/video/cluster_bn/gamma:0
    tower/video/cluster_bn/beta:0
    tower/video/cluster_weights2:0
    tower/video/vlad_bn/gamma:0
    tower/video/vlad_bn/beta:0
    tower/tag_classifier/v/hidden1_weights:0
    tower/tag_classifier/v/hidden1_bn/gamma:0
    tower/tag_classifier/v/hidden1_bn/beta:0
    tower/tag_classifier/v/gating_weights_1:0
    tower/tag_classifier/v/gating_bn/beta:0
    tower/tag_classifier/v/gating_bn/gamma:0
    tower/tag_classifier/v/gating_weights_2:0
    tower/tag_classifier/v/fully_connected/weights:0
    tower/tag_classifier/v/fully_connected/biases:0
    tower/audio/fully_connected/weights:0
    tower/audio/fully_connected/biases:0
    tower/audio/fully_connected_1/weights:0
    tower/audio/fully_connected_1/biases:0
    tower/audio/cluster_weights:0
    tower/audio/cluster_bn/gamma:0
    tower/audio/cluster_bn/beta:0
    tower/audio/cluster_weights2:0
    tower/audio/vlad_bn/gamma:0
    tower/audio/vlad_bn/beta:0
    tower/tag_classifier/a/hidden1_weights:0
    tower/tag_classifier/a/hidden1_bn/gamma:0
    tower/tag_classifier/a/hidden1_bn/beta:0
    tower/tag_classifier/a/gating_weights_1:0
    tower/tag_classifier/a/gating_bn/beta:0
    tower/tag_classifier/a/gating_bn/gamma:0
    tower/tag_classifier/a/gating_weights_2:0
    tower/tag_classifier/a/fully_connected/weights:0
    tower/tag_classifier/a/fully_connected/biases:0
    tower/text/bert/embeddings/word_embeddings:0
    tower/text/bert/embeddings/token_type_embeddings:0
    tower/text/bert/embeddings/position_embeddings:0
    tower/text/bert/embeddings/LayerNorm/beta:0
    tower/text/bert/embeddings/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_0/attention/self/query/kernel:0
    tower/text/bert/encoder/layer_0/attention/self/query/bias:0
    tower/text/bert/encoder/layer_0/attention/self/key/kernel:0
    tower/text/bert/encoder/layer_0/attention/self/key/bias:0
    tower/text/bert/encoder/layer_0/attention/self/value/kernel:0
    tower/text/bert/encoder/layer_0/attention/self/value/bias:0
    tower/text/bert/encoder/layer_0/attention/output/dense/kernel:0
    tower/text/bert/encoder/layer_0/attention/output/dense/bias:0
    tower/text/bert/encoder/layer_0/attention/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_0/attention/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_0/intermediate/dense/kernel:0
    tower/text/bert/encoder/layer_0/intermediate/dense/bias:0
    tower/text/bert/encoder/layer_0/output/dense/kernel:0
    tower/text/bert/encoder/layer_0/output/dense/bias:0
    tower/text/bert/encoder/layer_0/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_0/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_1/attention/self/query/kernel:0
    tower/text/bert/encoder/layer_1/attention/self/query/bias:0
    tower/text/bert/encoder/layer_1/attention/self/key/kernel:0
    tower/text/bert/encoder/layer_1/attention/self/key/bias:0
    tower/text/bert/encoder/layer_1/attention/self/value/kernel:0
    tower/text/bert/encoder/layer_1/attention/self/value/bias:0
    tower/text/bert/encoder/layer_1/attention/output/dense/kernel:0
    tower/text/bert/encoder/layer_1/attention/output/dense/bias:0
    tower/text/bert/encoder/layer_1/attention/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_1/attention/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_1/intermediate/dense/kernel:0
    tower/text/bert/encoder/layer_1/intermediate/dense/bias:0
    tower/text/bert/encoder/layer_1/output/dense/kernel:0
    tower/text/bert/encoder/layer_1/output/dense/bias:0
    tower/text/bert/encoder/layer_1/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_1/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_2/attention/self/query/kernel:0
    tower/text/bert/encoder/layer_2/attention/self/query/bias:0
    tower/text/bert/encoder/layer_2/attention/self/key/kernel:0
    tower/text/bert/encoder/layer_2/attention/self/key/bias:0
    tower/text/bert/encoder/layer_2/attention/self/value/kernel:0
    tower/text/bert/encoder/layer_2/attention/self/value/bias:0
    tower/text/bert/encoder/layer_2/attention/output/dense/kernel:0
    tower/text/bert/encoder/layer_2/attention/output/dense/bias:0
    tower/text/bert/encoder/layer_2/attention/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_2/attention/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_2/intermediate/dense/kernel:0
    tower/text/bert/encoder/layer_2/intermediate/dense/bias:0
    tower/text/bert/encoder/layer_2/output/dense/kernel:0
    tower/text/bert/encoder/layer_2/output/dense/bias:0
    tower/text/bert/encoder/layer_2/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_2/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_3/attention/self/query/kernel:0
    tower/text/bert/encoder/layer_3/attention/self/query/bias:0
    tower/text/bert/encoder/layer_3/attention/self/key/kernel:0
    tower/text/bert/encoder/layer_3/attention/self/key/bias:0
    tower/text/bert/encoder/layer_3/attention/self/value/kernel:0
    tower/text/bert/encoder/layer_3/attention/self/value/bias:0
    tower/text/bert/encoder/layer_3/attention/output/dense/kernel:0
    tower/text/bert/encoder/layer_3/attention/output/dense/bias:0
    tower/text/bert/encoder/layer_3/attention/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_3/attention/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_3/intermediate/dense/kernel:0
    tower/text/bert/encoder/layer_3/intermediate/dense/bias:0
    tower/text/bert/encoder/layer_3/output/dense/kernel:0
    tower/text/bert/encoder/layer_3/output/dense/bias:0
    tower/text/bert/encoder/layer_3/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_3/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_4/attention/self/query/kernel:0
    tower/text/bert/encoder/layer_4/attention/self/query/bias:0
    tower/text/bert/encoder/layer_4/attention/self/key/kernel:0
    tower/text/bert/encoder/layer_4/attention/self/key/bias:0
    tower/text/bert/encoder/layer_4/attention/self/value/kernel:0
    tower/text/bert/encoder/layer_4/attention/self/value/bias:0
    tower/text/bert/encoder/layer_4/attention/output/dense/kernel:0
    tower/text/bert/encoder/layer_4/attention/output/dense/bias:0
    tower/text/bert/encoder/layer_4/attention/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_4/attention/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_4/intermediate/dense/kernel:0
    tower/text/bert/encoder/layer_4/intermediate/dense/bias:0
    tower/text/bert/encoder/layer_4/output/dense/kernel:0
    tower/text/bert/encoder/layer_4/output/dense/bias:0
    tower/text/bert/encoder/layer_4/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_4/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_5/attention/self/query/kernel:0
    tower/text/bert/encoder/layer_5/attention/self/query/bias:0
    tower/text/bert/encoder/layer_5/attention/self/key/kernel:0
    tower/text/bert/encoder/layer_5/attention/self/key/bias:0
    tower/text/bert/encoder/layer_5/attention/self/value/kernel:0
    tower/text/bert/encoder/layer_5/attention/self/value/bias:0
    tower/text/bert/encoder/layer_5/attention/output/dense/kernel:0
    tower/text/bert/encoder/layer_5/attention/output/dense/bias:0
    tower/text/bert/encoder/layer_5/attention/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_5/attention/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_5/intermediate/dense/kernel:0
    tower/text/bert/encoder/layer_5/intermediate/dense/bias:0
    tower/text/bert/encoder/layer_5/output/dense/kernel:0
    tower/text/bert/encoder/layer_5/output/dense/bias:0
    tower/text/bert/encoder/layer_5/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_5/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_6/attention/self/query/kernel:0
    tower/text/bert/encoder/layer_6/attention/self/query/bias:0
    tower/text/bert/encoder/layer_6/attention/self/key/kernel:0
    tower/text/bert/encoder/layer_6/attention/self/key/bias:0
    tower/text/bert/encoder/layer_6/attention/self/value/kernel:0
    tower/text/bert/encoder/layer_6/attention/self/value/bias:0
    tower/text/bert/encoder/layer_6/attention/output/dense/kernel:0
    tower/text/bert/encoder/layer_6/attention/output/dense/bias:0
    tower/text/bert/encoder/layer_6/attention/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_6/attention/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_6/intermediate/dense/kernel:0
    tower/text/bert/encoder/layer_6/intermediate/dense/bias:0
    tower/text/bert/encoder/layer_6/output/dense/kernel:0
    tower/text/bert/encoder/layer_6/output/dense/bias:0
    tower/text/bert/encoder/layer_6/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_6/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_7/attention/self/query/kernel:0
    tower/text/bert/encoder/layer_7/attention/self/query/bias:0
    tower/text/bert/encoder/layer_7/attention/self/key/kernel:0
    tower/text/bert/encoder/layer_7/attention/self/key/bias:0
    tower/text/bert/encoder/layer_7/attention/self/value/kernel:0
    tower/text/bert/encoder/layer_7/attention/self/value/bias:0
    tower/text/bert/encoder/layer_7/attention/output/dense/kernel:0
    tower/text/bert/encoder/layer_7/attention/output/dense/bias:0
    tower/text/bert/encoder/layer_7/attention/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_7/attention/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_7/intermediate/dense/kernel:0
    tower/text/bert/encoder/layer_7/intermediate/dense/bias:0
    tower/text/bert/encoder/layer_7/output/dense/kernel:0
    tower/text/bert/encoder/layer_7/output/dense/bias:0
    tower/text/bert/encoder/layer_7/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_7/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_8/attention/self/query/kernel:0
    tower/text/bert/encoder/layer_8/attention/self/query/bias:0
    tower/text/bert/encoder/layer_8/attention/self/key/kernel:0
    tower/text/bert/encoder/layer_8/attention/self/key/bias:0
    tower/text/bert/encoder/layer_8/attention/self/value/kernel:0
    tower/text/bert/encoder/layer_8/attention/self/value/bias:0
    tower/text/bert/encoder/layer_8/attention/output/dense/kernel:0
    tower/text/bert/encoder/layer_8/attention/output/dense/bias:0
    tower/text/bert/encoder/layer_8/attention/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_8/attention/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_8/intermediate/dense/kernel:0
    tower/text/bert/encoder/layer_8/intermediate/dense/bias:0
    tower/text/bert/encoder/layer_8/output/dense/kernel:0
    tower/text/bert/encoder/layer_8/output/dense/bias:0
    tower/text/bert/encoder/layer_8/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_8/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_9/attention/self/query/kernel:0
    tower/text/bert/encoder/layer_9/attention/self/query/bias:0
    tower/text/bert/encoder/layer_9/attention/self/key/kernel:0
    tower/text/bert/encoder/layer_9/attention/self/key/bias:0
    tower/text/bert/encoder/layer_9/attention/self/value/kernel:0
    tower/text/bert/encoder/layer_9/attention/self/value/bias:0
    tower/text/bert/encoder/layer_9/attention/output/dense/kernel:0
    tower/text/bert/encoder/layer_9/attention/output/dense/bias:0
    tower/text/bert/encoder/layer_9/attention/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_9/attention/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_9/intermediate/dense/kernel:0
    tower/text/bert/encoder/layer_9/intermediate/dense/bias:0
    tower/text/bert/encoder/layer_9/output/dense/kernel:0
    tower/text/bert/encoder/layer_9/output/dense/bias:0
    tower/text/bert/encoder/layer_9/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_9/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_10/attention/self/query/kernel:0
    tower/text/bert/encoder/layer_10/attention/self/query/bias:0
    tower/text/bert/encoder/layer_10/attention/self/key/kernel:0
    tower/text/bert/encoder/layer_10/attention/self/key/bias:0
    tower/text/bert/encoder/layer_10/attention/self/value/kernel:0
    tower/text/bert/encoder/layer_10/attention/self/value/bias:0
    tower/text/bert/encoder/layer_10/attention/output/dense/kernel:0
    tower/text/bert/encoder/layer_10/attention/output/dense/bias:0
    tower/text/bert/encoder/layer_10/attention/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_10/attention/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_10/intermediate/dense/kernel:0
    tower/text/bert/encoder/layer_10/intermediate/dense/bias:0
    tower/text/bert/encoder/layer_10/output/dense/kernel:0
    tower/text/bert/encoder/layer_10/output/dense/bias:0
    tower/text/bert/encoder/layer_10/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_10/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_11/attention/self/query/kernel:0
    tower/text/bert/encoder/layer_11/attention/self/query/bias:0
    tower/text/bert/encoder/layer_11/attention/self/key/kernel:0
    tower/text/bert/encoder/layer_11/attention/self/key/bias:0
    tower/text/bert/encoder/layer_11/attention/self/value/kernel:0
    tower/text/bert/encoder/layer_11/attention/self/value/bias:0
    tower/text/bert/encoder/layer_11/attention/output/dense/kernel:0
    tower/text/bert/encoder/layer_11/attention/output/dense/bias:0
    tower/text/bert/encoder/layer_11/attention/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_11/attention/output/LayerNorm/gamma:0
    tower/text/bert/encoder/layer_11/intermediate/dense/kernel:0
    tower/text/bert/encoder/layer_11/intermediate/dense/bias:0
    tower/text/bert/encoder/layer_11/output/dense/kernel:0
    tower/text/bert/encoder/layer_11/output/dense/bias:0
    tower/text/bert/encoder/layer_11/output/LayerNorm/beta:0
    tower/text/bert/encoder/layer_11/output/LayerNorm/gamma:0
    tower/text/bert/pooler/dense/kernel:0
    tower/text/bert/pooler/dense/bias:0
    tower/text/text_features/kernel:0
    tower/text/text_features/bias:0
    tower/text/batch_normalization/gamma:0
    tower/text/batch_normalization/beta:0
    tower/tag_classifier/t/hidden1_weights:0
    tower/tag_classifier/t/hidden1_bn/gamma:0
    tower/tag_classifier/t/hidden1_bn/beta:0
    tower/tag_classifier/t/gating_weights_1:0
    tower/tag_classifier/t/gating_bn/beta:0
    tower/tag_classifier/t/gating_bn/gamma:0
    tower/tag_classifier/t/gating_weights_2:0
    tower/tag_classifier/t/fully_connected/weights:0
    tower/tag_classifier/t/fully_connected/biases:0
    tower/image/resnet_v2_50/conv1/weights:0
    tower/image/resnet_v2_50/conv1/biases:0
    tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/preact/gamma:0
    tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/preact/beta:0
    tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/shortcut/weights:0
    tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/shortcut/biases:0
    tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/weights:0
    tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/BatchNorm/beta:0
    tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/weights:0
    tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/BatchNorm/beta:0
    tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv3/weights:0
    tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv3/biases:0
    tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/preact/gamma:0
    tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/preact/beta:0
    tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/weights:0
    tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/BatchNorm/beta:0
    tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/weights:0
    tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/BatchNorm/beta:0
    tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv3/weights:0
    tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv3/biases:0
    tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/preact/gamma:0
    tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/preact/beta:0
    tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/weights:0
    tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/BatchNorm/beta:0
    tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/weights:0
    tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/BatchNorm/beta:0
    tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv3/weights:0
    tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv3/biases:0
    tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/preact/gamma:0
    tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/preact/beta:0
    tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/shortcut/weights:0
    tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/shortcut/biases:0
    tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/weights:0
    tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/BatchNorm/beta:0
    tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/weights:0
    tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/BatchNorm/beta:0
    tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv3/weights:0
    tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv3/biases:0
    tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/preact/gamma:0
    tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/preact/beta:0
    tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/weights:0
    tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/BatchNorm/beta:0
    tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/weights:0
    tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/BatchNorm/beta:0
    tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv3/weights:0
    tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv3/biases:0
    tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/preact/gamma:0
    tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/preact/beta:0
    tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/weights:0
    tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/BatchNorm/beta:0
    tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/weights:0
    tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/BatchNorm/beta:0
    tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv3/weights:0
    tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv3/biases:0
    tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/preact/gamma:0
    tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/preact/beta:0
    tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/weights:0
    tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/BatchNorm/beta:0
    tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/weights:0
    tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/BatchNorm/beta:0
    tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv3/weights:0
    tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv3/biases:0
    tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/preact/gamma:0
    tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/preact/beta:0
    tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/shortcut/weights:0
    tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/shortcut/biases:0
    tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/weights:0
    tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/BatchNorm/beta:0
    tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/weights:0
    tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/BatchNorm/beta:0
    tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv3/weights:0
    tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv3/biases:0
    tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/preact/gamma:0
    tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/preact/beta:0
    tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/weights:0
    tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/BatchNorm/beta:0
    tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/weights:0
    tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/BatchNorm/beta:0
    tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv3/weights:0
    tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv3/biases:0
    tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/preact/gamma:0
    tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/preact/beta:0
    tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/weights:0
    tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/BatchNorm/beta:0
    tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/weights:0
    tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/BatchNorm/beta:0
    tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv3/weights:0
    tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv3/biases:0
    tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/preact/gamma:0
    tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/preact/beta:0
    tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/weights:0
    tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/BatchNorm/beta:0
    tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/weights:0
    tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/BatchNorm/beta:0
    tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv3/weights:0
    tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv3/biases:0
    tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/preact/gamma:0
    tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/preact/beta:0
    tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/weights:0
    tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/BatchNorm/beta:0
    tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/weights:0
    tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/BatchNorm/beta:0
    tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv3/weights:0
    tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv3/biases:0
    tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/preact/gamma:0
    tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/preact/beta:0
    tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/weights:0
    tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/BatchNorm/beta:0
    tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/weights:0
    tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/BatchNorm/beta:0
    tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv3/weights:0
    tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv3/biases:0
    tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/preact/gamma:0
    tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/preact/beta:0
    tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/shortcut/weights:0
    tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/shortcut/biases:0
    tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/weights:0
    tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/BatchNorm/beta:0
    tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/weights:0
    tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/BatchNorm/beta:0
    tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv3/weights:0
    tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv3/biases:0
    tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/preact/gamma:0
    tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/preact/beta:0
    tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/weights:0
    tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/BatchNorm/beta:0
    tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/weights:0
    tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/BatchNorm/beta:0
    tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv3/weights:0
    tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv3/biases:0
    tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/preact/gamma:0
    tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/preact/beta:0
    tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/weights:0
    tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/BatchNorm/beta:0
    tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/weights:0
    tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/BatchNorm/gamma:0
    tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/BatchNorm/beta:0
    tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv3/weights:0
    tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv3/biases:0
    tower/image/resnet_v2_50/postnorm/gamma:0
    tower/image/resnet_v2_50/postnorm/beta:0
    tower/tag_classifier/i/hidden1_weights:0
    tower/tag_classifier/i/hidden1_bn/gamma:0
    tower/tag_classifier/i/hidden1_bn/beta:0
    tower/tag_classifier/i/gating_weights_1:0
    tower/tag_classifier/i/gating_bn/beta:0
    tower/tag_classifier/i/gating_bn/gamma:0
    tower/tag_classifier/i/gating_weights_2:0
    tower/tag_classifier/i/fully_connected/weights:0
    tower/tag_classifier/i/fully_connected/biases:0
    tower/tag_classifier/fusion/hidden1_weights:0
    tower/tag_classifier/fusion/hidden1_bn/gamma:0
    tower/tag_classifier/fusion/hidden1_bn/beta:0
    tower/tag_classifier/fusion/gating_weights_1:0
    tower/tag_classifier/fusion/gating_bn/beta:0
    tower/tag_classifier/fusion/gating_bn/gamma:0
    tower/tag_classifier/fusion/gating_weights_2:0
    tower/tag_classifier/fusion/fully_connected/weights:0
    tower/tag_classifier/fusion/fully_connected/biases:0
    INFO:tensorflow:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    INFO:tensorflow:video vars size: 10|audio vars size: 10|text vars size: 203|image vars size: 172|classifier vars size: 45
    input_name: video, input_shape:[300, 1024], input_dtype: <dtype: 'float32'>
    input_name: video_frames_num, input_shape:[], input_dtype: <dtype: 'int32'>
    input_name: idx, input_shape:[], input_dtype: <dtype: 'string'>
    input_name: audio, input_shape:[300, 128], input_dtype: <dtype: 'float32'>
    input_name: audio_frames_num, input_shape:[], input_dtype: <dtype: 'int32'>
    input_name: image, input_shape:[224, 224, 3], input_dtype: <dtype: 'float32'>
    input_name: text, input_shape:[128], input_dtype: <dtype: 'int64'>
    input_name: tagging, input_shape:[267], input_dtype: <dtype: 'float32'>
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    INFO:tensorflow:Scale of 0 disables regularizer.
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/utils/base_trainer.py:237: The name tf.summary.merge_all is deprecated. Please use tf.compat.v1.summary.merge_all instead.
    
    assign:  bert/embeddings/LayerNorm/beta tower/text/bert/embeddings/LayerNorm/beta
    assign:  bert/embeddings/LayerNorm/gamma tower/text/bert/embeddings/LayerNorm/gamma
    assign:  bert/embeddings/position_embeddings tower/text/bert/embeddings/position_embeddings
    assign:  bert/embeddings/token_type_embeddings tower/text/bert/embeddings/token_type_embeddings
    assign:  bert/embeddings/word_embeddings tower/text/bert/embeddings/word_embeddings
    assign:  bert/encoder/layer_0/attention/output/LayerNorm/beta tower/text/bert/encoder/layer_0/attention/output/LayerNorm/beta
    assign:  bert/encoder/layer_0/attention/output/LayerNorm/gamma tower/text/bert/encoder/layer_0/attention/output/LayerNorm/gamma
    assign:  bert/encoder/layer_0/attention/output/dense/bias tower/text/bert/encoder/layer_0/attention/output/dense/bias
    assign:  bert/encoder/layer_0/attention/output/dense/kernel tower/text/bert/encoder/layer_0/attention/output/dense/kernel
    assign:  bert/encoder/layer_0/attention/self/key/bias tower/text/bert/encoder/layer_0/attention/self/key/bias
    assign:  bert/encoder/layer_0/attention/self/key/kernel tower/text/bert/encoder/layer_0/attention/self/key/kernel
    assign:  bert/encoder/layer_0/attention/self/query/bias tower/text/bert/encoder/layer_0/attention/self/query/bias
    assign:  bert/encoder/layer_0/attention/self/query/kernel tower/text/bert/encoder/layer_0/attention/self/query/kernel
    assign:  bert/encoder/layer_0/attention/self/value/bias tower/text/bert/encoder/layer_0/attention/self/value/bias
    assign:  bert/encoder/layer_0/attention/self/value/kernel tower/text/bert/encoder/layer_0/attention/self/value/kernel
    assign:  bert/encoder/layer_0/intermediate/dense/bias tower/text/bert/encoder/layer_0/intermediate/dense/bias
    assign:  bert/encoder/layer_0/intermediate/dense/kernel tower/text/bert/encoder/layer_0/intermediate/dense/kernel
    assign:  bert/encoder/layer_0/output/LayerNorm/beta tower/text/bert/encoder/layer_0/output/LayerNorm/beta
    assign:  bert/encoder/layer_0/output/LayerNorm/gamma tower/text/bert/encoder/layer_0/output/LayerNorm/gamma
    assign:  bert/encoder/layer_0/output/dense/bias tower/text/bert/encoder/layer_0/output/dense/bias
    assign:  bert/encoder/layer_0/output/dense/kernel tower/text/bert/encoder/layer_0/output/dense/kernel
    assign:  bert/encoder/layer_1/attention/output/LayerNorm/beta tower/text/bert/encoder/layer_1/attention/output/LayerNorm/beta
    assign:  bert/encoder/layer_1/attention/output/LayerNorm/gamma tower/text/bert/encoder/layer_1/attention/output/LayerNorm/gamma
    assign:  bert/encoder/layer_1/attention/output/dense/bias tower/text/bert/encoder/layer_1/attention/output/dense/bias
    assign:  bert/encoder/layer_1/attention/output/dense/kernel tower/text/bert/encoder/layer_1/attention/output/dense/kernel
    assign:  bert/encoder/layer_1/attention/self/key/bias tower/text/bert/encoder/layer_1/attention/self/key/bias
    assign:  bert/encoder/layer_1/attention/self/key/kernel tower/text/bert/encoder/layer_1/attention/self/key/kernel
    assign:  bert/encoder/layer_1/attention/self/query/bias tower/text/bert/encoder/layer_1/attention/self/query/bias
    assign:  bert/encoder/layer_1/attention/self/query/kernel tower/text/bert/encoder/layer_1/attention/self/query/kernel
    assign:  bert/encoder/layer_1/attention/self/value/bias tower/text/bert/encoder/layer_1/attention/self/value/bias
    assign:  bert/encoder/layer_1/attention/self/value/kernel tower/text/bert/encoder/layer_1/attention/self/value/kernel
    assign:  bert/encoder/layer_1/intermediate/dense/bias tower/text/bert/encoder/layer_1/intermediate/dense/bias
    assign:  bert/encoder/layer_1/intermediate/dense/kernel tower/text/bert/encoder/layer_1/intermediate/dense/kernel
    assign:  bert/encoder/layer_1/output/LayerNorm/beta tower/text/bert/encoder/layer_1/output/LayerNorm/beta
    assign:  bert/encoder/layer_1/output/LayerNorm/gamma tower/text/bert/encoder/layer_1/output/LayerNorm/gamma
    assign:  bert/encoder/layer_1/output/dense/bias tower/text/bert/encoder/layer_1/output/dense/bias
    assign:  bert/encoder/layer_1/output/dense/kernel tower/text/bert/encoder/layer_1/output/dense/kernel
    assign:  bert/encoder/layer_10/attention/output/LayerNorm/beta tower/text/bert/encoder/layer_10/attention/output/LayerNorm/beta
    assign:  bert/encoder/layer_10/attention/output/LayerNorm/gamma tower/text/bert/encoder/layer_10/attention/output/LayerNorm/gamma
    assign:  bert/encoder/layer_10/attention/output/dense/bias tower/text/bert/encoder/layer_10/attention/output/dense/bias
    assign:  bert/encoder/layer_10/attention/output/dense/kernel tower/text/bert/encoder/layer_10/attention/output/dense/kernel
    assign:  bert/encoder/layer_10/attention/self/key/bias tower/text/bert/encoder/layer_10/attention/self/key/bias
    assign:  bert/encoder/layer_10/attention/self/key/kernel tower/text/bert/encoder/layer_10/attention/self/key/kernel
    assign:  bert/encoder/layer_10/attention/self/query/bias tower/text/bert/encoder/layer_10/attention/self/query/bias
    assign:  bert/encoder/layer_10/attention/self/query/kernel tower/text/bert/encoder/layer_10/attention/self/query/kernel
    assign:  bert/encoder/layer_10/attention/self/value/bias tower/text/bert/encoder/layer_10/attention/self/value/bias
    assign:  bert/encoder/layer_10/attention/self/value/kernel tower/text/bert/encoder/layer_10/attention/self/value/kernel
    assign:  bert/encoder/layer_10/intermediate/dense/bias tower/text/bert/encoder/layer_10/intermediate/dense/bias
    assign:  bert/encoder/layer_10/intermediate/dense/kernel tower/text/bert/encoder/layer_10/intermediate/dense/kernel
    assign:  bert/encoder/layer_10/output/LayerNorm/beta tower/text/bert/encoder/layer_10/output/LayerNorm/beta
    assign:  bert/encoder/layer_10/output/LayerNorm/gamma tower/text/bert/encoder/layer_10/output/LayerNorm/gamma
    assign:  bert/encoder/layer_10/output/dense/bias tower/text/bert/encoder/layer_10/output/dense/bias
    assign:  bert/encoder/layer_10/output/dense/kernel tower/text/bert/encoder/layer_10/output/dense/kernel
    assign:  bert/encoder/layer_11/attention/output/LayerNorm/beta tower/text/bert/encoder/layer_11/attention/output/LayerNorm/beta
    assign:  bert/encoder/layer_11/attention/output/LayerNorm/gamma tower/text/bert/encoder/layer_11/attention/output/LayerNorm/gamma
    assign:  bert/encoder/layer_11/attention/output/dense/bias tower/text/bert/encoder/layer_11/attention/output/dense/bias
    assign:  bert/encoder/layer_11/attention/output/dense/kernel tower/text/bert/encoder/layer_11/attention/output/dense/kernel
    assign:  bert/encoder/layer_11/attention/self/key/bias tower/text/bert/encoder/layer_11/attention/self/key/bias
    assign:  bert/encoder/layer_11/attention/self/key/kernel tower/text/bert/encoder/layer_11/attention/self/key/kernel
    assign:  bert/encoder/layer_11/attention/self/query/bias tower/text/bert/encoder/layer_11/attention/self/query/bias
    assign:  bert/encoder/layer_11/attention/self/query/kernel tower/text/bert/encoder/layer_11/attention/self/query/kernel
    assign:  bert/encoder/layer_11/attention/self/value/bias tower/text/bert/encoder/layer_11/attention/self/value/bias
    assign:  bert/encoder/layer_11/attention/self/value/kernel tower/text/bert/encoder/layer_11/attention/self/value/kernel
    assign:  bert/encoder/layer_11/intermediate/dense/bias tower/text/bert/encoder/layer_11/intermediate/dense/bias
    assign:  bert/encoder/layer_11/intermediate/dense/kernel tower/text/bert/encoder/layer_11/intermediate/dense/kernel
    assign:  bert/encoder/layer_11/output/LayerNorm/beta tower/text/bert/encoder/layer_11/output/LayerNorm/beta
    assign:  bert/encoder/layer_11/output/LayerNorm/gamma tower/text/bert/encoder/layer_11/output/LayerNorm/gamma
    assign:  bert/encoder/layer_11/output/dense/bias tower/text/bert/encoder/layer_11/output/dense/bias
    assign:  bert/encoder/layer_11/output/dense/kernel tower/text/bert/encoder/layer_11/output/dense/kernel
    assign:  bert/encoder/layer_2/attention/output/LayerNorm/beta tower/text/bert/encoder/layer_2/attention/output/LayerNorm/beta
    assign:  bert/encoder/layer_2/attention/output/LayerNorm/gamma tower/text/bert/encoder/layer_2/attention/output/LayerNorm/gamma
    assign:  bert/encoder/layer_2/attention/output/dense/bias tower/text/bert/encoder/layer_2/attention/output/dense/bias
    assign:  bert/encoder/layer_2/attention/output/dense/kernel tower/text/bert/encoder/layer_2/attention/output/dense/kernel
    assign:  bert/encoder/layer_2/attention/self/key/bias tower/text/bert/encoder/layer_2/attention/self/key/bias
    assign:  bert/encoder/layer_2/attention/self/key/kernel tower/text/bert/encoder/layer_2/attention/self/key/kernel
    assign:  bert/encoder/layer_2/attention/self/query/bias tower/text/bert/encoder/layer_2/attention/self/query/bias
    assign:  bert/encoder/layer_2/attention/self/query/kernel tower/text/bert/encoder/layer_2/attention/self/query/kernel
    assign:  bert/encoder/layer_2/attention/self/value/bias tower/text/bert/encoder/layer_2/attention/self/value/bias
    assign:  bert/encoder/layer_2/attention/self/value/kernel tower/text/bert/encoder/layer_2/attention/self/value/kernel
    assign:  bert/encoder/layer_2/intermediate/dense/bias tower/text/bert/encoder/layer_2/intermediate/dense/bias
    assign:  bert/encoder/layer_2/intermediate/dense/kernel tower/text/bert/encoder/layer_2/intermediate/dense/kernel
    assign:  bert/encoder/layer_2/output/LayerNorm/beta tower/text/bert/encoder/layer_2/output/LayerNorm/beta
    assign:  bert/encoder/layer_2/output/LayerNorm/gamma tower/text/bert/encoder/layer_2/output/LayerNorm/gamma
    assign:  bert/encoder/layer_2/output/dense/bias tower/text/bert/encoder/layer_2/output/dense/bias
    assign:  bert/encoder/layer_2/output/dense/kernel tower/text/bert/encoder/layer_2/output/dense/kernel
    assign:  bert/encoder/layer_3/attention/output/LayerNorm/beta tower/text/bert/encoder/layer_3/attention/output/LayerNorm/beta
    assign:  bert/encoder/layer_3/attention/output/LayerNorm/gamma tower/text/bert/encoder/layer_3/attention/output/LayerNorm/gamma
    assign:  bert/encoder/layer_3/attention/output/dense/bias tower/text/bert/encoder/layer_3/attention/output/dense/bias
    assign:  bert/encoder/layer_3/attention/output/dense/kernel tower/text/bert/encoder/layer_3/attention/output/dense/kernel
    assign:  bert/encoder/layer_3/attention/self/key/bias tower/text/bert/encoder/layer_3/attention/self/key/bias
    assign:  bert/encoder/layer_3/attention/self/key/kernel tower/text/bert/encoder/layer_3/attention/self/key/kernel
    assign:  bert/encoder/layer_3/attention/self/query/bias tower/text/bert/encoder/layer_3/attention/self/query/bias
    assign:  bert/encoder/layer_3/attention/self/query/kernel tower/text/bert/encoder/layer_3/attention/self/query/kernel
    assign:  bert/encoder/layer_3/attention/self/value/bias tower/text/bert/encoder/layer_3/attention/self/value/bias
    assign:  bert/encoder/layer_3/attention/self/value/kernel tower/text/bert/encoder/layer_3/attention/self/value/kernel
    assign:  bert/encoder/layer_3/intermediate/dense/bias tower/text/bert/encoder/layer_3/intermediate/dense/bias
    assign:  bert/encoder/layer_3/intermediate/dense/kernel tower/text/bert/encoder/layer_3/intermediate/dense/kernel
    assign:  bert/encoder/layer_3/output/LayerNorm/beta tower/text/bert/encoder/layer_3/output/LayerNorm/beta
    assign:  bert/encoder/layer_3/output/LayerNorm/gamma tower/text/bert/encoder/layer_3/output/LayerNorm/gamma
    assign:  bert/encoder/layer_3/output/dense/bias tower/text/bert/encoder/layer_3/output/dense/bias
    assign:  bert/encoder/layer_3/output/dense/kernel tower/text/bert/encoder/layer_3/output/dense/kernel
    assign:  bert/encoder/layer_4/attention/output/LayerNorm/beta tower/text/bert/encoder/layer_4/attention/output/LayerNorm/beta
    assign:  bert/encoder/layer_4/attention/output/LayerNorm/gamma tower/text/bert/encoder/layer_4/attention/output/LayerNorm/gamma
    assign:  bert/encoder/layer_4/attention/output/dense/bias tower/text/bert/encoder/layer_4/attention/output/dense/bias
    assign:  bert/encoder/layer_4/attention/output/dense/kernel tower/text/bert/encoder/layer_4/attention/output/dense/kernel
    assign:  bert/encoder/layer_4/attention/self/key/bias tower/text/bert/encoder/layer_4/attention/self/key/bias
    assign:  bert/encoder/layer_4/attention/self/key/kernel tower/text/bert/encoder/layer_4/attention/self/key/kernel
    assign:  bert/encoder/layer_4/attention/self/query/bias tower/text/bert/encoder/layer_4/attention/self/query/bias
    assign:  bert/encoder/layer_4/attention/self/query/kernel tower/text/bert/encoder/layer_4/attention/self/query/kernel
    assign:  bert/encoder/layer_4/attention/self/value/bias tower/text/bert/encoder/layer_4/attention/self/value/bias
    assign:  bert/encoder/layer_4/attention/self/value/kernel tower/text/bert/encoder/layer_4/attention/self/value/kernel
    assign:  bert/encoder/layer_4/intermediate/dense/bias tower/text/bert/encoder/layer_4/intermediate/dense/bias
    assign:  bert/encoder/layer_4/intermediate/dense/kernel tower/text/bert/encoder/layer_4/intermediate/dense/kernel
    assign:  bert/encoder/layer_4/output/LayerNorm/beta tower/text/bert/encoder/layer_4/output/LayerNorm/beta
    assign:  bert/encoder/layer_4/output/LayerNorm/gamma tower/text/bert/encoder/layer_4/output/LayerNorm/gamma
    assign:  bert/encoder/layer_4/output/dense/bias tower/text/bert/encoder/layer_4/output/dense/bias
    assign:  bert/encoder/layer_4/output/dense/kernel tower/text/bert/encoder/layer_4/output/dense/kernel
    assign:  bert/encoder/layer_5/attention/output/LayerNorm/beta tower/text/bert/encoder/layer_5/attention/output/LayerNorm/beta
    assign:  bert/encoder/layer_5/attention/output/LayerNorm/gamma tower/text/bert/encoder/layer_5/attention/output/LayerNorm/gamma
    assign:  bert/encoder/layer_5/attention/output/dense/bias tower/text/bert/encoder/layer_5/attention/output/dense/bias
    assign:  bert/encoder/layer_5/attention/output/dense/kernel tower/text/bert/encoder/layer_5/attention/output/dense/kernel
    assign:  bert/encoder/layer_5/attention/self/key/bias tower/text/bert/encoder/layer_5/attention/self/key/bias
    assign:  bert/encoder/layer_5/attention/self/key/kernel tower/text/bert/encoder/layer_5/attention/self/key/kernel
    assign:  bert/encoder/layer_5/attention/self/query/bias tower/text/bert/encoder/layer_5/attention/self/query/bias
    assign:  bert/encoder/layer_5/attention/self/query/kernel tower/text/bert/encoder/layer_5/attention/self/query/kernel
    assign:  bert/encoder/layer_5/attention/self/value/bias tower/text/bert/encoder/layer_5/attention/self/value/bias
    assign:  bert/encoder/layer_5/attention/self/value/kernel tower/text/bert/encoder/layer_5/attention/self/value/kernel
    assign:  bert/encoder/layer_5/intermediate/dense/bias tower/text/bert/encoder/layer_5/intermediate/dense/bias
    assign:  bert/encoder/layer_5/intermediate/dense/kernel tower/text/bert/encoder/layer_5/intermediate/dense/kernel
    assign:  bert/encoder/layer_5/output/LayerNorm/beta tower/text/bert/encoder/layer_5/output/LayerNorm/beta
    assign:  bert/encoder/layer_5/output/LayerNorm/gamma tower/text/bert/encoder/layer_5/output/LayerNorm/gamma
    assign:  bert/encoder/layer_5/output/dense/bias tower/text/bert/encoder/layer_5/output/dense/bias
    assign:  bert/encoder/layer_5/output/dense/kernel tower/text/bert/encoder/layer_5/output/dense/kernel
    assign:  bert/encoder/layer_6/attention/output/LayerNorm/beta tower/text/bert/encoder/layer_6/attention/output/LayerNorm/beta
    assign:  bert/encoder/layer_6/attention/output/LayerNorm/gamma tower/text/bert/encoder/layer_6/attention/output/LayerNorm/gamma
    assign:  bert/encoder/layer_6/attention/output/dense/bias tower/text/bert/encoder/layer_6/attention/output/dense/bias
    assign:  bert/encoder/layer_6/attention/output/dense/kernel tower/text/bert/encoder/layer_6/attention/output/dense/kernel
    assign:  bert/encoder/layer_6/attention/self/key/bias tower/text/bert/encoder/layer_6/attention/self/key/bias
    assign:  bert/encoder/layer_6/attention/self/key/kernel tower/text/bert/encoder/layer_6/attention/self/key/kernel
    assign:  bert/encoder/layer_6/attention/self/query/bias tower/text/bert/encoder/layer_6/attention/self/query/bias
    assign:  bert/encoder/layer_6/attention/self/query/kernel tower/text/bert/encoder/layer_6/attention/self/query/kernel
    assign:  bert/encoder/layer_6/attention/self/value/bias tower/text/bert/encoder/layer_6/attention/self/value/bias
    assign:  bert/encoder/layer_6/attention/self/value/kernel tower/text/bert/encoder/layer_6/attention/self/value/kernel
    assign:  bert/encoder/layer_6/intermediate/dense/bias tower/text/bert/encoder/layer_6/intermediate/dense/bias
    assign:  bert/encoder/layer_6/intermediate/dense/kernel tower/text/bert/encoder/layer_6/intermediate/dense/kernel
    assign:  bert/encoder/layer_6/output/LayerNorm/beta tower/text/bert/encoder/layer_6/output/LayerNorm/beta
    assign:  bert/encoder/layer_6/output/LayerNorm/gamma tower/text/bert/encoder/layer_6/output/LayerNorm/gamma
    assign:  bert/encoder/layer_6/output/dense/bias tower/text/bert/encoder/layer_6/output/dense/bias
    assign:  bert/encoder/layer_6/output/dense/kernel tower/text/bert/encoder/layer_6/output/dense/kernel
    assign:  bert/encoder/layer_7/attention/output/LayerNorm/beta tower/text/bert/encoder/layer_7/attention/output/LayerNorm/beta
    assign:  bert/encoder/layer_7/attention/output/LayerNorm/gamma tower/text/bert/encoder/layer_7/attention/output/LayerNorm/gamma
    assign:  bert/encoder/layer_7/attention/output/dense/bias tower/text/bert/encoder/layer_7/attention/output/dense/bias
    assign:  bert/encoder/layer_7/attention/output/dense/kernel tower/text/bert/encoder/layer_7/attention/output/dense/kernel
    assign:  bert/encoder/layer_7/attention/self/key/bias tower/text/bert/encoder/layer_7/attention/self/key/bias
    assign:  bert/encoder/layer_7/attention/self/key/kernel tower/text/bert/encoder/layer_7/attention/self/key/kernel
    assign:  bert/encoder/layer_7/attention/self/query/bias tower/text/bert/encoder/layer_7/attention/self/query/bias
    assign:  bert/encoder/layer_7/attention/self/query/kernel tower/text/bert/encoder/layer_7/attention/self/query/kernel
    assign:  bert/encoder/layer_7/attention/self/value/bias tower/text/bert/encoder/layer_7/attention/self/value/bias
    assign:  bert/encoder/layer_7/attention/self/value/kernel tower/text/bert/encoder/layer_7/attention/self/value/kernel
    assign:  bert/encoder/layer_7/intermediate/dense/bias tower/text/bert/encoder/layer_7/intermediate/dense/bias
    assign:  bert/encoder/layer_7/intermediate/dense/kernel tower/text/bert/encoder/layer_7/intermediate/dense/kernel
    assign:  bert/encoder/layer_7/output/LayerNorm/beta tower/text/bert/encoder/layer_7/output/LayerNorm/beta
    assign:  bert/encoder/layer_7/output/LayerNorm/gamma tower/text/bert/encoder/layer_7/output/LayerNorm/gamma
    assign:  bert/encoder/layer_7/output/dense/bias tower/text/bert/encoder/layer_7/output/dense/bias
    assign:  bert/encoder/layer_7/output/dense/kernel tower/text/bert/encoder/layer_7/output/dense/kernel
    assign:  bert/encoder/layer_8/attention/output/LayerNorm/beta tower/text/bert/encoder/layer_8/attention/output/LayerNorm/beta
    assign:  bert/encoder/layer_8/attention/output/LayerNorm/gamma tower/text/bert/encoder/layer_8/attention/output/LayerNorm/gamma
    assign:  bert/encoder/layer_8/attention/output/dense/bias tower/text/bert/encoder/layer_8/attention/output/dense/bias
    assign:  bert/encoder/layer_8/attention/output/dense/kernel tower/text/bert/encoder/layer_8/attention/output/dense/kernel
    assign:  bert/encoder/layer_8/attention/self/key/bias tower/text/bert/encoder/layer_8/attention/self/key/bias
    assign:  bert/encoder/layer_8/attention/self/key/kernel tower/text/bert/encoder/layer_8/attention/self/key/kernel
    assign:  bert/encoder/layer_8/attention/self/query/bias tower/text/bert/encoder/layer_8/attention/self/query/bias
    assign:  bert/encoder/layer_8/attention/self/query/kernel tower/text/bert/encoder/layer_8/attention/self/query/kernel
    assign:  bert/encoder/layer_8/attention/self/value/bias tower/text/bert/encoder/layer_8/attention/self/value/bias
    assign:  bert/encoder/layer_8/attention/self/value/kernel tower/text/bert/encoder/layer_8/attention/self/value/kernel
    assign:  bert/encoder/layer_8/intermediate/dense/bias tower/text/bert/encoder/layer_8/intermediate/dense/bias
    assign:  bert/encoder/layer_8/intermediate/dense/kernel tower/text/bert/encoder/layer_8/intermediate/dense/kernel
    assign:  bert/encoder/layer_8/output/LayerNorm/beta tower/text/bert/encoder/layer_8/output/LayerNorm/beta
    assign:  bert/encoder/layer_8/output/LayerNorm/gamma tower/text/bert/encoder/layer_8/output/LayerNorm/gamma
    assign:  bert/encoder/layer_8/output/dense/bias tower/text/bert/encoder/layer_8/output/dense/bias
    assign:  bert/encoder/layer_8/output/dense/kernel tower/text/bert/encoder/layer_8/output/dense/kernel
    assign:  bert/encoder/layer_9/attention/output/LayerNorm/beta tower/text/bert/encoder/layer_9/attention/output/LayerNorm/beta
    assign:  bert/encoder/layer_9/attention/output/LayerNorm/gamma tower/text/bert/encoder/layer_9/attention/output/LayerNorm/gamma
    assign:  bert/encoder/layer_9/attention/output/dense/bias tower/text/bert/encoder/layer_9/attention/output/dense/bias
    assign:  bert/encoder/layer_9/attention/output/dense/kernel tower/text/bert/encoder/layer_9/attention/output/dense/kernel
    assign:  bert/encoder/layer_9/attention/self/key/bias tower/text/bert/encoder/layer_9/attention/self/key/bias
    assign:  bert/encoder/layer_9/attention/self/key/kernel tower/text/bert/encoder/layer_9/attention/self/key/kernel
    assign:  bert/encoder/layer_9/attention/self/query/bias tower/text/bert/encoder/layer_9/attention/self/query/bias
    assign:  bert/encoder/layer_9/attention/self/query/kernel tower/text/bert/encoder/layer_9/attention/self/query/kernel
    assign:  bert/encoder/layer_9/attention/self/value/bias tower/text/bert/encoder/layer_9/attention/self/value/bias
    assign:  bert/encoder/layer_9/attention/self/value/kernel tower/text/bert/encoder/layer_9/attention/self/value/kernel
    assign:  bert/encoder/layer_9/intermediate/dense/bias tower/text/bert/encoder/layer_9/intermediate/dense/bias
    assign:  bert/encoder/layer_9/intermediate/dense/kernel tower/text/bert/encoder/layer_9/intermediate/dense/kernel
    assign:  bert/encoder/layer_9/output/LayerNorm/beta tower/text/bert/encoder/layer_9/output/LayerNorm/beta
    assign:  bert/encoder/layer_9/output/LayerNorm/gamma tower/text/bert/encoder/layer_9/output/LayerNorm/gamma
    assign:  bert/encoder/layer_9/output/dense/bias tower/text/bert/encoder/layer_9/output/dense/bias
    assign:  bert/encoder/layer_9/output/dense/kernel tower/text/bert/encoder/layer_9/output/dense/kernel
    assign:  bert/pooler/dense/bias tower/text/bert/pooler/dense/bias
    assign:  bert/pooler/dense/kernel tower/text/bert/pooler/dense/kernel
    not in variables: cls/predictions/output_bias
    not in variables: cls/predictions/transform/LayerNorm/beta
    not in variables: cls/predictions/transform/LayerNorm/gamma
    not in variables: cls/predictions/transform/dense/bias
    not in variables: cls/predictions/transform/dense/kernel
    not in variables: cls/seq_relationship/output_bias
    not in variables: cls/seq_relationship/output_weights
    WARNING:tensorflow:From scripts/train_tagging.py:47: The name tf.train.init_from_checkpoint is deprecated. Please use tf.compat.v1.train.init_from_checkpoint instead.
    
    load text_pretrained_model: pretrained/bert/chinese_L-12_H-768_A-12/bert_model.ckpt
    not in variables: global_step
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/BatchNorm/beta tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/BatchNorm/beta
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/BatchNorm/gamma tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/BatchNorm/gamma
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/BatchNorm/moving_mean tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/BatchNorm/moving_variance tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/weights tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/weights
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv1/weights/Momentum
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/BatchNorm/beta tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/BatchNorm/beta
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/BatchNorm/gamma tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/BatchNorm/gamma
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/BatchNorm/moving_mean tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/BatchNorm/moving_variance tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/weights tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/weights
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv2/weights/Momentum
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/conv3/biases tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv3/biases
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv3/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv3/biases/Momentum
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/conv3/weights tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/conv3/weights
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv3/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/conv3/weights/Momentum
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/preact/beta tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/preact/beta
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/preact/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/preact/beta/Momentum
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/preact/gamma tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/preact/gamma
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/preact/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/preact/gamma/Momentum
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/preact/moving_mean tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/preact/moving_mean
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/preact/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/preact/moving_variance tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/preact/moving_variance
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/preact/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/shortcut/biases tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/shortcut/biases
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/shortcut/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/shortcut/biases/Momentum
    assign:  resnet_v2_50/block1/unit_1/bottleneck_v2/shortcut/weights tower/image/resnet_v2_50/block1/unit_1/bottleneck_v2/shortcut/weights
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/shortcut/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_1/bottleneck_v2/shortcut/weights/Momentum
    assign:  resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/BatchNorm/beta tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/BatchNorm/beta
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/BatchNorm/gamma tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/BatchNorm/gamma
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/BatchNorm/moving_mean tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/BatchNorm/moving_variance tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/weights tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/weights
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv1/weights/Momentum
    assign:  resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/BatchNorm/beta tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/BatchNorm/beta
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/BatchNorm/gamma tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/BatchNorm/gamma
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/BatchNorm/moving_mean tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/BatchNorm/moving_variance tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/weights tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/weights
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv2/weights/Momentum
    assign:  resnet_v2_50/block1/unit_2/bottleneck_v2/conv3/biases tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv3/biases
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv3/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv3/biases/Momentum
    assign:  resnet_v2_50/block1/unit_2/bottleneck_v2/conv3/weights tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/conv3/weights
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv3/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/conv3/weights/Momentum
    assign:  resnet_v2_50/block1/unit_2/bottleneck_v2/preact/beta tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/preact/beta
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/preact/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/preact/beta/Momentum
    assign:  resnet_v2_50/block1/unit_2/bottleneck_v2/preact/gamma tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/preact/gamma
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/preact/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/preact/gamma/Momentum
    assign:  resnet_v2_50/block1/unit_2/bottleneck_v2/preact/moving_mean tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/preact/moving_mean
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/preact/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block1/unit_2/bottleneck_v2/preact/moving_variance tower/image/resnet_v2_50/block1/unit_2/bottleneck_v2/preact/moving_variance
    not in variables: resnet_v2_50/block1/unit_2/bottleneck_v2/preact/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/BatchNorm/beta tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/BatchNorm/beta
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/BatchNorm/gamma tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/BatchNorm/gamma
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/BatchNorm/moving_mean tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/BatchNorm/moving_variance tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/weights tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/weights
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv1/weights/Momentum
    assign:  resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/BatchNorm/beta tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/BatchNorm/beta
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/BatchNorm/gamma tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/BatchNorm/gamma
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/BatchNorm/moving_mean tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/BatchNorm/moving_variance tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/weights tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/weights
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv2/weights/Momentum
    assign:  resnet_v2_50/block1/unit_3/bottleneck_v2/conv3/biases tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv3/biases
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv3/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv3/biases/Momentum
    assign:  resnet_v2_50/block1/unit_3/bottleneck_v2/conv3/weights tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/conv3/weights
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv3/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/conv3/weights/Momentum
    assign:  resnet_v2_50/block1/unit_3/bottleneck_v2/preact/beta tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/preact/beta
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/preact/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/preact/beta/Momentum
    assign:  resnet_v2_50/block1/unit_3/bottleneck_v2/preact/gamma tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/preact/gamma
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/preact/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/preact/gamma/Momentum
    assign:  resnet_v2_50/block1/unit_3/bottleneck_v2/preact/moving_mean tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/preact/moving_mean
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/preact/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block1/unit_3/bottleneck_v2/preact/moving_variance tower/image/resnet_v2_50/block1/unit_3/bottleneck_v2/preact/moving_variance
    not in variables: resnet_v2_50/block1/unit_3/bottleneck_v2/preact/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/BatchNorm/beta tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/BatchNorm/beta
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/BatchNorm/gamma tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/BatchNorm/gamma
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/BatchNorm/moving_mean tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/BatchNorm/moving_variance tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/weights tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/weights
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv1/weights/Momentum
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/BatchNorm/beta tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/BatchNorm/beta
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/BatchNorm/gamma tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/BatchNorm/gamma
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/BatchNorm/moving_mean tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/BatchNorm/moving_variance tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/weights tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/weights
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv2/weights/Momentum
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/conv3/biases tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv3/biases
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv3/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv3/biases/Momentum
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/conv3/weights tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/conv3/weights
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv3/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/conv3/weights/Momentum
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/preact/beta tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/preact/beta
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/preact/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/preact/beta/Momentum
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/preact/gamma tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/preact/gamma
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/preact/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/preact/gamma/Momentum
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/preact/moving_mean tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/preact/moving_mean
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/preact/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/preact/moving_variance tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/preact/moving_variance
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/preact/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/shortcut/biases tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/shortcut/biases
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/shortcut/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/shortcut/biases/Momentum
    assign:  resnet_v2_50/block2/unit_1/bottleneck_v2/shortcut/weights tower/image/resnet_v2_50/block2/unit_1/bottleneck_v2/shortcut/weights
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/shortcut/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_1/bottleneck_v2/shortcut/weights/Momentum
    assign:  resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/BatchNorm/beta tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/BatchNorm/beta
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/BatchNorm/gamma tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/BatchNorm/gamma
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/BatchNorm/moving_mean tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/BatchNorm/moving_variance tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/weights tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/weights
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv1/weights/Momentum
    assign:  resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/BatchNorm/beta tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/BatchNorm/beta
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/BatchNorm/gamma tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/BatchNorm/gamma
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/BatchNorm/moving_mean tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/BatchNorm/moving_variance tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/weights tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/weights
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv2/weights/Momentum
    assign:  resnet_v2_50/block2/unit_2/bottleneck_v2/conv3/biases tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv3/biases
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv3/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv3/biases/Momentum
    assign:  resnet_v2_50/block2/unit_2/bottleneck_v2/conv3/weights tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/conv3/weights
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv3/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/conv3/weights/Momentum
    assign:  resnet_v2_50/block2/unit_2/bottleneck_v2/preact/beta tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/preact/beta
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/preact/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/preact/beta/Momentum
    assign:  resnet_v2_50/block2/unit_2/bottleneck_v2/preact/gamma tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/preact/gamma
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/preact/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/preact/gamma/Momentum
    assign:  resnet_v2_50/block2/unit_2/bottleneck_v2/preact/moving_mean tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/preact/moving_mean
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/preact/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_2/bottleneck_v2/preact/moving_variance tower/image/resnet_v2_50/block2/unit_2/bottleneck_v2/preact/moving_variance
    not in variables: resnet_v2_50/block2/unit_2/bottleneck_v2/preact/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/BatchNorm/beta tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/BatchNorm/beta
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/BatchNorm/gamma tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/BatchNorm/gamma
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/BatchNorm/moving_mean tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/BatchNorm/moving_variance tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/weights tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/weights
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv1/weights/Momentum
    assign:  resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/BatchNorm/beta tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/BatchNorm/beta
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/BatchNorm/gamma tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/BatchNorm/gamma
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/BatchNorm/moving_mean tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/BatchNorm/moving_variance tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/weights tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/weights
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv2/weights/Momentum
    assign:  resnet_v2_50/block2/unit_3/bottleneck_v2/conv3/biases tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv3/biases
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv3/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv3/biases/Momentum
    assign:  resnet_v2_50/block2/unit_3/bottleneck_v2/conv3/weights tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/conv3/weights
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv3/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/conv3/weights/Momentum
    assign:  resnet_v2_50/block2/unit_3/bottleneck_v2/preact/beta tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/preact/beta
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/preact/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/preact/beta/Momentum
    assign:  resnet_v2_50/block2/unit_3/bottleneck_v2/preact/gamma tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/preact/gamma
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/preact/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/preact/gamma/Momentum
    assign:  resnet_v2_50/block2/unit_3/bottleneck_v2/preact/moving_mean tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/preact/moving_mean
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/preact/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_3/bottleneck_v2/preact/moving_variance tower/image/resnet_v2_50/block2/unit_3/bottleneck_v2/preact/moving_variance
    not in variables: resnet_v2_50/block2/unit_3/bottleneck_v2/preact/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/BatchNorm/beta tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/BatchNorm/beta
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/BatchNorm/gamma tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/BatchNorm/gamma
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/BatchNorm/moving_mean tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/BatchNorm/moving_variance tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/weights tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/weights
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv1/weights/Momentum
    assign:  resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/BatchNorm/beta tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/BatchNorm/beta
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/BatchNorm/gamma tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/BatchNorm/gamma
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/BatchNorm/moving_mean tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/BatchNorm/moving_variance tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/weights tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/weights
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv2/weights/Momentum
    assign:  resnet_v2_50/block2/unit_4/bottleneck_v2/conv3/biases tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv3/biases
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv3/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv3/biases/Momentum
    assign:  resnet_v2_50/block2/unit_4/bottleneck_v2/conv3/weights tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/conv3/weights
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv3/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/conv3/weights/Momentum
    assign:  resnet_v2_50/block2/unit_4/bottleneck_v2/preact/beta tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/preact/beta
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/preact/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/preact/beta/Momentum
    assign:  resnet_v2_50/block2/unit_4/bottleneck_v2/preact/gamma tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/preact/gamma
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/preact/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/preact/gamma/Momentum
    assign:  resnet_v2_50/block2/unit_4/bottleneck_v2/preact/moving_mean tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/preact/moving_mean
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/preact/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block2/unit_4/bottleneck_v2/preact/moving_variance tower/image/resnet_v2_50/block2/unit_4/bottleneck_v2/preact/moving_variance
    not in variables: resnet_v2_50/block2/unit_4/bottleneck_v2/preact/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/BatchNorm/beta tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/BatchNorm/beta
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/BatchNorm/gamma tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/BatchNorm/gamma
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/BatchNorm/moving_mean tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/BatchNorm/moving_variance tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/weights tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/weights
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv1/weights/Momentum
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/BatchNorm/beta tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/BatchNorm/beta
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/BatchNorm/gamma tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/BatchNorm/gamma
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/BatchNorm/moving_mean tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/BatchNorm/moving_variance tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/weights tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/weights
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv2/weights/Momentum
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/conv3/biases tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv3/biases
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv3/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv3/biases/Momentum
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/conv3/weights tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/conv3/weights
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv3/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/conv3/weights/Momentum
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/preact/beta tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/preact/beta
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/preact/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/preact/beta/Momentum
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/preact/gamma tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/preact/gamma
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/preact/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/preact/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/preact/moving_mean tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/preact/moving_mean
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/preact/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/preact/moving_variance tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/preact/moving_variance
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/preact/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/shortcut/biases tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/shortcut/biases
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/shortcut/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/shortcut/biases/Momentum
    assign:  resnet_v2_50/block3/unit_1/bottleneck_v2/shortcut/weights tower/image/resnet_v2_50/block3/unit_1/bottleneck_v2/shortcut/weights
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/shortcut/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_1/bottleneck_v2/shortcut/weights/Momentum
    assign:  resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/BatchNorm/beta tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/BatchNorm/beta
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/BatchNorm/gamma tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/BatchNorm/gamma
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/BatchNorm/moving_mean tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/BatchNorm/moving_variance tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/weights tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/weights
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv1/weights/Momentum
    assign:  resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/BatchNorm/beta tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/BatchNorm/beta
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/BatchNorm/gamma tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/BatchNorm/gamma
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/BatchNorm/moving_mean tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/BatchNorm/moving_variance tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/weights tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/weights
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv2/weights/Momentum
    assign:  resnet_v2_50/block3/unit_2/bottleneck_v2/conv3/biases tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv3/biases
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv3/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv3/biases/Momentum
    assign:  resnet_v2_50/block3/unit_2/bottleneck_v2/conv3/weights tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/conv3/weights
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv3/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/conv3/weights/Momentum
    assign:  resnet_v2_50/block3/unit_2/bottleneck_v2/preact/beta tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/preact/beta
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/preact/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/preact/beta/Momentum
    assign:  resnet_v2_50/block3/unit_2/bottleneck_v2/preact/gamma tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/preact/gamma
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/preact/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/preact/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_2/bottleneck_v2/preact/moving_mean tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/preact/moving_mean
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/preact/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_2/bottleneck_v2/preact/moving_variance tower/image/resnet_v2_50/block3/unit_2/bottleneck_v2/preact/moving_variance
    not in variables: resnet_v2_50/block3/unit_2/bottleneck_v2/preact/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/BatchNorm/beta tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/BatchNorm/beta
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/BatchNorm/gamma tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/BatchNorm/gamma
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/BatchNorm/moving_mean tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/BatchNorm/moving_variance tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/weights tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/weights
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv1/weights/Momentum
    assign:  resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/BatchNorm/beta tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/BatchNorm/beta
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/BatchNorm/gamma tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/BatchNorm/gamma
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/BatchNorm/moving_mean tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/BatchNorm/moving_variance tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/weights tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/weights
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv2/weights/Momentum
    assign:  resnet_v2_50/block3/unit_3/bottleneck_v2/conv3/biases tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv3/biases
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv3/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv3/biases/Momentum
    assign:  resnet_v2_50/block3/unit_3/bottleneck_v2/conv3/weights tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/conv3/weights
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv3/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/conv3/weights/Momentum
    assign:  resnet_v2_50/block3/unit_3/bottleneck_v2/preact/beta tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/preact/beta
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/preact/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/preact/beta/Momentum
    assign:  resnet_v2_50/block3/unit_3/bottleneck_v2/preact/gamma tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/preact/gamma
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/preact/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/preact/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_3/bottleneck_v2/preact/moving_mean tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/preact/moving_mean
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/preact/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_3/bottleneck_v2/preact/moving_variance tower/image/resnet_v2_50/block3/unit_3/bottleneck_v2/preact/moving_variance
    not in variables: resnet_v2_50/block3/unit_3/bottleneck_v2/preact/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/BatchNorm/beta tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/BatchNorm/beta
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/BatchNorm/gamma tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/BatchNorm/gamma
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/BatchNorm/moving_mean tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/BatchNorm/moving_variance tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/weights tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/weights
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv1/weights/Momentum
    assign:  resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/BatchNorm/beta tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/BatchNorm/beta
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/BatchNorm/gamma tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/BatchNorm/gamma
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/BatchNorm/moving_mean tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/BatchNorm/moving_variance tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/weights tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/weights
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv2/weights/Momentum
    assign:  resnet_v2_50/block3/unit_4/bottleneck_v2/conv3/biases tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv3/biases
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv3/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv3/biases/Momentum
    assign:  resnet_v2_50/block3/unit_4/bottleneck_v2/conv3/weights tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/conv3/weights
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv3/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/conv3/weights/Momentum
    assign:  resnet_v2_50/block3/unit_4/bottleneck_v2/preact/beta tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/preact/beta
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/preact/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/preact/beta/Momentum
    assign:  resnet_v2_50/block3/unit_4/bottleneck_v2/preact/gamma tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/preact/gamma
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/preact/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/preact/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_4/bottleneck_v2/preact/moving_mean tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/preact/moving_mean
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/preact/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_4/bottleneck_v2/preact/moving_variance tower/image/resnet_v2_50/block3/unit_4/bottleneck_v2/preact/moving_variance
    not in variables: resnet_v2_50/block3/unit_4/bottleneck_v2/preact/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/BatchNorm/beta tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/BatchNorm/beta
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/BatchNorm/gamma tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/BatchNorm/gamma
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/BatchNorm/moving_mean tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/BatchNorm/moving_variance tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/weights tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/weights
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv1/weights/Momentum
    assign:  resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/BatchNorm/beta tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/BatchNorm/beta
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/BatchNorm/gamma tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/BatchNorm/gamma
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/BatchNorm/moving_mean tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/BatchNorm/moving_variance tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/weights tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/weights
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv2/weights/Momentum
    assign:  resnet_v2_50/block3/unit_5/bottleneck_v2/conv3/biases tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv3/biases
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv3/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv3/biases/Momentum
    assign:  resnet_v2_50/block3/unit_5/bottleneck_v2/conv3/weights tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/conv3/weights
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv3/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/conv3/weights/Momentum
    assign:  resnet_v2_50/block3/unit_5/bottleneck_v2/preact/beta tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/preact/beta
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/preact/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/preact/beta/Momentum
    assign:  resnet_v2_50/block3/unit_5/bottleneck_v2/preact/gamma tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/preact/gamma
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/preact/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/preact/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_5/bottleneck_v2/preact/moving_mean tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/preact/moving_mean
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/preact/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_5/bottleneck_v2/preact/moving_variance tower/image/resnet_v2_50/block3/unit_5/bottleneck_v2/preact/moving_variance
    not in variables: resnet_v2_50/block3/unit_5/bottleneck_v2/preact/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/BatchNorm/beta tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/BatchNorm/beta
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/BatchNorm/gamma tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/BatchNorm/gamma
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/BatchNorm/moving_mean tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/BatchNorm/moving_variance tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/weights tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/weights
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv1/weights/Momentum
    assign:  resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/BatchNorm/beta tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/BatchNorm/beta
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/BatchNorm/gamma tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/BatchNorm/gamma
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/BatchNorm/moving_mean tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/BatchNorm/moving_variance tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/weights tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/weights
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv2/weights/Momentum
    assign:  resnet_v2_50/block3/unit_6/bottleneck_v2/conv3/biases tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv3/biases
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv3/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv3/biases/Momentum
    assign:  resnet_v2_50/block3/unit_6/bottleneck_v2/conv3/weights tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/conv3/weights
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv3/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/conv3/weights/Momentum
    assign:  resnet_v2_50/block3/unit_6/bottleneck_v2/preact/beta tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/preact/beta
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/preact/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/preact/beta/Momentum
    assign:  resnet_v2_50/block3/unit_6/bottleneck_v2/preact/gamma tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/preact/gamma
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/preact/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/preact/gamma/Momentum
    assign:  resnet_v2_50/block3/unit_6/bottleneck_v2/preact/moving_mean tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/preact/moving_mean
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/preact/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block3/unit_6/bottleneck_v2/preact/moving_variance tower/image/resnet_v2_50/block3/unit_6/bottleneck_v2/preact/moving_variance
    not in variables: resnet_v2_50/block3/unit_6/bottleneck_v2/preact/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/BatchNorm/beta tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/BatchNorm/beta
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/BatchNorm/gamma tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/BatchNorm/gamma
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/BatchNorm/moving_mean tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/BatchNorm/moving_variance tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/weights tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/weights
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv1/weights/Momentum
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/BatchNorm/beta tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/BatchNorm/beta
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/BatchNorm/gamma tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/BatchNorm/gamma
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/BatchNorm/moving_mean tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/BatchNorm/moving_variance tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/weights tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/weights
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv2/weights/Momentum
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/conv3/biases tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv3/biases
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv3/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv3/biases/Momentum
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/conv3/weights tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/conv3/weights
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv3/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/conv3/weights/Momentum
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/preact/beta tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/preact/beta
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/preact/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/preact/beta/Momentum
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/preact/gamma tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/preact/gamma
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/preact/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/preact/gamma/Momentum
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/preact/moving_mean tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/preact/moving_mean
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/preact/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/preact/moving_variance tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/preact/moving_variance
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/preact/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/shortcut/biases tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/shortcut/biases
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/shortcut/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/shortcut/biases/Momentum
    assign:  resnet_v2_50/block4/unit_1/bottleneck_v2/shortcut/weights tower/image/resnet_v2_50/block4/unit_1/bottleneck_v2/shortcut/weights
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/shortcut/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_1/bottleneck_v2/shortcut/weights/Momentum
    assign:  resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/BatchNorm/beta tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/BatchNorm/beta
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/BatchNorm/gamma tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/BatchNorm/gamma
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/BatchNorm/moving_mean tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/BatchNorm/moving_variance tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/weights tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/weights
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv1/weights/Momentum
    assign:  resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/BatchNorm/beta tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/BatchNorm/beta
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/BatchNorm/gamma tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/BatchNorm/gamma
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/BatchNorm/moving_mean tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/BatchNorm/moving_variance tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/weights tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/weights
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv2/weights/Momentum
    assign:  resnet_v2_50/block4/unit_2/bottleneck_v2/conv3/biases tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv3/biases
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv3/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv3/biases/Momentum
    assign:  resnet_v2_50/block4/unit_2/bottleneck_v2/conv3/weights tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/conv3/weights
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv3/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/conv3/weights/Momentum
    assign:  resnet_v2_50/block4/unit_2/bottleneck_v2/preact/beta tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/preact/beta
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/preact/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/preact/beta/Momentum
    assign:  resnet_v2_50/block4/unit_2/bottleneck_v2/preact/gamma tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/preact/gamma
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/preact/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/preact/gamma/Momentum
    assign:  resnet_v2_50/block4/unit_2/bottleneck_v2/preact/moving_mean tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/preact/moving_mean
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/preact/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_2/bottleneck_v2/preact/moving_variance tower/image/resnet_v2_50/block4/unit_2/bottleneck_v2/preact/moving_variance
    not in variables: resnet_v2_50/block4/unit_2/bottleneck_v2/preact/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/BatchNorm/beta tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/BatchNorm/beta
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/BatchNorm/gamma tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/BatchNorm/gamma
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/BatchNorm/moving_mean tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/BatchNorm/moving_variance tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/weights tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/weights
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv1/weights/Momentum
    assign:  resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/BatchNorm/beta tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/BatchNorm/beta
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/BatchNorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/BatchNorm/beta/Momentum
    assign:  resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/BatchNorm/gamma tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/BatchNorm/gamma
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/BatchNorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/BatchNorm/gamma/Momentum
    assign:  resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/BatchNorm/moving_mean tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/BatchNorm/moving_mean
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/BatchNorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/BatchNorm/moving_variance tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/BatchNorm/moving_variance
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/BatchNorm/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/weights tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/weights
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv2/weights/Momentum
    assign:  resnet_v2_50/block4/unit_3/bottleneck_v2/conv3/biases tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv3/biases
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv3/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv3/biases/Momentum
    assign:  resnet_v2_50/block4/unit_3/bottleneck_v2/conv3/weights tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/conv3/weights
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv3/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/conv3/weights/Momentum
    assign:  resnet_v2_50/block4/unit_3/bottleneck_v2/preact/beta tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/preact/beta
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/preact/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/preact/beta/Momentum
    assign:  resnet_v2_50/block4/unit_3/bottleneck_v2/preact/gamma tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/preact/gamma
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/preact/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/preact/gamma/Momentum
    assign:  resnet_v2_50/block4/unit_3/bottleneck_v2/preact/moving_mean tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/preact/moving_mean
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/preact/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/block4/unit_3/bottleneck_v2/preact/moving_variance tower/image/resnet_v2_50/block4/unit_3/bottleneck_v2/preact/moving_variance
    not in variables: resnet_v2_50/block4/unit_3/bottleneck_v2/preact/moving_variance/ExponentialMovingAverage
    assign:  resnet_v2_50/conv1/biases tower/image/resnet_v2_50/conv1/biases
    not in variables: resnet_v2_50/conv1/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/conv1/biases/Momentum
    assign:  resnet_v2_50/conv1/weights tower/image/resnet_v2_50/conv1/weights
    not in variables: resnet_v2_50/conv1/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/conv1/weights/Momentum
    not in variables: resnet_v2_50/logits/biases
    not in variables: resnet_v2_50/logits/biases/ExponentialMovingAverage
    not in variables: resnet_v2_50/logits/biases/Momentum
    not in variables: resnet_v2_50/logits/weights
    not in variables: resnet_v2_50/logits/weights/ExponentialMovingAverage
    not in variables: resnet_v2_50/logits/weights/Momentum
    assign:  resnet_v2_50/postnorm/beta tower/image/resnet_v2_50/postnorm/beta
    not in variables: resnet_v2_50/postnorm/beta/ExponentialMovingAverage
    not in variables: resnet_v2_50/postnorm/beta/Momentum
    assign:  resnet_v2_50/postnorm/gamma tower/image/resnet_v2_50/postnorm/gamma
    not in variables: resnet_v2_50/postnorm/gamma/ExponentialMovingAverage
    not in variables: resnet_v2_50/postnorm/gamma/Momentum
    assign:  resnet_v2_50/postnorm/moving_mean tower/image/resnet_v2_50/postnorm/moving_mean
    not in variables: resnet_v2_50/postnorm/moving_mean/ExponentialMovingAverage
    assign:  resnet_v2_50/postnorm/moving_variance tower/image/resnet_v2_50/postnorm/moving_variance
    not in variables: resnet_v2_50/postnorm/moving_variance/ExponentialMovingAverage
    not in variables: total_loss/ExponentialMovingAverage
    load image_pretrained_model: pretrained/resnet_v2_50/resnet_v2_50.ckpt
    WARNING:tensorflow:From /home/tione/notebook/MultiModal-Tagging/utils/base_trainer.py:273: Supervisor.__init__ (from tensorflow.python.training.supervisor) is deprecated and will be removed in a future version.
    Instructions for updating:
    Please switch to tf.train.MonitoredTrainingSession
    INFO:tensorflow:/job:master/task:0: Starting managed session.
    INFO:tensorflow:Running local_init_op.
    INFO:tensorflow:Done running local_init_op.
    INFO:tensorflow:Starting standard services.
    INFO:tensorflow:Starting queue runners.
    INFO:tensorflow:/job:master/task:0: Entering training loop.
    INFO:tensorflow:global_step/sec: 0
    INFO:tensorflow:Recording summary at step 0.
    INFO:tensorflow:training step 1 | tagging_loss_video: 121.484|tagging_loss_audio: 140.009|tagging_loss_text: 145.842|tagging_loss_image: 133.549|tagging_loss_fusion: 204.537|total_loss: 745.421 | 0.80 Examples/sec
    INFO:tensorflow:training step 2 | tagging_loss_video: 140.286|tagging_loss_audio: 173.535|tagging_loss_text: 151.918|tagging_loss_image: 136.746|tagging_loss_fusion: 208.594|total_loss: 811.079 | 2.14 Examples/sec
    INFO:tensorflow:training step 3 | tagging_loss_video: 81.015|tagging_loss_audio: 95.206|tagging_loss_text: 102.527|tagging_loss_image: 85.364|tagging_loss_fusion: 134.548|total_loss: 498.660 | 2.15 Examples/sec
    INFO:tensorflow:training step 4 | tagging_loss_video: 50.472|tagging_loss_audio: 40.454|tagging_loss_text: 79.873|tagging_loss_image: 64.196|tagging_loss_fusion: 68.660|total_loss: 303.655 | 2.18 Examples/sec
    INFO:tensorflow:training step 5 | tagging_loss_video: 27.307|tagging_loss_audio: 19.787|tagging_loss_text: 34.409|tagging_loss_image: 21.625|tagging_loss_fusion: 36.715|total_loss: 139.842 | 2.12 Examples/sec
    INFO:tensorflow:training step 6 | tagging_loss_video: 16.184|tagging_loss_audio: 13.182|tagging_loss_text: 21.811|tagging_loss_image: 29.958|tagging_loss_fusion: 23.158|total_loss: 104.293 | 2.17 Examples/sec
    INFO:tensorflow:global_step/sec: 0.0594097
    ^C


### 模型测试

Baseline的测试可以直接使用 ./run.sh test \[CHECKPOINT_DIR\] 进行，成功执行后会在VideoStructuring/MultiModal-Tagging/results/目录下生成tagging_5k_A.json结果文件。  
提交这个文件就可以参与排名。  
注意: ./run.sh test的特征提取时间较长（13小时左右），为了简化操作，baseline的测试集特征提取已预先完成，test时长约为半小时左右。用户可以自由地优化算法与相关流程。  


```python
!cd ~/notebook/VideoStructuring && sudo chmod a+x ./run.sh && ./run.sh test checkpoints/tagging_train799/export/step_2000_0.5608
```
