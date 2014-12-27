# -*- coding:utf-8 -*-
import web,datetime

db = web.database(dbn='mysql',db='cqndt',user='root',charset='utf8')

def get_posts():
	return db.select('entries',order='id DESC')  
def get_post(id):
	try:
		return db.select('entries',where='id=$id',vars=locals())[0]
	except IndexError:	##超出索引异常
		return None			

def new_post(title,text):
	db.insert('entries',title=title,content=text,posted_on=datetime.datetime.utcnow())##utcnow方法为获取一个当前的utc
	
def del_post(id):
	db.delete('entries',where="id=$id",vars=locals()) #´Ë´¦varsÓÐÊ²Ã´ÒâÒå
	
def update_post(id,title,text):
	db.update('entries',where="id=$id",vars=locals(),title=title,content=text)

