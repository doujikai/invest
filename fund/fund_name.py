#!/usr/bin/python3
import akshare as ak

df = ak.fund_name_em()
for i,row in df.iterrows():
    print(row['基金代码'], row['基金类型'], row['基金简称'])
