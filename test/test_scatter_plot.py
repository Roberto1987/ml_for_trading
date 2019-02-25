from src.ConfigManager import ConfigManager
from src.Tools import load_resource, drop_volume, multistock, daily_returns
import matplotlib.pyplot as plt

config = ConfigManager('..\\src\\config.ini')

# LOAD CSVs, return a dict with name
df_dict = load_resource(config.source_folder)

drop_volume(df_dict)
print('Labels : {}'.format(list(df_dict['GOOG'].columns)))
agg_df = multistock(df_dict, 'Close')
for i in list(agg_df.columns):
        agg_df[i] = daily_returns(agg_df[i])

print(agg_df.columns)

ax = agg_df.plot(kind='scatter', x='MSFT', y='GOOG')
bx = agg_df.plot(kind='scatter', x='MSFT', y='IBM')
plt.show()
