from src.ConfigManager import ConfigManager
from src.Tools import load_resource, rolling_mean, rolling_std, bollinger_bands, backfill_data
import matplotlib.pyplot as plt

config = ConfigManager('..\\src\\config.ini')
df_dict = load_resource(config.source_folder)

# fixing Google dataframe for testing purposes
test_df = df_dict['IBM']

# Possible labels: 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close'
# Fixing label 'Open; for testing purposes
lbl = 'Close'
window = 10

_title = 'Bollinger Bands'
x_lbl = 'Date'
y_lbl = 'Price'.format(window)

moving_mean = backfill_data(rolling_mean(test_df, lbl, window))
moving_std = backfill_data(rolling_std(test_df, lbl, window))
print(moving_std)
up,down = bollinger_bands(moving_mean, moving_std)

up.plot(),down.plot()
ax = moving_mean.plot(title=_title)

ax.set_xlabel(x_lbl)
ax.set_ylabel(y_lbl)
plt.show()
