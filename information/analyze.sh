#!/bin/bash
./cctv_news.py 20221128
./car_brand_sale.py 202210
begin_day=-364
end_day=0
for((i=${begin_day};i<=${end_day};i++));
do
				day=`date -d "${i} days" +"%Y%m%d"`
				./cctv_news.py  ${day} |sed -E "s/^\b/${day} /">> 2022.txt 
done
