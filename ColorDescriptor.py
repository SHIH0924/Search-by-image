"CBIR(Content-Base Image Retrieval)"
import numpy as np
import cv2

class ColorDescriptor:
    def __init__(self, bins):
        # store the number of bins for the HSV histogram
        self.bins = bins

    def describe(self, image):
        # 將圖像轉換為 HSV 顏色空間
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        features =[]
        # 抓取尺寸併計算圖像的中心
        (h,w) = image.shape[:2]
        (cx,cy) = (int(w*0.5), int(h*0.5))

        # 分割圖像
        segments =[(0,cx,0,cy),(cx,w,0,cy),(cx,w,cy,h),(0,cx,cy,h)]

        # 建構一個表示圖像中心的橢圓模版
        (axesX, axesY) =(int((w*0.75)/2), int((h*0.75)/2))
        ellipMask = np.zeros(image.shape[:2],np.uint8)#dtype="uint8"
        cv2.ellipse(ellipMask,(cx,cy),(axesX,axesY),0.0,0.0,360.0,255.0,-1)

        # 循環所有片段
        for(startX,endX, startY, endY) in segments:
            cornerMask = np.zeros(image.shape[:2],np.uint8)#dtype="uint8"
            cv2.rectangle(cornerMask,(startX,startY),(endX,endY),255,-1)
            cornerMask = cv2.subtract(cornerMask, ellipMask)

            # 計算直方圖
            hist = self.histogram(image, cornerMask)
            features.extend(hist)

        # 計算橢圓直方圖
        hist = self.histogram(image, ellipMask)
        features.extend(hist)

        # 返回特徵向量
        return features

    # 定義直方圖的功能
    def histogram(self, image, mask):
        # 從遮罩區域中提取顏色直方圖
        hist = cv2.calcHist([image],[0,1,2],mask, self.bins,[0,180,0,256,0,256])
        hist = cv2.normalize(hist,hist).flatten()
        return hist     