
import pandas as pd

hist_prc=pd.read_csv("historical_prices.csv")
hist_prc=hist_prc.drop("Unnamed: 0", axis=1)
hist_prc.columns

hist_prc_hi_lo_avg = hist_prc[["SYMBOL", "SERIES", "TIMESTAMP", 'HIGH', 'LOW']]
hist_prc_hi_lo_avg["AVG"] = hist_prc_hi_lo_avg[["HIGH", "LOW"]].mean(axis=1)
hist_prc_hi_lo_avg.columns
hist_prc_hi_lo_avg.head()

hist_prc_drivers = hist_prc[["SYMBOL", "SERIES", "TIMESTAMP",'TOTTRDQTY', 'TOTTRDVAL', 'TOTALTRADES']]
hist_prc_drivers[hist_prc_drivers["SYMBOL"]=="ZUARIGLOB"]
shifted = hist_prc_drivers.groupby("SYMBOL").shift(+1)
len(shifted)
shifted .columns
shifted[shifted["SYMBOL"]=="ZUARIGLOB"]
hist_prc.head()
shifted = hist_prc.groupby(level="SYMBOL").shift(-1)
hist_prc.join(shifted.rename(columns=lambda x: x+"_lag"))
hist_prc.groupby("SYMBOL").mean()
