"""Sources:
https://www.quandl.com/data/GOOG-Google-Finance
https://www.quandl.com/data/FRED-Federal-Reserve-Economic-Data
"""

import quandl
import datetime

quandl.ApiConfig.api_key = 'o8m4zQE4JiyjM4fhU7G4'

### Downloads historical data from quandl

#start = datetime.date(2000,1,1)
end = datetime.date(2017,1,20)

# SPY = S&P 500 (Index)
SPY = quandl.get("YAHOO/INDEX_GSPC", end_date = end)
SPY.to_csv('SPY.csv')

# DOW = Dow Jones (Index)
DOW = quandl.get("YAHOO/INDEX_DJI", end_date = end)
DOW.to_csv('DOW.csv')

# RUS3 = Russell 3000 (ETF)
RUS3 = quandl.get("GOOG/NYSE_IWV", end_date = end)
RUS3.to_csv('RUS3.csv')

# EEM = MSCI Emerging Market (ETF)
EEM = quandl.get("GOOG/NYSEARCA_EEM", end_date = end)
EEM.to_csv('EEM.csv')

# EFA = MSCI EAFE (ETF)
EFA = quandl.get("GOOG/NYSE_EFA", end_date = end)
EFA.to_csv('EFA.csv')

# ICF = iShares Cohen & Steers (ETF)
ICF = quandl.get("GOOG/NYSEARCA_ICF", end_date = end)
ICF.to_csv('ICF.csv')