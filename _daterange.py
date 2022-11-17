# Monthly
import pandas as pd

# returns last date of the month
d = pd.date_range('2022-01-01',periods=10,freq='M')

# returns first date of the month
d1 = pd.date_range('2022-01-01',periods=10,freq='MS')