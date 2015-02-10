#!/usr/bin/env python
# -*- coding:utf8 - *-
import web
import category_model
import render_templates

urls=(
	'','view',
	'/new','new',
	'/edit/(\d+)','edit',
	'/delete/(\d+)','delete',
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

class view:
	def GET(self):
		if logged():
			posts = category_model.get_posts()		
			return render.category(posts)
		else:
			raise web.seeother('login')

class edit:
	def GET(self,id):
		if logged():
			post = category_model.get_post(int(id))
			return render.category_edit(post)
		else:
			raise web.seeother('login')

	def POST(self,id):
		data = web.input()
		excute = category_model.update_post(int(id),data.title)
		if excute == 1:
			return 'category update done'
		else:
			return 'category update fail'

class delete:
	def GET(self,id):
		if logged():
			excute = category_model.delete_post(int(id))
			return excute
		else:
			raise web.seeother('login')
	def POST(self,id):
		excute = category_model.delete_post(int(id))
		if excute == 1:
			return 'Delete category done'
		else:
			return 'Delete category fail'

class new:
	def GET(self):
		if logged():
			data = web.input()
			return render.category_new(data)
		else:
			raise web.seeother('login')
	def POST(self):
		data = web.input()
		excute = category_model.insert_post(data.title)
		return excute
		
app_category = web.application(urls,globals())