from matplotlib import pyplot as plt
from fredapi import Fred

display = raw_input("What would you like to display? >> ")

fred = Fred(api_key = "api")
SPY = fred.get_series(display)

plt.plot(SPY)
plt.title(display)
plt.show()
