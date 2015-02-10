#!/usr/bin/env python
# -*- coding:utf8 -*-
import web
import notice_model
import render_templates

urls = (
	'','getall',
	'/add','add',
	'/view/(\d+)','view'
	'/edit/(\d+)','edit',
	'/delete/(\d+)','delete'

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

class getall:
	def GET(self):
		if login():
			posts = notice_model.getall_notice()
			return render.notice(posts)
		else:
			raise web.seeother('login')

app_notice = web.application(urls,globals())