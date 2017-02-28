#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mysql_utils.db_table import MyTable
import datetime


class DbOprate():

     def __init__(self,mysql_host,mysql_user,mysql_passwd,db):
         engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}:3306/{3}'.format(mysql_user, mysql_passwd, mysql_host,db))
         self.DBSession = sessionmaker(bind=engine)

     def insert_balance_monitor(self,username=None):
         session = self.DBSession()
         new_task = MyTable(username = username)
         session.add(new_task)
         session.commit()
         id = new_task.id
         session.close()
         return id

     def select_balance_monitor(self,id=None,agent_id=None):
         session = self.DBSession()
         if id:
             return session.query(MyTable).filter(MyTable.id == id).all()
         else:
             return session.query(MyTable).all()

     def update_balance_monitor_info(self, id,username):
         session = self.DBSession()
         session.query(MyTable).filter(MyTable.id == id).update({MyTable.username: username})
         session.commit()
         session.close()
