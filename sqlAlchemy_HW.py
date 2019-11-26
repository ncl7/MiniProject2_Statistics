from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
# using relative path
engine.connect()

print(engine)

from sqlalchemy import MetaData, Table, String, Column, Text, DateTime, Boolean, Integer
from datetime import datetime

metadata = MetaData()

customers = Table('customers', metadata,
    Column('id', Integer(), primary_key=True),
    Column('first_name', String(100), nullable=False),
    Column('last_name', String(100), nullable=False),
    Column('username', String(50), nullable=False),
    Column('email', String(200), nullable=False),
    Column('address', String(200), nullable=False),
    Column('town', String(50), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

