from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declarative import Address, Base, Person

engine = create_engine('sqlite:///sqlalchemy_example.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Insert a Person in the person table
new_person = Person(name='new person')
session.add(new_person)
session.commit()

# Insert an Address in the address table
new_address = Address(post_code='00000', person=new_person)
session.add(new_address)
session.commit()

# Make a query to find all Persons in the database
session.query(Person).all()

# Return the first Person from all Persons in the database
person = session.query(Person).first()
person.name
u'new person'

# Find all Address whose person field is pointing to the person object
session.query(Address).filter(Address.person == person).all()

# Retrieve one Address whose person field is point to the person object
session.query(Address).filter(Address.person == person).one()
address = session.query(Address).filter(Address.person == person).one()
address.post_code
u'00000'
