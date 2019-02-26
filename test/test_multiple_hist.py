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
    if i in ['IBM', 'MSFT']:
        agg_df[i] = daily_returns(agg_df[i])
    else:
        agg_df=agg_df.drop(i,axis=1)

print(agg_df.columns)

# Aggregating two stocks in one DF, they will be plotted in sepaated chats
ax = agg_df.hist(bins=20)
plt.show()

daily_returns(df_dict['IBM']['Open']).hist(bins=20, label='IBM', edgecolor='black')
daily_returns(df_dict['MSFT']['Open']).hist(bins=20, label='MSFT',edgecolor='black')
plt.legend(loc='upper right')

plt.show()