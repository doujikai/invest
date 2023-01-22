#!/usr/bin/python3
import akshare as ak
import pandas as pd

energy_oil_hist_df = ak.energy_oil_hist()
pd.set_option("display.max_rows",None)
print(energy_oil_hist_df)
