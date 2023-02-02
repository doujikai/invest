#!/bin/bash
cat name.txt | grep 混合型-偏股|grep -v [ABCDE]|grep -v 后端|while read line
#cat name.txt | grep 混合型-偏股|grep A|while read line
do
				code=$(echo $line|awk '{print $1}')
				name=$(echo $line|awk '{print $3}')
				./fund_portfolio_hold.py $code|awk  '{printf "%-7s %-14s\t净值比例:%-6s 股数:%-10s 市值:%-8s %s\n", $1,$2,$3,$4,$5/10000,$6}'|sed "s/^/$code $name /"
done
