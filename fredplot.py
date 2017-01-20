from matplotlib import pyplot as plt
from fredapi import Fred

display = raw_input("What would you like to display? >> ")

fred = Fred(api_key = "bf4553bb81babdaf14c46693d57579c1")
SPY = fred.get_series(display)

plt.plot(SPY)
plt.title(display)
plt.show()