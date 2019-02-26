from src.ConfigManager import ConfigManager
from src.Tools import load_resource, drop_volume, multistock, daily_returns
import matplotlib.pyplot as plt
import numpy as np

config = ConfigManager('..\\src\\config.ini')

# LOAD CSVs, return a dict with name
df_dict = load_resource(config.source_folder)

drop_volume(df_dict)
print('Labels : {}'.format(list(df_dict['GOOG'].columns)))
agg_df = multistock(df_dict, 'Close')
for i in list(agg_df.columns):
    agg_df[i] = daily_returns(agg_df[i])

print(agg_df.columns)

lbl_1, lbl_2, lbl_3 = 'MSFT', 'IBM', 'GOOG'

ax = agg_df.plot(kind='scatter', x=lbl_1, y=lbl_2)

beta_1, alpha_1 = np.polyfit(agg_df[lbl_1], agg_df[lbl_2], 1)
beta_2, alpha_2 = np.polyfit(agg_df[lbl_1], agg_df[lbl_3], 1)
plt.plot(agg_df[lbl_1], beta_1 * agg_df[lbl_1] + alpha_1, '-', color ='r')

print('BETA {}-{} : {} '.format(lbl_1,lbl_2, beta_1))
print('ALFA {}-{} : {}'.format(lbl_1, lbl_2,alpha_1))
print('====================================')
print('BETA {}-{} : {} '.format(lbl_1, lbl_3,beta_2))
print('ALFA {}-{} : {}'.format(lbl_1,lbl_3 ,alpha_2))

print(agg_df.corr(method='pearson'))
plt.show()


ax = agg_df.plot(kind='scatter', x=lbl_2, y=lbl_1)
plt.plot(agg_df[lbl_1], beta_2 * agg_df[lbl_1] + alpha_2, '-', color ='r')

plt.show()