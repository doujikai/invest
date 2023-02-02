#!/usr/bin/python3
import akshare as ak
import sys
code=str(sys.argv[1])
name=str(sys.argv[2])
stock_mda_ym_df = ak.stock_mda_ym(symbol=code)
for i,row in stock_mda_ym_df.iterrows():
    report_date=row['报告期']
    content=row['内容']
    print(code,name,report_date,content,"\n")
