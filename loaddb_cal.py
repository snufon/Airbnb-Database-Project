import pandas as pd
from sqlalchemy import create_engine

file_berlin = '../airbnb/berlin_calendar.csv'
file_barcelona = '../airbnb/barcelona_calendar.csv'
file_madrid = '../airbnb/madrid_calendar.csv'

#x =  pd.read_csv(file_berlin)
#print(x.shape[0])
print(pd.read_csv(file_berlin))
print(pd.read_csv(file_barcelona))
print(pd.read_csv(file_madrid))

chunksize = 100000
i = 0
j = 1

"""
for df in pd.read_csv(file, chunksize=chunksize, iterator=True):
      df = df.rename(columns={c: c.replace(' ', '') for c in df.columns})
      df.index += j
      i+=1
      df.to_sql('table', csv_database, if_exists='append')
      j = df.index[-1] + 1
"""
