import sqlalchemy as db
engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
