import matplotlib.pyplot as plt

from src.ConfigManager import ConfigManager
from src.Tools import load_resource, drop_volume, multistock, daily_returns, portfolio_eval, cumulative_returns, \
    sharp_ratio, portfolio_estimation, stochastic_sum, stochastic_sum_constraint
import scipy.optimize as opt
import numpy as np

config = ConfigManager('..\\src\\config.ini')

# LOAD CSVs, return a dict with name
df_dict = load_resource(config.source_folder)

drop_volume(df_dict)
agg_df = multistock(df_dict, 'High')

x0 = np.array([0, 0, 1, 0])
initial_guess = []

min_result = opt.minimize(
    portfolio_estimation,
    [.25, .25, .25, .25],
    args=agg_df,
    method='SLSQP',
    options={'disp': True},
    bounds = ((0.0, 1.0),(0.0, 1.0),(0.0, 1.0),(0.0, 1.0)),
    constraints=({'type':'eq', 'fun': stochastic_sum_constraint})
)
print(min_result.x)
print(sum(list(min_result.x)))
