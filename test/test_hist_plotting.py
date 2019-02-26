from src.ConfigManager import ConfigManager
from src.Tools import load_resource, daily_returns
import matplotlib.pyplot as plt

# PLOT AN HISTOGRAM WITH MEAN AND STD DEV

config = ConfigManager('..\\src\\config.ini')
df_dict = load_resource(config.source_folder)

# fixing Google dataframe for testing purposes

print(type(df_dict['IBM']))

test_df = df_dict['IBM']
# Possible labels: 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close'
# Fixing label 'Open; for testing purposes
lbl = 'Close'

_title = 'Daily Returns'
x_lbl = 'Date'
y_lbl = 'Daily return'

day_rets = daily_returns(test_df[lbl])
ax = day_rets.hist(bins=40, edgecolor='b')

ax.set_xlabel(x_lbl)
ax.set_ylabel(y_lbl)

mean = day_rets.mean()
std = day_rets.std()
kurtosis = day_rets.kurtosis()

print('Kurtosis : {} ; if positive, it says that this distributions has "Fat" tails'.format(kurtosis))

# Mean
plt.axvline(mean, color='k', linestyle='dashed', linewidth=2)

# STD interval

plt.axvline(std, color='r', linestyle='dashed', linewidth=1.5)
plt.axvline(-std, color='r', linestyle='dashed', linewidth=1.5)

plt.show()
