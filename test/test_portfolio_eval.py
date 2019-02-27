import matplotlib.pyplot as plt

from src.ConfigManager import ConfigManager
from src.Tools import load_resource, drop_volume, multistock, daily_returns, portfolio_eval, cumulative_returns, sharp_ratio

config = ConfigManager('..\\src\\config.ini')

yearly = 252
weekly = 52
monthly = 12

# LOAD CSVs, return a dict with name
df_dict = load_resource(config.source_folder)

drop_volume(df_dict)
print('Labels : {}'.format(list(df_dict['GOOG'].columns)))
agg_df = multistock(df_dict, 'Close')
portfolio = portfolio_eval(agg_df, [.5,.0,.5,.0],  normalize=True)

cum_ret = cumulative_returns(portfolio)

#portfolio = daily_returns(portfolio)

sr = sharp_ratio(portfolio,yearly)
portfolio.plot()
print('Sharp ratio: {}, Cumulative returns: {}'.format(sr, cum_ret))

plt.legend(loc=1)
plt.show()