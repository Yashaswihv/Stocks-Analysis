
import pandas as pd
import os
import matplotlib.pyplot as plt
print(os.getcwd())
hist_prc=pd.read_csv("./Stocks-Analysis/historical_prices.csv")
hist_prc.columns
hist_prc = hist_prc[['SYMBOL', 'SERIES', 'TIMESTAMP', 'HIGH', 'LOW',
                     'TOTTRDQTY', 'TOTTRDVAL', 'TOTALTRADES']]

hist_prc.columns
hist_prc["TIMESTAMP"] = pd.to_datetime(hist_prc["TIMESTAMP"])
hist_prc = hist_prc.sort_values(by=["SYMBOL", "SERIES", "TIMESTAMP"])
hist_prc["AVG"] = hist_prc[["HIGH", "LOW"]].mean(axis=1)
hist_prc["QTY_PER_TRADE"] = hist_prc["TOTTRDQTY"]/hist_prc["TOTALTRADES"]
hist_prc["VAL_PER_TRADE"] = hist_prc["TOTTRDVAL"]/hist_prc["TOTALTRADES"]

shifted = hist_prc.groupby("SYMBOL").shift(+1)
hist_prc = hist_prc.join(shifted.rename(columns=lambda x:
x+"_LAG"))
shifted_1 = hist_prc[['SYMBOL', 'TOTTRDQTY', 'TOTTRDVAL','TOTALTRADES',
                      'QTY_PER_TRADE', 'VAL_PER_TRADE']].groupby(
    'SYMBOL').shift(+2)
hist_prc = hist_prc.join(shifted_1.rename(columns=lambda x:
x+"_LAG2"))

hist_prc["DAYS_FROM_LAST_TRADE"] = hist_prc['TIMESTAMP'] - hist_prc[
    'TIMESTAMP_LAG']
hist_prc["TOTTRDQTY_DIFF"] = abs((hist_prc['TOTTRDQTY_LAG']-hist_prc[
    'TOTTRDQTY_LAG2'])/hist_prc['TOTTRDQTY_LAG2'])
hist_prc["TOTTRDVAL_DIFF"] = abs((hist_prc['TOTTRDVAL_LAG']-hist_prc[
    'TOTTRDVAL_LAG2'])/hist_prc['TOTTRDVAL_LAG2'])
hist_prc["TOTALTRADES_DIFF"] = abs((hist_prc['TOTALTRADES_LAG']-hist_prc[
    'TOTALTRADES_LAG2'])/hist_prc['TOTALTRADES_LAG2'])
hist_prc["QTY_PER_TRADE_DIFF"] = (hist_prc['QTY_PER_TRADE_LAG']-hist_prc[
    'QTY_PER_TRADE_LAG2'])/hist_prc['QTY_PER_TRADE_LAG2']
hist_prc["VAL_PER_TRADE_DIFF"] = abs((hist_prc['VAL_PER_TRADE_LAG']-hist_prc[
    'VAL_PER_TRADE_LAG2'])/hist_prc['VAL_PER_TRADE_LAG2'])
hist_prc["AVG_DIFF"] = (hist_prc['AVG']-hist_prc[
    'AVG_LAG'])/hist_prc['AVG_LAG']

x=hist_prc["QTY_PER_TRADE_DIFF"].loc[(abs(hist_prc["AVG_DIFF"])<0.06) & (
        abs(hist_prc["QTY_PER_TRADE_DIFF"]<0.1))]
y=hist_prc["AVG_DIFF"].loc[(abs(hist_prc["AVG_DIFF"])<0.06) & (
        abs(hist_prc["QTY_PER_TRADE_DIFF"]<0.1))]
plt.scatter(x,y)


x=hist_prc["TOTTRDQTY_DIFF"].loc[(abs(hist_prc["AVG_DIFF"])<0.06) & (
        abs(hist_prc["TOTTRDQTY_DIFF"]<0.06))]
y=hist_prc["AVG_DIFF"].loc[(abs(hist_prc["AVG_DIFF"])<0.06) & (
        abs(hist_prc["TOTTRDQTY_DIFF"]<0.06))]
plt.scatter(x,y)

len(x)
