from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

eng = create_engine('sqlite:///database.db')

Base = declarative_base()


class User(Base):
    __tablename__ = "Users"

    Id = Column(Integer, primary_key=True)
    Username = Column(String)
    Password = Column(String)
    Email = Column(String)
    Score = Column(Integer)


class Token(Base):
    __tablename__ = "Tokens"

    Id = Column(Integer, primary_key=True)
    UserId = Column(Integer, ForeignKey("Users.Id"))
    Token = Column(String)

    User = relationship("User")


class Game(Base):
    __tablename__ = "Games"

    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Num = Column(Integer)
    Joined = Column(Integer)
    Turn = Column(Integer)
    Board = Column(String)
    Wall = Column(String)


class Joine(Base):
    __tablename__ = "Joines"

    Id = Column(Integer, primary_key=True)
    UserId = Column(Integer, ForeignKey("Users.Id"))
    GameId = Column(Integer, ForeignKey("Games.Id"))

    Game = relationship("Game")
    User = relationship("User")


Base.metadata.bind = eng
Base.metadata.create_all()

Session = sessionmaker(bind=eng)
ses = Session()
