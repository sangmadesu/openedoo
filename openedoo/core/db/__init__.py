from sqlalchemy import *
from sqlalchemy.orm import relationship, backref,create_session,Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import json
from datetime import datetime, date

##table declaration
from db_tables import od_users
from openedoo import config


engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Base = declarative_base()
metadata = MetaData(bind=engine)
auto_map = automap_base()


class query(object):
	def __init__(self):
		self = "welcome to help menu"

	def select_db(self,tables,column,page=0,page_size=None,**value_column):
		'''equvalent with select * from tables where column = value_column, this didn't support with order by or join table'''
		try:
			session = sessionmaker()
			session.configure(bind=engine)
	 		Base.metadata.create_all(engine)
			s = session()
			if ('value' in value_column):
				kueridb = s.query(tables).filter(column == value_column['value'])
			else:
				kueridb = s.query(tables)
			if page_size != None:
				kueridb = kueridb.limit(page_size)
			if page != 0:
				kueridb = kueridb.offset(page*page_size)
			list1 = list(s.execute(kueridb))
			engine.dispose()
			return list1
		except Exception as e:
			return False
			
	def update_db(self,tables,column,value_column,dict_update):
		'''for update row in tables'''
		#namatable = namatable
		session = sessionmaker()
		session.configure(bind=engine)
 		Base.metadata.create_all(engine)
		s = session()
		try:
			s.query(tables).filter(column==value_column).update(dict_update)
			s.commit()
			engine.dispose()
			return True
		except Exception as e:
			return e
	def delete_db(self,tables,data):
		try:
			session = sessionmaker()
			session.configure(bind=engine)
			Base.metadata.create_all(engine)
			s = session()
			Base.metadata.create_all(engine)
			jack = s.query(tables).get(data)
			s.delete(jack)
			s.commit()
			engine.dispose()
			return True
		except Exception as e:
			return False

	def insert_db(self,new):
		try:
			Session = sessionmaker(bind=engine)
			session = Session()
			Base.metadata.create_all(engine)
			session.add(new)
			session.commit()
			engine.dispose()
			return True
		except Exception as e:
			return False
