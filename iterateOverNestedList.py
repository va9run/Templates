x = [['a','b','c'],'d',['e','f']]
y = ['G','H','I']

for i in x:
    print(i)
    for j in i:
        print(j)

for i,j in zip(x,y):
    for g in i:
        print(g,j)
