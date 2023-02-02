#!/usr/bin/python3
import akshare as ak

df = ak.fund_report_stock_cninfo(date="20221231")
for i,row in df.iterrows():
    print( row['股票代码'], row['股票简称'], row['报告期'], row['基金覆盖家数'], row['持股总数'], round(row['持股总市值']/10000,2))
