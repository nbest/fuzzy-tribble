#import quandl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
import datetime
import scipy.optimize as scopt
import os
import glob

### Lists the CSV files available at the path below
### Removes the '.csv' ending and assigns new_name

path = 'C:\\Users\\nbest\\Documents\\_Python\\data\\'
extension = 'csv'
os.chdir(path)
result = [i for i in glob.glob('*.{}'.format(extension))]
new_name = []

for items in result:
	new_name.append(items[:-4])

### Opens each csv and retrieves the date and close price column
### Names each variable the name of the csv

st = "2007-01-01"
en = "2017-01-20"

for items in new_name:
	exec("%s = pd.read_csv(%r'.csv', index_col = 0, usecols = ['Date','Close'])" % (items, items))
	exec("%s_pct_change = %s.pct_change()" % (items, items))
	exec("%s_conformed = %s[st:en]" % (items, items))
	exec("%s_close = %s_conformed['Close']" % (items, items))

"""Although exec() functions are to be avoided, here they make the process dynamic.
To recap, the four exec() functions above have created four dynamic variables
for each csv file, as outlined below"""

### There are 6 csv files, and 4 dynamic variables per csv
### SPY -> df with all historical index data
### SPY_pct_change -> daily % movements for each index
### SPY_conformed -> conforms all index variables to same length of time
###		per the variables st (start date) and en (end date)
### SPY_close -> df containing only the daily close column for each index
###		in the defined time length (st, en)

master_list = pd.concat([DOW_conformed, EEM_conformed, EFA_conformed, ICF_conformed, 
				RUS3_conformed, SPY_conformed], axis=1)
master_list.columns = new_name

master_list_pct_change = master_list.pct_change()

### master_list -> df aggregating all daily return data for 
### the various indices in one variable

def create_portfolio(holdings, weights = None):
	if weights is None:
		shares = np.ones(len(holdings))/len(tickers)
	portfolio = pd.DataFrame({'Tickers': holdings,
								'Weights': weights},
								index = holdings)
	return portfolio

current = ['DOW', 'EEM', 'EFA', 'ICF', 'RUS3', 'SPY']
allocation = [0.15, 0.1, 0.1, 0.15, 0.2, 0.2]
	
portfolio = create_portfolio(current, allocation)	

def calculate_weighted_portfolio_value(portfolio, returns, name = 'Value'):
	total_weights = portfolio.Weights.sum()
	weighted_returns = returns * (portfolio.Weights / total_weights)
	return pd.DataFrame({name: weighted_returns.sum(axis=1)})

### Now, wr = portfolio weighted return, according to the allocation (line 65)
	
wr = calculate_weighted_portfolio_value(portfolio, master_list_pct_change, "Value")

with_value = pd.concat([master_list_pct_change, wr], axis = 1)

def plot_portfolio_returns(returns, title = None):
	returns.plot(figsize=(12,8))
	plt.xlabel('Year')
	plt.ylabel('Returns')
	if title is not None: plt.title(title)
	plt.show()
	
print wr
wr2 = (1+wr.Value).cumprod()-1
print wr2
plot_portfolio_returns(wr2)