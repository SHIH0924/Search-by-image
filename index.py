"CBIR(Content-Base Image Retrieval)--Extract Features and Indexing"
import ColorDescriptor
import glob
import cv2
import openfile

def Integrate_Index():
    cd = ColorDescriptor.ColorDescriptor((8,12,3))
    dataset=openfile.open_folder()
    # 打開輸出索引文件進行寫入
    output = open("1.csv","w")

    # 使用 glob 抓取圖像路徑並循環
    for imagePath in glob.glob(dataset+"/*.jpg"):
        # extract the image ID from the image
        imageID = imagePath[imagePath.rfind("\\")+1:]
        image = cv2.imread(imagePath)

        # 描述圖像
        features = cd.describe(image)

        # 將特徵寫入文件
        features = [str(f) for f in features]
        output.write("%s,%s\n" %(imageID,",".join(features)))
    # 關閉索引文件
    output.close()