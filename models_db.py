import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connect to the database
engine = create_engine('sqlite:///lya', echo=True)

# Declarative mapping: tables description and class mapping to them in one step
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)

# Create a schema: For actually creating the tables in the database
Base.metadata.create_all(engine)
