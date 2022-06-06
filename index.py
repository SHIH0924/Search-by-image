"CBIR(Content-Base Image Retrieval)--Extract Features and Indexing"
import ColorDescriptor
import argparse
import glob
import cv2
import numpy as np
from tkinter import filedialog
import tkinter as tk
def open_file():                            # 開檔函式
    root = tk.Tk()
    root.withdraw()
    sfname = filedialog.askopenfilename(title='選擇要開啟的檔案',
        # 開起對話框，對話框名稱
                                            filetypes=[# 文件能選擇的類型
                                                ('All Files','*'),
                                                ("jpeg files","*.jpg"),
                                                ("png files","*.png"),
                                                ("gif files","*.gif")])
    return sfname

def open_folder():                            # 開啟資料夾
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askdirectory()                                      
        return file_path

#ap = argparse.ArgumentParser()
#ap.add_argument("-d", "--dataset", required=True, help="Path to the directory that cntains the images to be indexed")
#ap.add_argument("-i", "--index", required=True, help="Path to where the computed index will be stored")
#args = vars(ap.parse_args())
#print(args)
cd = ColorDescriptor.ColorDescriptor((8,12,3))
dataset=open_folder()
#Open the output index file for writing
output = open("1.csv","w")

# use glob to grab the image paths and loop over them
for imagePath in glob.glob(dataset+"/*.jpg"):
    # extract the image ID from the image
    imageID = imagePath[imagePath.rfind("\\")+1:]
    image = cv2.imread(imagePath)

    # describe the image
    features = cd.describe(image)

    # write feature to file
    features = [str(f) for f in features]
    output.write("%s,%s\n" %(imageID,",".join(features)))
# close index file
output.close()