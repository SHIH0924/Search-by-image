# Search by image(已圖搜圖)
## 期末作業一共有六個檔案
這六個檔案分別為**ColorDescriptor.py、index.py、Integrate.py、openfile.py、Search1.py**及**Searcher1.py**
* Integrate.py  
	將函式整合起來，並用tkinter來輸出操做介面。  
* ColorDescriptor.py  
	計算影像中不同區域的 3D HSV 顏色直方圖，使用基於區域的直方圖，這樣可以模擬各個區域的顏色分佈。  
* index.py  
	對資料集中的每幅影像提取特徵，並將其持久儲存起來，對於每幅影像，可以提取一個 imageID，即影像的檔名，這個作為示例的搜尋引擎，也可以針對每幅影產出一個 UUID，最後將其存為 csv 檔，並在當前資料夾下儲存為 index。  
* Searcher1.py  
	比較這些特徵，獲取相似度，由於比較的是顏色的直方圖，根據概率分佈的定義，選用皮爾森的卡方測試統計,用來比較離散概率分佈。  
* Search1.py  
	選擇要搜尋的影像後，該影像將與資料集中的每幅影像進行比較，目標是找到資料集中與待搜尋影像相似的影像，依相似度高到低輸出檔名後，並將其存起來。  
 
