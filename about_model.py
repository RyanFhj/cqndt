# -*- coding:utf-8 -*-
import web

db = web.database(dbn='mysql',host='115.29.224.23',db='cqndt',user='ryan',charset='utf8')

def get_posts():
	return db.select('about',order='id DESC')  
def get_post(id):
	try:
		return db.select('about',where='id=$id',vars=locals())[0]
	except IndexError:	##超出索引异常
		return None			

def new_post(title,content,phonenum,email,address,img,):
	return db.insert('about',title=title,content=content,phonenum=phonenum,email=email,address=address,img=img)##utcnow方法为获取一个当前的utc
	
def del_post(id):
	return db.delete('about',where="id=$id",vars=locals()) #´Ë´¦varsÓÐÊ²Ã´ÒâÒå
	
def update_post(id,title,content,phonenum,email,address,img,):
	return db.update('about',where="id=$id",vars=locals(),title=title,content=content,phonenum=phonenum,email=email,address=address,img=img)

