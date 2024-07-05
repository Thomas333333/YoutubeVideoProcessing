# youtube医学视频处理

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

