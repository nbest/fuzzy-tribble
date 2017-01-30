import csv
from datetime import datetime, timedelta, date
import quandl

quandl.ApiConfig.api_key = 'o8m4zQE4JiyjM4fhU7G4'

# SPY
with open('SPY.csv', 'rb') as f:
	row_count = sum(1 for row in f)
	f.close()

with open('SPY.csv','rb') as g:
	mycsv = csv.reader(g)
	mycsv = list(mycsv)
	text = mycsv[row_count - 1][0]

date = datetime.strptime(text, "%Y-%m-%d").date()
modified_date = date + timedelta(days=1)

if date.today() == modified_date:
	print("No new data")
	sys.exit()
	
else:
	modified_date
	
with open('SPY.csv', 'ab') as file:
	newdata = quandl.get("YAHOO/INDEX_GSPC", start_date = modified_date)
	newdata.to_csv(file, header = False)
	print "%s Success!" % file
	file.close()

# DOW = Dow Jones (Index)
with open('DOW.csv', 'rb') as f:
	row_count = sum(1 for row in f)
	f.close()

with open('DOW.csv','rb') as g:
	mycsv = csv.reader(g)
	mycsv = list(mycsv)
	text = mycsv[row_count - 1][0]

date = datetime.strptime(text, "%Y-%m-%d").date()
modified_date = date + timedelta(days=1)

if date.today() == modified_date:
	print("No new data")
	sys.exit()
	
else:
	modified_date
	
with open('DOW.csv', 'ab') as file:
	newdata = quandl.get("YAHOO/INDEX_DJI", start_date = modified_date)
	newdata.to_csv(file, header = False)
	print "%s Success!" % file
	file.close()

# RUS3 = Russell 3000 (ETF)
with open('RUS3.csv', 'rb') as f:
	row_count = sum(1 for row in f)
	f.close()

with open('RUS3.csv','rb') as g:
	mycsv = csv.reader(g)
	mycsv = list(mycsv)
	text = mycsv[row_count - 1][0]

date = datetime.strptime(text, "%Y-%m-%d").date()
modified_date = date + timedelta(days=1)

if date.today() == modified_date:
	print("No new data")
	sys.exit()
	
else:
	modified_date
	
with open('RUS3.csv', 'ab') as file:
	newdata = quandl.get("GOOG/NYSE_IWV", start_date = modified_date)
	newdata.to_csv(file, header = False)
	print "%s Success!" % file
	file.close()

# EEM = MSCI Emerging Market (ETF)
with open('EEM.csv', 'rb') as f:
	row_count = sum(1 for row in f)
	f.close()

with open('EEM.csv','rb') as g:
	mycsv = csv.reader(g)
	mycsv = list(mycsv)
	text = mycsv[row_count - 1][0]

date = datetime.strptime(text, "%Y-%m-%d").date()
modified_date = date + timedelta(days=1)

if date.today() == modified_date:
	print("No new data")
	sys.exit()
	
else:
	modified_date
	
with open('EEM.csv', 'ab') as file:
	newdata = quandl.get("GOOG/NYSEARCA_EEM", start_date = modified_date)
	newdata.to_csv(file, header = False)
	print "%s Success!" % file
	file.close()

# EFA = MSCI EAFE (ETF)
with open('EFA.csv', 'rb') as f:
	row_count = sum(1 for row in f)
	f.close()

with open('EFA.csv','rb') as g:
	mycsv = csv.reader(g)
	mycsv = list(mycsv)
	text = mycsv[row_count - 1][0]

date = datetime.strptime(text, "%Y-%m-%d").date()
modified_date = date + timedelta(days=1)

if date.today() == modified_date:
	print("No new data")
	sys.exit()
	
else:
	modified_date
	
with open('EFA.csv', 'ab') as file:
	newdata = quandl.get("GOOG/NYSE_EFA", start_date = modified_date)
	newdata.to_csv(file, header = False)
	print "%s Success!" % file
	file.close()

# ICF = iShares Cohen & Steers (ETF)
with open('ICF.csv', 'rb') as f:
	row_count = sum(1 for row in f)
	f.close()

with open('ICF.csv','rb') as g:
	mycsv = csv.reader(g)
	mycsv = list(mycsv)
	text = mycsv[row_count - 1][0]

date = datetime.strptime(text, "%Y-%m-%d").date()
modified_date = date + timedelta(days=1)

if date.today() == modified_date:
	print("No new data")
	sys.exit()
	
else:
	modified_date
	
with open('ICF.csv', 'ab') as file:
	newdata = quandl.get("GOOG/NYSEARCA_ICF", start_date = modified_date)
	newdata.to_csv(file, header = False)
	print "%s Success!" % file
	file.close()