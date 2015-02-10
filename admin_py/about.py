#!/usr/bin/env python
# -*- coding:utf8 -*-

import web
import about_model
import render_templates

urls = (
	'','about',
	'/new','new',
	'/view/(\d+)','view',
	'/edit/(\d+)','edit',
	'/delete/(\d+)','delete',
)

t_globals ={
	'datestr':web.datestr
}


render = render_templates.get_admin_templates(t_globals)

def logged():
	if web.ctx.session.login == 1:
		return True
	else:
		return False

class about:
	def GET(self):
		if logged():
			posts = about_model.get_posts()
			return render.about(posts)
		else:
			raise web.seeother('login')

class view:
	def GET(self,id):
		if logged():
			posts = about_model.get_post(int(id))
			return render.about_view(posts)
		else:
			raise web.seeother('login')

class edit:
	def GET(self,id):
		if logged():
			posts = about_model.get_post(int(id))
			return render.about_edit(posts)
		else:
			raise web.seeother('login')
	def POST(self,id):
		data = web.input()
		excute = about_model.update_post(int(id),data.title,data.content,data.phonenum,data.email,data.address,data.img)
		if excute == 1:
			return 'Update done'
		else:
			return 'No data update'

class delete:
	def GET(self,id):
		if logged():
			excute = about_model.del_post(int(id))
			if excute ==1:
				return "Delete done"
			else:
				return "No data delete"
		else:
			raise web.seeother('login')
	def POST(self,id):
		excute = about_model.del_post(int(id))
		if excute ==1:
			return "Delete done"
		else:
			return "No data delete"

class new:
	def GET(self):
		if logged():
			data = web.input()
			return render.about_new(data)
		else:
			raise web.seeother('login')
	def POST(self):
		data = web.input()
		excute = about_model.new_post(data.title,data.content,data.phonenum,data.email,data.address,data.img)		
		if excute:
			return 'Add access'
		else:
			return 'Add fail'


app_about = web.application(urls,globals())