#!/usr/bin/env python
# -*- coding:utf8 -*-

import web

db = web.database(dbn='mysql',host='115.29.224.23',db='cqndt',user='ryan',charset='utf8')

def get_article(id):
	if id <> '':
		return article_posts = db.select('article')
	else:
		return article_posts = db.query("SELECT count( * ) as num,category.id, category.title FROM category, article WHERE category.id = article.category GROUP BY category.id ORDER BY id DESC")
