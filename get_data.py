import quandl
import datetime

quandl.ApiConfig.api_key = '{key}'

### Downloads historical data from quandl

start = datetime.date(2013,1,1)
end = datetime.date(2017,1,23)

SPY = quandl.get("YAHOO/INDEX_GSPC", start_date = start, end_date = end)
#SPY_pct_change = SPY.pct_change()

#print(SPY_pct_change)

# set file path and name

SPY.to_csv('SPY.csv')
