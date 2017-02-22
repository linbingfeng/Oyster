#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BalanceMonitor(Base):
    __tablename__ = 'balance_monitor'

    id = Column(Integer(), primary_key=True)
    agent_id = Column(String(200))
    task_status = Column(Integer())
    fail_info = Column(String(1000))
    start_time = Column(DateTime())
    end_time = Column(DateTime())
