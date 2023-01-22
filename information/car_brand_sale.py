#!/usr/bin/python3
import akshare as ak
import sys
car_gasgoo_sale_rank_df = ak.car_gasgoo_sale_rank(symbol="品牌榜", date=str(sys.argv[1]))
print(car_gasgoo_sale_rank_df)
