import pandas as pd

df = pd.read_csv('./data/sample_pandas_normal.csv', index_col=0)
print(df)
#          age state  point
# name
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

print(df['age'])
print(type(df['age']))
# name
# Alice      24
# Bob        42
# Charlie    18
# Dave       68
# Ellen      24
# Frank      30
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(df.age)
print(type(df.age))
# name
# Alice      24
# Bob        42
# Charlie    18
# Dave       68
# Ellen      24
# Frank      30
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(df[['age', 'point']])
print(type(df[['age', 'point']]))
#          age  point
# name
# Alice     24     64
# Bob       42     92
# Charlie   18     70
# Dave      68     70
# Ellen     24     88
# Frank     30     57
# <class 'pandas.core.frame.DataFrame'>

print(df[['age']])
print(type(df[['age']]))
#          age
# name
# Alice     24
# Bob       42
# Charlie   18
# Dave      68
# Ellen     24
# Frank     30
# <class 'pandas.core.frame.DataFrame'>

print(df['age':'point'])
# Empty DataFrame
# Columns: [age, state, point]
# Index: []

print(df.loc[:, 'age':'point'])
print(type(df.loc[:, 'age':'point']))
#          age state  point
# name
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57
# <class 'pandas.core.frame.DataFrame'>

print(df.iloc[:, [0, 2]])
print(type(df.iloc[:, [0, 2]]))
#          age  point
# name
# Alice     24     64
# Bob       42     92
# Charlie   18     70
# Dave      68     70
# Ellen     24     88
# Frank     30     57
# <class 'pandas.core.frame.DataFrame'>

print(df[1:4])
print(type(df[1:4]))
#          age state  point
# name
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# <class 'pandas.core.frame.DataFrame'>

print(df[:-3])
print(type(df[1:-3]))
#          age state  point
# name
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# <class 'pandas.core.frame.DataFrame'>

print(df[::2])
print(type(df[::2]))
#          age state  point
# name
# Alice     24    NY     64
# Charlie   18    CA     70
# Ellen     24    CA     88
# <class 'pandas.core.frame.DataFrame'>

print(df[1::2])
print(type(df[1::2]))
#        age state  point
# name
# Bob     42    CA     92
# Dave    68    TX     70
# Frank   30    NY     57
# <class 'pandas.core.frame.DataFrame'>

# print(df[1])
# KeyError: 1

print(df[1:2])
print(type(df[1:2]))
#       age state  point
# name
# Bob    42    CA     92
# <class 'pandas.core.frame.DataFrame'>

print(df['Bob':'Ellen'])
print(type(df['Bob':'Ellen']))
#          age state  point
# name
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# <class 'pandas.core.frame.DataFrame'>

print(df.loc['Bob'])
print(type(df.loc['Bob']))
# age      42
# state    CA
# point    92
# Name: Bob, dtype: object
# <class 'pandas.core.series.Series'>

print(df.loc[['Bob', 'Ellen']])
print(type(df.loc[['Bob', 'Ellen']]))
#        age state  point
# name
# Bob     42    CA     92
# Ellen   24    CA     88
# <class 'pandas.core.frame.DataFrame'>

print(df.iloc[[1, 4]])
print(type(df.iloc[[1, 4]]))
#        age state  point
# name
# Bob     42    CA     92
# Ellen   24    CA     88
# <class 'pandas.core.frame.DataFrame'>

s = df['age']
print(s)
# name
# Alice      24
# Bob        42
# Charlie    18
# Dave       68
# Ellen      24
# Frank      30
# Name: age, dtype: int64

print(s[3])
print(type(s[3]))
# 68
# <class 'numpy.int64'>

print(s['Dave'])
print(type(s['Dave']))
# 68
# <class 'numpy.int64'>

print(s[-1])
print(type(s[-1]))
# 30
# <class 'numpy.int64'>

print(s.Dave)
print(type(s.Dave))
# 68
# <class 'numpy.int64'>

print(s[[1, 3]])
print(type(s[[1, 3]]))
# name
# Bob     42
# Dave    68
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(s[['Bob', 'Dave']])
print(type(s[['Bob', 'Dave']]))
# name
# Bob     42
# Dave    68
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(s[[1]])
print(type(s[[1]]))
# name
# Bob    42
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(s[['Bob']])
print(type(s[['Bob']]))
# name
# Bob    42
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(s[1:3])
print(type(s[1:3]))
# name
# Bob        42
# Charlie    18
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(s['Bob':'Dave'])
print(type(s['Bob':'Dave']))
# name
# Bob        42
# Charlie    18
# Dave       68
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(s[1:2])
print(type(s[1:2]))
# name
# Bob    42
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(s['Bob':'Bob'])
print(type(s['Bob':'Bob']))
# name
# Bob    42
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(df['age']['Alice'])
# 24

print(df['Bob':'Dave'][['age', 'point']])
#          age  point
# name
# Bob       42     92
# Charlie   18     70
# Dave      68     70

print(df.at['Alice', 'age'])
# 24

print(df.loc['Bob':'Dave', ['age', 'point']])
#          age  point
# name
# Bob       42     92
# Charlie   18     70
# Dave      68     70

df = pd.DataFrame([[0, 10, 20], [30, 40, 50], [60, 70, 80]],
                  index=[2, 0, 1], columns=[1, 2, 0])
print(df)
#     1   2   0
# 2   0  10  20
# 0  30  40  50
# 1  60  70  80

print(df[0])
# 2    20
# 0    50
# 1    80
# Name: 0, dtype: int64

print(df[[0, 2]])
#     0   2
# 2  20  10
# 0  50  40
# 1  80  70

print(df[:2])
#     1   2   0
# 2   0  10  20
# 0  30  40  50

print(df[-2:])
#     1   2   0
# 0  30  40  50
# 1  60  70  80

print(df.loc[:2])
#    1   2   0
# 2  0  10  20

print(df.iloc[:2])
#     1   2   0
# 2   0  10  20
# 0  30  40  50

s = df[2]
print(s)
# 2    10
# 0    40
# 1    70
# Name: 2, dtype: int64

print(s[0])
# 40

print(s.at[0])
# 40

print(s.iat[0])
# 10

# print(s[-1])
# KeyError: -1

print(s.iat[-1])
# 70