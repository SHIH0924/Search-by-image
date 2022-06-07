"CBIR(Content-Base Image Retrieval)--Search"
import argparse

import cv2

import ColorDescriptor
import Searcher1
import openfile
def Integrate_Search():
    query=openfile.open_file()
    result_path=openfile.open_folder()
    cd = ColorDescriptor.ColorDescriptor((8,12,3))

    # 加載查詢圖像並描述它
    filequery = cv2.imread(query)
    features = cd.describe(filequery)

    # 執行搜索
    searcher = Searcher1.Searcher("1.csv")
    results = searcher.search(features)

    print(results)
    # 顯示要查詢的圖片
    cv2.imshow("Query", filequery)


    # 循環結果
    for(score, resultID) in results:
        # 加載結果圖像並儲存
        print("1.csv"+"/"+resultID)    
        result = cv2.imread(result_path+"/"+resultID)
        cv2.imwrite(str(resultID)+'', result)
    cv2.waitKey(0)
    