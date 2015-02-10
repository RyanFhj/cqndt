#!/usr/bin/env python
# -*- coding:utf8 -*-
import web
import article_model
import render_templates

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

render = render_templates.get_admin_templates(t_globals)

def logged():
	if web.ctx.session.login == 1:
		return True
	else:
		return False

class page:
	def GET(self,id):
		if logged():
			pagesize = 10
			num = article_model.get_num()
			if num % pagesize == 0:
				pages = num / pagesize
			else:
				pages = num / pagesize +1
			startindex = (int(id)-1) * pagesize
			article = article_model.get_page_article(pagesize,startindex)
			return render.article(article,pages)
		else:
			raise web.seeother('login')

class getall:
	def GET(self):
		if logged():
			data = web.input()
			if len(data) == 0:
				pagesize = 10
				num = article_model.get_num()
				if num % pagesize == 0:
					pages = num / pagesize
				else:
					pages = num / pagesize +1
				startindex = 0
				article = article_model.get_page_article(pagesize,startindex)
				return render.article(article,pages)
			else:
				search = data.search
				pagesize = 10
				num = article_model.searchnum(search)
				if num % pagesize ==0:
					pages = num / pagesize
				else:
					pages = num / pagesize +1
				startindex = 0
				article = article_model.search(search,pagesize,startindex)
				return render.article(article,pages)
		else:
			raise web.seeother('login')

class view:
	def GET(self,id):
		if logged():
			posts = article_model.get_post(int(id))
			ib = list(posts)
			return render.article_view(ib)
		else:
			raise web.seeother('login')

class edit:
	def GET(self,id):
		if logged():
			posts = article_model.get_article(int(id))
			c_posts = article_model.get_category()
			return render.article_edit(list(posts),list(c_posts))
		else:
			raise web.seeother('login')

	def POST(self,id):
		data = web.input()
		excute = article_model.update_post(int(id),data.title,data.category,data.content,data.author,data.img,data.date)
		if excute == 1:
			return 'Update Done'
		else:
			return 'Update Fail'

class delete:
	def GET(self,id):
		if logged():
			excute = article_model.delete_post(int(id))
			if excute == 1:
				return 'Delete Done'
			else:
				return 'Delete Fail'
		else:
			raise web.seeother('login')

	def POST(self,id):
		excute = article_model.delete_post(int(id))
		if excute == 1:
			return 'Delete Done'
		else:
			return 'Delete Fail'

class new:
	def GET(self):
		if logged():
			c_posts = article_model.get_category()
			return render.article_new(c_posts)
		else:
			raise web.seeother('login')
			
	def POST(self):
		data = web.input()
		excute = article_model.insert_post(data.title,data.category,data.content,data.author,data.img)
		if excute:
			return 'Add Done'
		else:
			return 'Add Fail'


app_article = web.application(urls,globals())