from youtube_transcript_api import YouTubeTranscriptApi
import requests
import json 
import os 

#设置代理，如果在香港可以注释6-13行试一试，并去掉22行的proxies参数
proxies = {
    "http": "http://127.0.0.1:8000",  # 替换为您的代理地址和端口
    "https": "http://127.0.0.1:8000",  # 替换为您的代理地址和端口
}
session = requests.Session()
session.proxies.update(proxies)
session.verify = False

video_path = 'videos/'
transcripts_list = []

#按照video文件夹内的id编号提取
for filename in os.listdir(video_path):
    video_id,ext= os.path.splitext(filename)
    print(video_id)
    transcript = YouTubeTranscriptApi.get_transcript(video_id,proxies=proxies)
    transcripts_list.append(
                {
                    "video_id": video_id,
                    "transcript": transcript,
                }
            )

with open('test.json', "w") as fp:#保存为json文件
    json.dump(transcripts_list, fp, indent=2)