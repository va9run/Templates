import pandas as pd
import datetime

x = pd.read_pickle('sampleData.pickle')
x['TimeList'] = pd.np.empty((len(x), 0)).tolist()

# Iterate over rows
for i, row in x.iterrows():
    min_time = row['time1']
    max_time = row['EndTime1']
# create a increament time using start and end time and save it to list 
    for s in range(min_time,max_time,1):
        row['TimeList'].append(s)