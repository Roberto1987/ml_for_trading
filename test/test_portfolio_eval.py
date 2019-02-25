import matplotlib.pyplot as plt

from src.ConfigManager import ConfigManager
from src.Tools import load_resource, drop_volume, multistock, daily_returns, rolling_mean, bollinger_bands, \
    portfolio_eval

config = ConfigManager('..\\src\\config.ini')

# LOAD CSVs, return a dict with name
df_dict = load_resource(config.source_folder)

drop_volume(df_dict)
print('Labels : {}'.format(list(df_dict['GOOG'].columns)))
agg_df = multistock(df_dict, 'Close')

portfolio = portfolio_eval(agg_df, [.01,.01,.01,.99], 100000)
portfolio.plot()
plt.show()