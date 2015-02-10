#!/usr/bin/env python
# -*- coding:utf8 -*-

import web
import render_templates

import index

import about
import orgnization
import expert
import category
import article
import notice
import login

web.config.debug=False
urls=(
	'/index',index.app_index,
	'/admin','admin',
	'/admin/about',about.app_about,
	'/admin/orgnization',orgnization.app_orgnization,
	'/admin/expert',expert.app_expert,
	'/admin/category',category.app_category,
	'/admin/article',article.app_article,
	'/admin/notice',notice.app_notice,
	'/admin/login',login.app_login,
	'/admin/logout','logout'
)

t_globals = {
	'datestr':web.datestr
}

render = render_templates.get_admin_templates(t_globals)
app = web.application(urls,globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'login': 0})

def session_hook():
    web.ctx.session = session

class admin:
	def GET(self):
		if logged():
			return render.admin(self)
		else:
			raise web.seeother('/admin/login')


def logged():
	if web.ctx.session.login == 1:
		return True
	else:
		return False

class logout:
	def GET(self):
		session.login = 0
		raise web.seeother('/admin/login')

app.add_processor(web.loadhook(session_hook))

if __name__ == "__main__":
	app.run()

		