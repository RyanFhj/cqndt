# -*- coding:utf8 -*-
import web

db = web.database(dbn='mysql',host='115.29.224.23',db='cqndt',user='ryan',charset='utf8')

def get_posts():
	return db.query("SELECT article.id,article.title,category.title as category_title,article.content,article.author,article.img,article.date FROM `category`,`article` WHERE article.category = category.id")

def get_post(id):
	return db.query("SELECT article.id as id,article.title as title,article.content as content,article.author as author,article.img as img,article.date as date,comment.id as c_id,comment.article_id as c_aid,comment.author as c_author,comment.content as c_content,comment.date as c_date FROM article  LEFT JOIN  comment ON article.id =comment.article_id where article.id = $id ORDER BY comment.date DESC",vars=locals())

def get_article(id):
	return db.query("SELECT a.id, a.title,c.id as c_id, c.title as c_title, a.content, a.author, a.img, a.date FROM `article` AS a, `category` AS c WHERE a.category = c.id and a.id = $id",vars=locals())

def get_category():
	return db.select('category')

def update_post(id,title,category,content,author,img,date):
	return db.update('article',where='id=$id',title=title,category=category,content=content,author=author,img=img,date=date,vars=locals())

def delete_post(id):
	return db.delete('article',where='id=$id',vars=locals())

def insert_post(title,category,content,author,img):
	return db.insert('article',title=title,category=category,content=content,author=author,img=img)


def get_num():
	results =  db.query('SELECT COUNT(*) as article_num FROM article')
	num = results[0].article_num
	return num

def get_page_article(pagesize,startindex):
	return db.select('article',order='date DESC',limit=pagesize,offset=startindex)

def searchnum(title):
	results = db.query('SELECT COUNT(*) AS num FROM article')
	num = results[0].num
	return num

def search(title,pagesize,startindex):
	return db.select('article',where='title like "%%%s%%"' % title,order='date DESC',limit=pagesize,offset=startindex,vars=locals())