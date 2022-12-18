from datetime import date
from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase
from sqlalchemy.orm import relationship

Base = declarative_base(cls=RepresentableBase)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    first_name = Column(String(50))
    age = Column(String(10))
    city = Column(String(50))
    description = Column(String(1000))
    created_day = Column(DateTime, default=date.today())

    goals = relationship('Goal', backref='user')

    def __repr__(self):
        return f'{self.username}'


class Goal(Base):
    __tablename__ = 'goals'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    goal = Column(String(1000))
    created_day = Column(DateTime, default=date.today())

    def __repr__(self):
        return f'{self.goal}'
