import pandas as pd


x = "7,18,19,20"
y = "8,9,10,22"

df = pd.DataFrame([x,y],columns=['A'])

df.A.str.get_dummies(sep=',')