import matplotlib.pyplot as plt

from src.ConfigManager import ConfigManager
from src.Tools import load_resource, drop_volume, multistock, daily_returns, rolling_mean, bollinger_bands


config = ConfigManager('config.ini')

# LOAD CSVs, return a dict with name
df_dict = load_resource(config.source_folder)

drop_volume(df_dict)
print('Labels : {}'.format(list(df_dict['GOOG'].columns)))
agg_df = multistock(df_dict, 'Close')
for i in list(agg_df.columns):
    if i in ['IBM', 'MSFT']:
        agg_df[i] = daily_returns(agg_df[i])
    else:
        agg_df=agg_df.drop(i,axis=1)

print(agg_df.columns)
agg_df.plot()
plt.show()



