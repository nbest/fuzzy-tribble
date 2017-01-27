import csv
from datetime import datetime, timedelta, date

### Retrieves the latest date in the file (the bottom of the file)

import csv
with open('SPY.csv', 'rb') as f:
	row_count = sum(1 for row in f)
	f.close()

with open('SPY.csv','rb') as g:
	mycsv = csv.reader(g)
	mycsv = list(mycsv)
	text = mycsv[row_count-1][0]
print(text)

### Updates to the next missing day

date = datetime.strptime(text, "%Y-%m-%d")
modified_date = date + timedelta(days=1)
datetime.strftime(modified_date, "%Y-%m-%d")
print(modified_date)
print("BREAK")

### Downloads Quandl data from next missing day to today

if date.today() == modified_date:
	print("same")
else:
	print("different")

#with open('example.csv', 'ab') as file:
#	newdata = ['4','4','4']
#	writer = csv.writer(file)
#	writer.writerow(newdata)
#	file.close()