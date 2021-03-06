import cv2
import os
from PIL import Image
import numpy as np
import sys

frame_count = 0
frame_num = 0
frame_width = 0
frame_height = 0

def video2img(video_name, img_size = None):
    global frame_count
    global frame_num
    global frame_width
    global frame_height

    cap = cv2.VideoCapture(video_name)
    res = cap.isOpened()
    frame_num = int(cap.get(7))      #视频总帧数
    frame_width = int(cap.get(3))    #帧宽度
    frame_height = int(cap.get(4))   #帧高度
    path = './imgs' #图片保存在运行该脚本下的'./imgs'目录下
    if not os.path.exists(path):
        os.mkdir(path)
    print('Total frames: ', frame_num)
    print('frame width: ', frame_width, ' pixels')
    print('frame height: ', frame_height, ' pixels')
    print('Converting video into images...')

    while res:
        frame_count += 1
        res, frame = cap.read()
        #params = []
        #params
        if(not res):
            print('Complete! ')
            break
        if(len(img_size) == 2): #如果指定了目标图像大小，则resize，否则保持默认
            frame = cv2.resize(frame, (img_size),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite("./imgs/%d.png"%frame_count, frame)
    cap.release()

def img2bin(file_name):
    global frame_num
    
    fp = open(file_name, 'wb+')  #以二进制格式写入，总是会创建一个新文件，从头开始写
    print('Converting images to binary file...')
    
    for img_count in range(1,frame_num+1):
        img = np.array(Image.open('./imgs/'+str(img_count)+'.png').convert('1'))  #convert转化为二值图像,0是黑,1是白
        #img = np.array(Image.open(str(img_count)+'.png').convert('L'))  #convert转化为灰度图像
        
        img = img.ravel()   #把二维矩阵展开为一维数组，一行一行地拼接
        #print(img)
        fp.write(img)   #写入时会把一位扩展为一字节

    fp.close()
    print('Complete! ')

if __name__ == "__main__":
    video_name = sys.argv[1]        #原文件名
    target_bin_name = sys.argv[2]   #生成的目标文件名
    img_size = []   #目标图像大小
    if(len(sys.argv) == 5): 
        img_size.append(int(sys.argv[3]))
        img_size.append(int(sys.argv[4]))
    elif(len(sys.argv)>3 or len(sys.argv)<3):
        raise RuntimeError("number of parameter error!")
        
    print("original video file name: ", video_name)
    print("target binary file name: ", target_bin_name)
    print("target image width: ", img_size[0] if(len(img_size)) else "default")
    print("target image height: ", img_size[1] if(len(img_size)) else "default")

    video2img(video_name, tuple(img_size))
    img2bin(target_bin_name)