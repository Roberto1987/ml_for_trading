from src.ConfigManager import ConfigManager
from src.Tools import load_resource, rolling_mean
import matplotlib.pyplot as plt

config = ConfigManager('..\\src\\config.ini')
df_dict = load_resource(config.source_folder)

# fixing Google dataframe for testing purposes
test_df = df_dict['IBM']

# Possible labels: 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close'
# Fixing label 'Open; for testing purposes
lbl = 'Close'
window = 10

_title = 'Moving average'
x_lbl = 'Date'
y_lbl = 'Rolling avg on a {} day windows'.format(window)

# Using the ratw as comparation
bx = test_df[lbl].plot()

# Retrieving the moving average
moving_mean = rolling_mean(test_df, lbl, window)

ax = moving_mean.plot(title=_title)

ax.set_xlabel(x_lbl)
ax.set_ylabel(y_lbl)
plt.show()
