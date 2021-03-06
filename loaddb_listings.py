"""from sqlalchemy import create_engine
import cx_Oracle

host='cs322-db.epfl.ch'
port='1521'
sid='ORCLCDB'
user='C##DB2019_G06'
password='DB2019_G06'
sid = cx_Oracle.makedsn(host, port, sid=sid)

cstr = 'oracle://{user}:{password}@{sid}'.format(
    user=user,
    password=password,
    sid=sid
)

engine =  create_engine(
    cstr,
    convert_unicode=False,
    pool_recycle=10,
    pool_size=50,
    echo=False
)

csv_database = create_engine('oracle://C##DB2019_G06:DB2019_G06@cs322-db.epfl.ch:1521/ORCLCDB',encoding='utf8')


result = csv_database.execute("INSERT INTO Amenities(name) VALUES ('henri2')")
result2 = csv_database.execute('SELECT * From Amenities')

for row in result2:
    print(row)
    
  
    
"""
    
import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle

file_berlin = '../airbnb/berlin_listings_filtered.csv'
file_barcelona = '../airbnb/barcelona_listings.csv'
file_madrid = '../airbnb/madrid_listings_filtered.csv'

#print(pd.read_csv(file_berlin, nrows=5))
#print(pd.read_csv(file_barcelona, nrows=5))
#print(pd.read_csv(file_madrid, nrows=5))

###   Step 1   -   Clear the data from incoherent rows ###

df_berlin = pd.read_csv(file_berlin)
df_barcelona = pd.read_csv(file_barcelona)
df_madrid = pd.read_csv(file_madrid)




#to drop the row with index 0 : df.drop(df.columns[[0]], axis=1)

### Step 1.1 find all rows indexes that are incoherents

### Step 1.2 removes those rows
for row in incoherent_rows:
	df.drop(df.columns[[row]], axis=1)

###   Step 2   -   Make smaller csv files ###
"""
def createSmallCsv(_file):
	df_hosts = pd.read_csv(_file, names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
	df_listings = pd.read_csv(_file, names=['id', 'host_id', 'neighorhood_id', 'Age', 'Pre-Test Score', 'Post-Test Score'])
	df_verifications = pd.read_csv(_file, names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
	df_neighborhoods = pd.read_csv(_file, names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
	df_amenities = pd.read_csv(_file, names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
	df_rents = pd.read_csv(_file, names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])	
	df_features = pd.read_csv(_file, names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
	df_reviewScores = pd.read_csv(_file, names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
	df_miscellaneous = pd.read_csv(_file, names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
	df_descriptions = pd.read_csv(_file, names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])

	df_reviews = pd.read_csv(_file, names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
	df_listingsHasAmenities = pd.read_csv(_file, names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
	df_hostshasverification = pd.read_csv(_file, names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
	df_calendars = pd.read_csv(_file, names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])

createSmallCsv(file_berlin)
createSmallCsv(file_barcelona)
createSmallCsv(file_madrid)

"""
#example
#df.columns = ['date']
#df['date'] = pd.to_datetme(df['date'])

#df.to_csv('path/file.csv')


###   Step 3   -   Load data in db (maybe not use python but sqldeveloper or datagrip) ###
"""
csv_database = create_engine('oracle://C##DB2019_G06:DB2019_G06@cs322-db.epfl.ch:1521/ORCLCDB')
df = pd.read_sql_query('SELECT * FROM Amenities', csv_database)

for row in df:
	print(df)

	
"""
"""
chunksize = 100000
i = 0
j = 1
for df in pd.read_csv(file, chunksize=chunksize, iterator=True):
      df = df.rename(columns={c: c.replace(' ', '') for c in df.columns})
      df.index += j
      i+=1
      df.to_sql('table', csv_database, if_exists='append')
      j = df.index[-1] + 1
"""
