#!/bin/bash
cat  ../code.txt|while read line 
do
				./stock_mda_ym.py $line > tmp.txt
				cat tmp.txt|grep -E '^.{8,15}2019中期' >> 2019H.txt
				cat tmp.txt|grep -E '^.{8,15}2019年度' >> 2019Y.txt
				cat tmp.txt|grep -E '^.{8,15}2020中期' >> 2020H.txt
				cat tmp.txt|grep -E '^.{8,15}2020年度' >> 2020Y.txt
				cat tmp.txt|grep -E '^.{8,15}2021中期' >> 2021H.txt
				cat tmp.txt|grep -E '^.{8,15}2021年度' >> 2021Y.txt
				cat tmp.txt|grep -E '^.{8,15}2022中期' >> 2022H.txt
done
