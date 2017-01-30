"""Sources:
https://www.quandl.com/data/GOOG-Google-Finance
https://www.quandl.com/data/FRED-Federal-Reserve-Economic-Data
"""

import quandl
import datetime

quandl.ApiConfig.api_key = 'o8m4zQE4JiyjM4fhU7G4'

### Downloads historical data from quandl

end = datetime.date(2017,1,20)

data = {'SPY':"YAHOO/INDEX_GSPC", 'DOW': "YAHOO/INDEX_DJI", 'RUS3': "GOOG/NYSE_IWV", 
		"EEM": "GOOG/NYSEARCA_EEM", "EFA": "GOOG/NYSE_EFA", "ICF": "GOOG/NYSEARCA_ICF"}

for items in data:
	exec("%s = quandl.get('%s', end_date = end)" % (items, data[items]))
	exec("%s.to_csv('%s.csv')" % (items, items))