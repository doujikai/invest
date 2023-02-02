#!/usr/bin/python3
import akshare as ak
import sys

symbol=sys.argv[1]
try:
    df = ak.fund_portfolio_hold_em(symbol, date="2022")
    for i,row in df.iterrows():
        print(row['股票代码'], row['股票名称'], row['占净值比例'], row['持股数'], row['持仓市值'], row['季度'])
except Exception as e :
    print(e)
