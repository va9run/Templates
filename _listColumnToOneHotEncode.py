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

# Column was in list type first convert it to normal column without list
x['TimeList'] = [','.join(map(str,l)) for l in x['TimeList']]
#Then make those objects to column names as one hot encooder
x = pd.concat([x,x.TimeList.str.get_dummies(sep=',')],1)