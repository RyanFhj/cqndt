#!/usr/bin/env python
# -*- coding:utf8 - *-
import web
import category_model

urls=(
	'','view',
	'/new','new',
	'/edit/(\d+)','edit',
	'/delete/(\d+)','delete',
)

t_globals={
	'datestr':web.datestr
}

render = web.template.render('templates/admin',base='base',globals=t_globals)

class view:
	def GET(self):
		posts = category_model.get_posts()
		
		return render.category(posts)

class edit:
	def GET(self,id):
		post = category_model.get_post(int(id))
		return render.category_edit(post)
	def POST(self,id):
		data = web.input()
		excute = category_model.update_post(int(id),data.title)
		if excute == 1:
			return 'category update done'
		else:
			return 'category update fail'

class delete:
	def GET(self,id):
		excute = category_model.delete_post(int(id))
		return excute
	def POST(self,id):
		excute = category_model.delete_post(int(id))
		if excute == 1:
			return 'Delete category done'
		else:
			return 'Delete category fail'

class new:
	def GET(self):
		data = web.input()
		return render.category_new(data)
	def POST(self):
		data = web.input()
		excute = category_model.insert_post(data.title)
		return excute
		
app_category = web.application(urls,globals())