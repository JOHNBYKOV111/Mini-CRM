from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Operator(Base):
  __tablename__ = 'operators'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  active = Column(Boolean)
  max_load = Column(Integer)
    
  # Связь с таблицей контактов (через многие-к-многим)
  contacts = relationship("Contact", back_populates="operator")

class Lead(Base):
  __tablename__ = 'leads'
  id = Column(Integer, primary_key=True)
  external_id = Column(String, unique=True)
    
  # Связь с таблицей контактов
  contacts = relationship("Contact", back_populates="lead")

class Source(Base):
  __tablename__ = 'sources'
  id = Column(Integer, primary_key=True)
  name = Column(String)
    
  # Связь с таблицей контактов
  contacts = relationship("Contact", back_populates="source")

class Contact(Base):
  __tablename__ = 'contacts'
  id = Column(Integer, primary_key=True)
  lead_id = Column(Integer, ForeignKey('leads.id'))
  source_id = Column(Integer, ForeignKey('sources.id'))
  operator_id = Column(Integer, ForeignKey('operators.id'), nullable=True)
  
  lead = relationship("Lead", back_populates="contacts")
  source = relationship("Source", back_populates="contacts")
  operator = relationship("Operator", back_populates="contacts")

# Дополнительная таблица для хранения весов операторов по источникам
class OperatorSourceWeight(Base):
  __tablename__ = 'operator_source_weights'
  id = Column(Integer, primary_key=True)
  operator_id = Column(Integer, ForeignKey('operators.id'))
  source_id = Column(Integer, ForeignKey('sources.id'))
  weight = Column(Integer)