import pandas as pd
import datetime
data = pd.read_pickle('sampleData.pickle')

# Iterrate over the length of the data
for _ in range(len(data)):
    for i in data.index:
        data.at[i,'EndTime'] = data.at[i,'time'] + datetime.timedelta(hours=int(data.at[i,'settings_allocatedTime']))