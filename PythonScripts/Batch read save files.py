import os
import cv2
'''
批量读取指定的文件夹下图片(文件)并保存到指定的路径
'''
def read_path(file_pathname):
    #遍历该目录下的所有图片文件
    for filename in os.listdir(file_pathname):
        print(filename)
        img = cv2.imread(file_pathname+'/'+filename)
        # 彩色图像均衡化，需要分解通道，对每一个通道均衡化
        (b, g, r) = cv2.split(img)
        bH = cv2.equalizeHist(b)
        gH = cv2.equalizeHist(g)
        rH = cv2.equalizeHist(r)
        result = cv2.merge((bH, gH, rH))
        # cv2.imwrite(f"./pictures/{x}.png", result)  # 保存图片
        cv2.imwrite('./pic'+"/"+filename,result)

read_path("./1")

