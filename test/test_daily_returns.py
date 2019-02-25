from src.ConfigManager import ConfigManager
from src.Tools import load_resource, daily_returns
import matplotlib.pyplot as plt



config = ConfigManager('..\\src\\config.ini')
df_dict = load_resource(config.source_folder)

# fixing Google dataframe for testing purposes

test_df = df_dict['IBM']

# Possible labels: 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close'
# Fixing label 'Open; for testing purposes
lbl = 'Close'

_title = 'Daily Returns'
x_lbl='Date'
y_lbl='Daily return'

day_rets = daily_returns(test_df[lbl])

ax = day_rets.plot(title=_title)

ax.set_xlabel(x_lbl)
ax.set_ylabel(y_lbl)
plt.show()