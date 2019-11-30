# This Python file uses the following encoding: utf-8
import sqlite3

conn = sqlite3.connect('/web/Sqlite-Data/example.db')

from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger, CheckConstraint

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from datetime import datetime

engine = create_engine("sqlite:///Sqlite-Data/sqlalchemy_example.db")

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    orders = relationship("Order", backref='customer')

    def __repr__(self):
        return "<Customer:{0}-{1}>".format(self.id, self.username)

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(SmallInteger(), nullable=False)
#     orders = relationship("Order", backref='customer')

    def __repr__(self):
        return "<Item:{0}-{1}>".format(self.id, self.name)

    __table_args__ = (
        CheckConstraint('quantity > 0', name='quantity_check'),)


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now, nullable=False)
    date_shipped = Column(DateTime())

    #     items = relationship("OrderLine")

    def __repr__(self):
        return "<Order:{0}>".format(self.id)


class OrderLine(Base):
    __tablename__ = 'order_lines'
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())
    order = relationship("Order", backref='order_lines')
    item = relationship("Item")

    def __repr__(self):
        return "<OrderLine:{0}>".format(self.id)


Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

from sqlalchemy.orm import sessionmaker, Session
Session = sessionmaker(bind=engine)
session = Session()

c1 = Customer(first_name = 'John',
              last_name = 'Green',
              username = 'johngreen',
              email = 'johngreen@mail.com',
              address = '164 Hidden Valley Road',
              town = 'Norfolk'
             )

c2 = Customer(
            first_name = 'Katherine',
            last_name = 'Wilson',
            username = 'katwilson',
            email = 'katwilson@gmail.com',
            address = '4685 West Side Avenue',
            town = 'Peterbrugh'
             )

c1, c2

c1.first_name, c1.last_name
c2.first_name, c2.last_name

