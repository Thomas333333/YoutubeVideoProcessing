# youtube医学视频处理
两个视频处理工具的代码。
+ OCR：[tesseract-ocr](https://github.com/tesseract-ocr/tesseract)
+ ASR：[YouTubeTranscriptApi](https://pypi.org/project/youtube-transcript-api/)
## 版本
+ python版本：3.8
+ 安装依赖包
```commandline
 conda install --yes --file requirements.txt 
```
## 参考
+ 参考了[队伍Dossier的代码](https://github.com/ProjectDossier/MedVid2022/tree/main/MedVidQA)
+ 可能有帮助的内容：2022年[队伍Dossier在VTT上的认识](https://aclanthology.org/2022.bionlp-1.43.pdf) 4.2节

## 效果
+ [YouTubeTranscriptApi](https://github.com/jdepoix/youtube-transcript-api)
  + 优点：是从网页直接抓取字幕，不需要下载Youtube视频到本地。响应速度快。而且处理出来的字幕效果好。
  + 缺点：从json文件来看，断句的时间不是很合适，后期需要整合。
+ [tesseract](https://github.com/tesseract-ocr/tesseract)
  + 优点：能够提取视频帧图片出现的文字。
  + 缺点：从json文件来看，提取效果不佳，存在乱码，而且ocr速度较慢。

## 程序解析
+ `api.py`调用`YouTubeTranscriptApi`来抓取对应youtube视频id的字幕。输出为`test.json`。
+ `get_video_frames.py`利用`cv2`来对视频进行分帧，每3s取一帧，保存在`images\`下。
+ `ocr_image.py`调用`pytesseract`来对每个视频帧进行ocr识别，输出结果在`ocr\ocr.json`。

## 实现避雷
+ `YouTubeTranscriptApi`在大陆没法正常使用，我在`windows`上的魔法无法确认代理的具体端口号，所以换在linux上用魔法。
+ `tesseract`
  + 除了安装python包，还要去[主页](https://github.com/tesseract-ocr/tesseract)下载对应的exe实现，并修改路径。
  + 在`windwos`平台上，修改安装位置还要改python包内文件的路径，同时加入环境变量。详情参考[csdn博客](https://blog.csdn.net/qq_42402648/article/details/120598537?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522172018163216800188525391%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=172018163216800188525391&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-120598537-null-null.142^v100^pc_search_result_base4&utm_term=pytesseract%20pip%E5%AE%89%E8%A3%85&spm=1018.2226.3001.4187)
