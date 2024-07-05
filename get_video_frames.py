import os
import cv2

video_path = 'videos/'
transcripts_list = []

for filename in os.listdir(video_path):
    video_id,ext= os.path.splitext(filename)
    print(video_id)
    out_folder = 'images/'+video_id
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
        
    every_n_seconds = 3     
    vidcap = cv2.VideoCapture('videos/'+filename)
    count = 0
    success = True
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    
    while success:
        success, image = vidcap.read()
        if (
            count % (every_n_seconds * fps) == fps
        ):  # every n seconds + 1 as we don't care about second 0 but actually second 1
            try:
                cv2.imwrite(f"{out_folder}/frame_{count/fps}.jpg", image)
            except:
                print("fail to save")
        count += 1