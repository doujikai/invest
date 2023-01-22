#!/usr/bin/python3
#接口: stock_mda_ym

#目标地址: http://f10.emoney.cn/f10/zbyz/1000001

#描述: 益盟-F10-管理层讨论与分析

#限量: 单次返回所有历史数据
#主营构成
import akshare as ak
import sys
code=str(sys.argv[1])
stock_zygc_ym_df = ak.stock_zygc_ym(symbol=code)
#stock_zygc_ym_df=stock_zygc_ym_df.sort_values(by=['分类方向'],ascending=[False])
for i, row in stock_zygc_ym_df.iterrows():
        group_type = row['分类方向'];
        report_date = row['报告期'];
        fenlei = row['分类']
        revenue=row['营业收入']
        revenue_grow=row['营业收入-同比增长']
        revenue_proportion=row['营业收入-占主营收入比']
        cost=row['营业成本']
        if '--'  in cost or '--' in revenue:
            gross_profit='--'
        else:
            gross_profit=str(round(float(revenue.replace("亿",""))-float(cost.replace("亿","")),2))
        gross_profit_rate=row['毛利率']
        gross_profit_grow=row['毛利率-同比增长']
        print("{10}  {0} {1} 收入:{3:<12} 收入增长{4:<10} 收入占比:{5:<10} 营业成本:{6:<8}\t毛利润:{9:<8}\t毛利率:{7:<10} 毛利率-同比:{8:<10} 业务:{2} ".format(report_date,group_type,fenlei,revenue,revenue_grow,revenue_proportion,cost,gross_profit_rate,gross_profit_grow,gross_profit,code))
