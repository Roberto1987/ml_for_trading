from src.ConfigManager import ConfigManager
from src.Tools import load_resource, rolling_std
import matplotlib.pyplot as plt

config = ConfigManager('..\\src\\config.ini')
df_dict = load_resource(config.source_folder)

# fixing Google dataframe for testing purposes
test_df = df_dict['IBM']

# Possible labels: 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close'
# Fixing label 'Open; for testing purposes
lbl = 'Close'
window=5

_title = 'Moving std'
x_lbl='Date'
y_lbl='Std avg on a {} day windows'.format(window)

# Retrieving the rolling standard deviation
moving_std = rolling_std(test_df, lbl, window)

ax = moving_std.plot(title=_title)

ax.set_xlabel(x_lbl)
ax.set_ylabel(y_lbl)
plt.show()