#!/usr/bin/env python
# -*- coding:utf8 -*-

import web
import orgnization_model

urls = (
	'','view',
	'/','view',
	'/edit/(\d+)','edit'
)

t_globals={
	
	'datestr':web.datestr
}

render = web.template.render('templates/admin',base='base',globals=t_globals)

		

class view:
	def GET(self):
		post = orgnization_model.get_posts()
		return render.orgnization(post)

class edit:
	def GET(self,id):
		post = orgnization_model.get_post(int(id))
		return render.orgnization_edit(post)
	def POST(self,id):
		posts = web.input()
		excute = orgnization_model.update(int(id),posts.title,posts.org_img)
		if excute == 1:
			raise web.seeother('/')
		else:
			return 'Error'

app_orgnization = web.application(urls,globals())
