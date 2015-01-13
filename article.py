#!/usr/bin/env python
# -*- coding:utf8 -*-
import web
import article_model

urls=(
	'','getall',
	'/view/(\d+)','view',
	'/edit/(\d+)','edit',
	'/delete/(\d+)','delete',
	'/new','new',
	'/page/(\d+)','page',
)

t_globals={
	'datestr':web.datestr
}

render = web.template.render('templates/admin',base='base',globals=t_globals)


class getall:
	def GET(self):
		pagesize = 10
		num = article_model.get_num()
		if num % pagesize == 0:
			pages = num / pagesize
		else:
			pages = num / pagesize +1
		startindex = 0
		article = article_model.get_page_article(pagesize,startindex)
		return render.article(article,pages)

class view:
	def GET(self,id):
		posts = article_model.get_post(int(id))
		ib = list(posts)
		return render.article_view(ib)

class edit:
	def GET(self,id):
		posts = article_model.get_article(int(id))
		c_posts = article_model.get_category()
		return render.article_edit(list(posts),list(c_posts))
	def POST(self,id):
		data = web.input()
		excute = article_model.update_post(int(id),data.title,data.category,data.content,data.author,data.img,data.date)
		if excute == 1:
			return 'Update Done'
		else:
			return 'Update Fail'

class delete:
	def GET(self,id):
		excute = article_model.delete_post(int(id))
		if excute == 1:
			return 'Delete Done'
		else:
			return 'Delete Fail'

	def POST(self,id):
		excute = article_model.delete_post(int(id))
		if excute == 1:
			return 'Delete Done'
		else:
			return 'Delete Fail'

class new:
	def GET(self):
		c_posts = article_model.get_category()
		return render.article_new(c_posts)
	def POST(self):
		data = web.input()
		excute = article_model.insert_post(data.title,data.category,data.content,data.author,data.img)
		if excute:
			return 'Add Done'
		else:
			return 'Add Fail'
class page:
	def GET(self,id):
		pagesize = 10
		num = article_model.get_num()
		if num % pagesize == 0:
			pages = num / pagesize
		else:
			pages = num / pagesize +1
		startindex = (int(id)-1) * pagesize
		article = article_model.get_page_article(pagesize,startindex)
		return render.article(article,pages)

app_article = web.application(urls,globals())