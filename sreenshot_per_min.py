import os
import cv2
from IPython.display import clear_output

home_path = 'D:\\video\\'
save_path = 'D:\\3_min_screenshot\\'

os.chdir(home_path)
all_video_path = os.listdir(os.curdir)

if not os.path.isdir(save_path):
    os.mkdir(save_path)

for video_counter in range( 0 , len(all_video_path) ):
    #clear_output(wait=True)
    current_path = home_path + str(all_video_path[video_counter])
    
    print("目前處理： " + current_path)
    
    cap = cv2.VideoCapture(current_path) # 讀取電腦中的影片
    
    total_frames = round(cap.get(7)) # get all frame amount
    
    fps = round(cap.get(5)) # get fps
    
    print("影片總frame數： " + str(total_frames))
    print("影片FPS： " + str(fps))
    print("進度： ( " + str(video_counter + 1) + " / " + str(len(all_video_path)) + " )." )
    
    for frame_counter in range(0,int(total_frames/fps/60/3)+1):
        
        cap.set(1, fps*60*3*frame_counter );
        ret, frame = cap.read() # Read the frame
        
        video_name = all_video_path[video_counter].split('.')[0]
        
        frame_save_path = save_path + video_name 
        
        if not os.path.isdir(frame_save_path):
            os.mkdir(frame_save_path)
        
        cv2.imwrite(frame_save_path+ "\\"  + str(frame_counter*3)  + "_min.jpg", frame)
        
    print("--------done--------")
