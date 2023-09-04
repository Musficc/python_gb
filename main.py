import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

def to_onehot(data1):
    def get_unique(data1):
        unique_List = pd.DataFrame(data1).drop_duplicates()
        return unique_List
    data2 = pd.DataFrame(data1, index=[data1.index], columns=[get_unique(data1).iloc[:,0]])
    for i in range(data2.index[-1][0]):
        if data1.iloc[i,0] == data2.columns[0][0]:
            data2.iloc[i,0] = True
            data2.iloc[i,1] = False
        else:
            data2.iloc[i,1] = True
            data2.iloc[i,0] = False
    return data2




print('\ndata')
print(data)

print('\nget_dummies')
print(pd.get_dummies(data))

print('\nresult')
print(to_onehot(data))