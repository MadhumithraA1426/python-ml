import pandas as pd
data={
    'Name':['Maddy','Aish','Sri','Divya'],
    'Age':[20,21,22,23],
    'City':['Bangalore','Hyderabad','Chennai','Mumbai']
}
df=pd.DataFrame(data)
print(df)
print(df['Name'])
print(df['Age'].mean())
print(df['City'].unique())

"""
    Name  Age       City
0  Maddy   20  Bangalore
1   Aish   21  Hyderabad
2    Sri   22    Chennai
3  Divya   23     Mumbai
0    Maddy
1     Aish
2      Sri
3    Divya
Name: Name, dtype: object
21.5
['Bangalore' 'Hyderabad' 'Chennai' 'Mumbai']"""