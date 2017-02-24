#!/usr/bin/env python
# -*- coding: utf-8 -*-
from util import config_util
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.spider_monitor_task import BalanceMonitor
import datetime


class DbOprate():

     def __init__(self):
         mysql_host = config_util.get_conf('MYSQL_HOST')
         mysql_user = config_util.get_conf('MYSQL_USER')
         mysql_passwd = config_util.get_conf('MYSQL_PASSWORD')
         engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}:3306/ycf_priceratio'.format(mysql_user, mysql_passwd, mysql_host))
         self.DBSession = sessionmaker(bind=engine)

     def insert_balance_monitor(self, agent_id, start_time=None):
         session = self.DBSession()
         new_task = BalanceMonitor(agent_id=agent_id, start_time=datetime.datetime.now())
         session.add(new_task)
         session.commit()
         id = new_task.id
         session.close()
         return id

     def select_balance_monitor(self,id=None,agent_id=None):
         session = self.DBSession()
         if agent_id and id:
             return session.query(BalanceMonitor).filter(BalanceMonitor.id == id). \
                 filter(BalanceMonitor.agent_id == agent_id).all()
         elif id:
             return session.query(BalanceMonitor).filter(BalanceMonitor.id == id).all()
         elif agent_id:
             return session.query(BalanceMonitor).filter(BalanceMonitor.agent_id == agent_id).all()
         else:
             return session.query(BalanceMonitor).all()

     def update_balance_monitor_info(self, id, task_status,error_info=None):
         session = self.DBSession()
         session.query(BalanceMonitor).filter(BalanceMonitor.id == id).update(
             {BalanceMonitor.end_time: datetime.datetime.now(), BalanceMonitor.fail_info: error_info, BalanceMonitor.task_status: task_status})
         session.commit()
         session.close()


if __name__ == '__main__':
    op = DbOprate()
    # op.insert_balance_monitor('GY1111',1,"test","ddd","dddd")
    a = op.select_balance_monitor()
    print a
    # hotels = op.select_monitor_hotel(1)
    # for h in hotels:
    #     print h.hotel_id, h.hotel_name
    # print len(hotels)

    # hotels = op.select_monitor_hotel(2)
    # for h in hotels:
    #     print h.hotel_id, h.hotel_name
    # print len(hotels)
