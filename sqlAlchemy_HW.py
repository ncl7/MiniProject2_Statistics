import sqlalchemy as db
engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)
# Print the column names
print(census.columns.keys())
# Print full table metadata
print(repr(metadata.tables['census']))
