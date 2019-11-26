import sqlalchemy
sqlalchemy.__version__
'1.2.2'

from sqlalchemy import create_engine
engine = create_engine('sqlite:///sqlite3.db')
# using relative path


