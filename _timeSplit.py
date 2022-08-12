import datetime
x = '10:00:00'
# time split
x[['h','m','s']] = x['time'].str.split(':',expand=True)

# Convert it to total Seconds
for i in x.index:
    x.at[i,'time1'] = (int(datetime.timedelta(hours=int(x.at[i,'h']),minutes=int(x.at[i,'m']),seconds=int(x.at[i,'s'])).total_seconds()))