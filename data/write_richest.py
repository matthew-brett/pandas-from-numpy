# Process gender data to 15 richest countries

import numpy as np
import pandas as pd

df = pd.read_csv('gender_stats.csv')
df = df.set_index('country_code')
top_15 = df.dropna().sort_values('gdp_us_billion').tail(15).sort_index()
top_15.reset_index().to_csv('richest_stats.csv', index=None)
