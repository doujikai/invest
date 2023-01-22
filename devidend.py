#!/usr/bin/python3
#接口: stock_history_dividend_detail

#目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_ShareBonus/stockid/300670.phtml

#描述: 新浪财经-发行与分配-分红配股

#限量: 单次获取指定股票的新浪财经-发行与分配-分红配股详情
import akshare as ak
import sys
import numpy as np
code=str(sys.argv[1])
stock_profile_cninfo_df = ak.stock_profile_cninfo(symbol=code)
for label,item in stock_profile_cninfo_df.items():
    print(label,item[0])

stock_history_dividend_detail_df = ak.stock_history_dividend_detail(symbol=code, indicator="分红")
print(stock_history_dividend_detail_df)
stock_share_change_cninfo_df = ak.stock_share_change_cninfo(symbol=code, start_date="20091227", end_date="20220713")
#stock_share_change_cninfo_df.drop(['机构名称'], axis=1, inplace=True)
for i,row in stock_share_change_cninfo_df.iterrows():
    name=row['证券简称']
    owner=row['控股股东、实际控制人']
    change_date=row['变动日期']
    change_reason=row['变动原因'][0:12]
    total_shares=round(row['总股本']/10000,2)
    outstanding_shares=round(row['已流通股份']/10000,2)
    print("{0} {1} {2} {3} {4:<16}\t总股本:{5} 流通股:{6}".format(code,name,owner,change_date,change_reason,total_shares,outstanding_shares))

