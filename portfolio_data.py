import quandl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
import datetime
import scipy.optimize as scopt
import os
import glob

# Lists the CSV files available at the path below
# Removes the '.csv' ending and assigns new_name

path = 'C:\\Users\\nbest\\Documents\\_Python\\data\\'
extension = 'csv'
os.chdir(path)
result = [i for i in glob.glob('*.{}'.format(extension))]
new_name = []

for items in result:
	new_name.append(items[:-4])

docs = new_name

# Opens each csv and retrieves the date and close price column
# Names each variable the name of the csv
	
for items in docs:
	exec("%s = pd.read_csv(%r'.csv', index_col = 0, usecols = ['Date','Close'])" % (items, items))
	exec("%s_pct_change = %s.pct_change()" % (items, items))

def plot_portfolio_returns(returns, title = None):
	returns.plot(figsize=(12,8))
	plt.xlabel('Year')
	plt.ylabel('Returns')
	if title is not None: plt.title(title)
	plt.show()