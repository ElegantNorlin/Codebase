import cv2

'''
彩色图像直方图均衡化
'''
img = cv2.imread("./flower.png",1)
cv2.imshow("src",img)
#彩色图像均衡化，需要分解通道，对每一个通道均衡化
(b,g,r) = cv2.split(img)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
result = cv2.merge((bH,gH,rH))
cv2.imshow("dst",result)
cv2.waitKey(0)
cv2.destoryAllWindows()