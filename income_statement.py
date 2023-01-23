#!/usr/bin/python3
#接口: stock_lrb_em

#目标地址: http://data.eastmoney.com/bbsj/202003/lrb.html

#描述: 东方财富-数据中心-年报季报-业绩快报-利润表

#限量: 单次获取指定 date 的利润表数据
import akshare as ak
import sys



stock_lrb_em_df = ak.stock_lrb_em(date=str(sys.argv[1]))
#format_dict={"净利润同比":"{:.2%}"}
#stock_lrb_em_df.style.format(format_dict)
stock_lrb_em_df=stock_lrb_em_df.sort_values(by=['净利润'],ascending=[False])
for i,row in stock_lrb_em_df.iterrows():
        code=row['股票代码']
        name=row['股票简称']
        revenue=round(row['营业总收入']/100000000,2)
        revenue_grow=str(round(row['营业总收入同比'],2))+"%"
        net_profit=round(row['净利润']/100000000,2)
        net_profit_grow=str(round(row['净利润同比'],2))+"%"
        #report_date=str(row['公告日期'])
        report_date=str(sys.argv[1])
        print("公告日期:{6:<10} {0}  收入:{2:<12} 收入同比{3:<10} 净利润:{4:<10} 净利润同比:{5:<12} {1}".format(code,name,revenue,revenue_grow,net_profit,net_profit_grow,report_date))
