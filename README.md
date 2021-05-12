# 2021TencentAds
* 关于taac2021赛道二的baseline，命名为**taac2021_baseline_tagging.md(from .ipynb文件),可优先参阅该文档**。
* 云服务器中预训练模型包含bert, inception, resnet, vggfish, 因为文件(**Multimodal-Tagging/pretrained**)较大，暂未上传至github，可按照baseline中指示将模型拷贝到服务器的可读写路径下。云服务器中预训练模型路径: home/notebook/algo-2021/baseline/tagging/VideoStructuring/MultiModal-Tagging/pretrained。 
* 数据集(**Multimodal-Tagging/dataset**)同上。路径: home/notebook/algo-2021/dataset, 可按照baseline指示链接至Multimodal-Tagging/dataset。
* baseline中测试集路径为videos/test_5k_A, 与可执行路径不符，已修改为videos/video_5k/test_5k。训练路径已经按照需求修改，原始路径为checkpoints/tagging5k_temp。
* 截至目前使用baseline进行的三次训练的日志文件已上传至google drive: https://drive.google.com/drive/folders/1iX_7_tBrJNkM78RwxDNq62Vzq0m-vtxE?usp=sharing
