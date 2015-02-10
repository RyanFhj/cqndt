#!/usr/bin/env python
# -*- coding:utf8 -*-

import web
import orgnization_model
import render_templates

urls = (
	'','view',
	'/','view',
	'/edit/(\d+)','edit'
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
			post = orgnization_model.get_posts()
			return render.orgnization(post)
		else:
			raise web.seeother('login')

class edit:
	def GET(self,id):
		if logged():
			post = orgnization_model.get_post(int(id))
			return render.orgnization_edit(post)
		else:
			raise web.seeother('login')
			
	def POST(self,id):
		posts = web.input()
		excute = orgnization_model.update(int(id),posts.title,posts.org_img)
		if excute == 1:
			raise web.seeother('/')
		else:
			return 'Error'

app_orgnization = web.application(urls,globals())
