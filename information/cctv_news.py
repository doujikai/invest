#!/usr/bin/python3
import akshare as ak
import sys
news_cctv_df = ak.news_cctv(date=str(sys.argv[1]))
for i,row in news_cctv_df.iterrows():
    print(i,row['title'],row['content'],"\n")
