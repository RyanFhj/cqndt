#!/usr/bin/env python
# -*- coding:utf8 -*-

import web
import login_model
import render_templates



urls=(

	'','login'

)

app_login = web.application(urls,globals())
t_globals=dict(
	datestr=web.datestr,
	static='/static'

)



def get_render():
	if logged():
		render = arender_templates.get_admin_templates(t_globals)
	else:
		render = web.template.render('../templates/admin',globals=t_globals)
	return render

def logged():
	if web.ctx.session.login == 1:
		return True
	else:
		return False

class login:
	def GET(self):
		if logged():
			render = get_render()
			return render.admin(self)
		else:
			render = get_render()
			return render.login()
	def POST(self):
		user,password = web.input().user,web.input().password
		posts = login_model.login(user,password)
		if len(posts) == 1:
			web.ctx.session.login = 1
			raise web.seeother('../admin')
		else:
			return 'error'
		
