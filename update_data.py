import csv
from datetime import datetime, timedelta, date
import quandl

quandl.ApiConfig.api_key = '{key}'

### Retrieves the latest date in the file (the bottom of the file)

with open('SPY.csv', 'rb') as f:
	row_count = sum(1 for row in f)
	f.close()
#print("# of rows:", row_count)

with open('SPY.csv','rb') as g:
	mycsv = csv.reader(g)
	mycsv = list(mycsv)
	text = mycsv[row_count - 1][0]
#print("Most recent data:", text)

### Updates to the next missing day

date = datetime.strptime(text, "%Y-%m-%d").date()
#print "Datetime object today", date
modified_date = date + timedelta(days=1)
#print "Next date in series:", modified_date
#print "Today is:", date.today()

### Downloads Quandl data from next missing day to yesterday
### Given the 1 day data feed lag, if the newest date is today
### the program ends as there is no new data

if date.today() == modified_date:
	print("No new data")
	sys.exit()
	
else:
	modified_date
	
with open('SPY.csv', 'ab') as file:
	newdata = quandl.get("YAHOO/INDEX_GSPC", start_date = modified_date)
	#print newdata
	newdata.to_csv(file, header = False)
	file.close()
