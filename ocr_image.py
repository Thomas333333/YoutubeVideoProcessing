import argparse
import json
import os

import pytesseract
from PIL import Image

video_path = 'videos/'
out_list = []

#按照video文件夹内的id编号提取
for filename in os.listdir(video_path):
    video_id,ext= os.path.splitext(filename)
    print(video_id)
    transcript = []
    for image in os.listdir('images/'+video_id):
        ocred_text = pytesseract.image_to_string(
            Image.open('images/'+video_id+'/'+image)
        )
        frame_n = image.split(".")[0].split("_")[1]

        ocred_text = " ".join(ocred_text.split())

        if ocred_text:
            transcript.append(
                {"text": ocred_text, "start": float(frame_n), "duration": 3.0}
            )

    transcript_sorted = sorted(transcript, key=lambda d: d["start"])

    out_list.append({"video_id": video_id, "transcript": transcript_sorted})
    
with open(
            'ocr/ocr.json',
            "w",
        ) as fp:
            json.dump(out_list, fp, indent=2)