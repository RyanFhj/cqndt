#!/usr/bin/env python
#-*- coding:utf8 -*-

import web
import expert_model
import render_templates

urls=(
	'','expert',
	'/view/(\d+)','view',
	'/edit/(\d+)','edit',
	'/delete/(\d+)','delete',
	'/new','new'
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

class expert:
	def GET(self):
		if logged():
			posts = expert_model.get_posts()
			return render.expert(posts)
		else:
			raise web.seeother('login')
class view:
	def GET(self,id):
		if logged():
			posts = expert_model.get_post(int(id))
			return render.expert_view(posts)
		else:
			raise web.seeother('login')
class edit:
	def GET(self,id):
		if logged():
			post = expert_model.get_post(int(id))
			return render.expert_edit(post)
		else:
			raise web.seeother('login')

	def POST(self,id):
		data = web.input()
		excute = expert_model.update_post(int(id),data.name,data.title,data.intro,data.work_exp,data.honor,data.img)
		if excute == 1:
			raise web.seeother('/')
		else:
			return 'No data update'

class delete:
	def GET(self,id):
		if logged():
			excute = expert_model.del_post(int(id))
			raise web.seeother('/')
		else:
			raise web.seeother('login')

class new:
	def GET(self):
		if logged():
			data = web.input()
			return render.expert_new(data)
		else:
			raise web.seeother('login')
	def POST(self):
		data = web.input()
		excute = expert_model.new_post(data.name,data.title,data.intro,data.work_exp,data.honor,data.img)
		if excute:
			raise web.seeother('/')
		else:
			return 'Add new expert fail'

app_expert = web.application(urls,globals())