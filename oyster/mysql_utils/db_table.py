#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MyTable(Base):
    __tablename__ = 'balance_monitor'

    id = Column(Integer(), primary_key=True)
    username = Column(String(40))
