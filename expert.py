#!/usr/bin/env python
#-*- coding:utf8 -*-

import web
import expert_model

urls=(
	'','expert',
	'/view/(\d+)','view',
	'/edit/(\d+)','edit',
	'/delete/(\d+)','delete',
	'/new','new'
)

t_globas={
	'datestr':web.datestr
}

render = web.template.render('templates/admin',base='base',globals=t_globas)

class expert:
	def GET(self):
		posts = expert_model.get_posts()
		return render.expert(posts)

class view:
	def GET(self,id):
		posts = expert_model.get_post(int(id))
		return render.expert_view(posts)

class edit:
	def GET(self,id):
		post = expert_model.get_post(int(id))
		return render.expert_edit(post)
	def POST(self,id):
		data = web.input()
		excute = expert_model.update_post(int(id),data.name,data.title,data.intro,data.work_exp,data.honor,data.img)
		if excute == 1:
			raise web.seeother('/')
		else:
			return 'No data update'

class delete:
	def GET(self,id):
		excute = expert_model.del_post(int(id))
		raise web.seeother('/')

class new:
	def GET(self):
		data = web.input()
		return render.expert_new(data)
	def POST(self):
		data = web.input()
		excute = expert_model.new_post(data.name,data.title,data.intro,data.work_exp,data.honor,data.img)
		if excute:
			raise web.seeother('/')
		else:
			return 'Add new expert fail'

app_expert = web.application(urls,globals())