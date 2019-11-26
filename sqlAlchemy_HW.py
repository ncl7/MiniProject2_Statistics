from sqlalchemy import create_engine
engine = create_engine('sqlite:///sqlite3.db')
# using relative path
engine.connect()

print(engine)
