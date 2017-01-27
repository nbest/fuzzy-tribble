import csv

### Retrieves the latest date in the file (the bottom of the file)

import csv
with open('example.csv', 'rb') as f:
	row_count = sum(1 for row in f)
	f.close()

with open('example.csv','rb') as g:
	mycsv = csv.reader(g)
	mycsv = list(mycsv)
	text = mycsv[row_count-1][0]
print text

#with open('example.csv', 'ab') as file:
#	newdata = ['4','4','4']
#	writer = csv.writer(file)
#	writer.writerow(newdata)
#	file.close()