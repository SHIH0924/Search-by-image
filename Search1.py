"CBIR(Content-Base Image Retrieval)--Search"
import argparse

import cv2

import ColorDescriptor
import Searcher1
import openfile

query=openfile.open_file()
result_path=openfile.open_folder()
cd = ColorDescriptor.ColorDescriptor((8,12,3))

# load the query image and describe it
filequery = cv2.imread(query)
features = cd.describe(filequery)

# perform the search
searcher = Searcher1.Searcher("1.csv")
results = searcher.search(features)


# display the query
cv2.imshow("Query", filequery)


# loop over the results
for(score, resultID) in results:
    # load the result image and display it
    print("1.csv"+"/"+resultID)    
    result = cv2.imread(result_path+"/"+resultID)  
    cv2.imwrite(str(resultID)+'', result)
    cv2.waitKey(0)