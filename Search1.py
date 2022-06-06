"CBIR(Content-Base Image Retrieval)--Search"
import argparse

import cv2

import ColorDescriptor
import Searcher

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required=True, help="Path to where the computed index will be stored")

ap.add_argument("-q", "--query", required=True, help="Path to query image")
ap.add_argument("-r", "--result_path", required = True, help="Path to the result Path")
args = vars(ap.parse_args())
cd = ColorDescriptor.ColorDescriptor((8,12,3))

# load the query image and describe it
query = cv2.imread(args["query"])
features = cd.describe(query)

# perform the search
searcher = Searcher.Searcher(args["index"])
results = searcher.search(features)


# display the query
cv2.imshow("Query", query)


# loop over the results
for(score, resultID) in results:
    # load the result image and display it
    print(args["index"]+"/"+resultID)    
    result = cv2.imread(args["result_path"]+"/"+resultID)  
    cv2.imwrite(str(resultID)+'', result)
    cv2.waitKey(0)