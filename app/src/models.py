from abc import abstractmethod
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class BaseModel:
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(DateTime, default=datetime.utcnow)

    @abstractmethod
    def from_dict(self, data):  # ToDo
        pass

    @abstractmethod
    def to_dict(self):
        pass


Lexeme_Tag = Table(
    "Lexeme_Tag",
    Base.metadata,
    Column("Lexeme_id", Integer, ForeignKey("Lexeme.id")),
    Column("Tag_id", Integer, ForeignKey("Tag.id")),
)


class Folder(Base, BaseModel):
    __tablename__ = 'Folder'

    name = Column(String)
    folder_id = Column(Integer, ForeignKey('Folder.id'), nullable=True)

    papers = relationship('Paper', back_populates='folder')

    def from_dict(self, data):
        for field in self.__class__.__table__.columns.keys():
            if field in BaseModel.__dict__.keys() and field != 'id':
                pass
            elif field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        data = {
            "id": self.id,
            "create_time": self.create_time,
            "name": self.name,
            "folder_id": self.folder_id
        }
        return data


class Paper(Base, BaseModel):
    __tablename__ = 'Paper'

    name = Column(String)
    folder_id = Column(Integer, ForeignKey('Folder.id'), nullable=True)

    folder = relationship('Folder', back_populates='papers')
    lexemes = relationship('Lexeme', back_populates='paper')

    def from_dict(self, data):
        for field in self.__class__.__table__.columns.keys():
            if field in BaseModel.__dict__.keys() and field != 'id':
                pass
            elif field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        data = {
            "id": self.id,
            "create_time": self.create_time,
            "name": self.name,
            "folder_id": self.folder_id
        }
        return data


class Tag(Base, BaseModel):
    __tablename__ = 'Tag'

    name = Column(String)

    lexemes = relationship('Lexeme', secondary=Lexeme_Tag, back_populates='tags')

    def from_dict(self, data):
        for field in self.__class__.__table__.columns.keys():
            if field in BaseModel.__dict__.keys() and field != 'id':
                pass
            elif field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        data = {
            "id": self.id,
            "create_time": self.create_time,
            "name": self.name
        }
        return data


class Lexeme(Base, BaseModel):
    __tablename__ = 'Lexeme'

    text = Column(String)
    translate = Column(String)
    paper_id = Column(Integer, ForeignKey('Paper.id'), nullable=False)

    paper = relationship('Paper', back_populates='lexemes')
    tags = relationship('Tag', secondary=Lexeme_Tag, back_populates='lexemes')

    def from_dict(self, data):
        for field in self.__class__.__table__.columns.keys():
            if field in BaseModel.__dict__.keys() and field != 'id':
                pass
            elif field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        data = {
            "id": self.id,
            "create_time": self.create_time,
            "text": self.text,
            "translate": self.translate,
            "paper_id": self.paper_id
        }
        return data


class LexemeStatistic(Base, BaseModel):
    __tablename__ = 'LexemeStatistic'

    passing_time = Column(Integer)
    rating = Column(Integer)
    lexeme_id = Column(Integer, ForeignKey('Lexeme.id'), nullable=False)

    lexeme = relationship('Lexeme', back_populates='lexeme_statistic')

    def from_dict(self, data):
        for field in self.__class__.__table__.columns.keys():
            if field in BaseModel.__dict__.keys() and field != 'id':
                pass
            elif field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        data = {
            "id": self.id,
            "create_time": self.create_time,
            "passing_time": self.passing_time,
            "rating": self.rating,
            "lexeme_id": self.lexeme_id
        }
        return data


parent_folder = relationship('Folder', remote_side=[Folder.id], backref='subfolders')
