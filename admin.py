#!/usr/bin/env python
# -*- coding:utf8 -*-

import web
import about
import orgnization
import expert
import category
import article

urls=(
	'/admin','admin',
	'/admin/about',about.app_about,
	'/admin/orgnization',orgnization.app_orgnization,
	'/admin/expert',expert.app_expert,
	'/admin/category',category.app_category,
	'/admin/article',article.app_article,
)

t_globals = {
	'datestr':web.datestr
}

render = web.template.render('templates/admin',base='base', globals=t_globals)

class admin:
	def GET(self):
		return render.admin(self)

app = web.application(urls,globals())

if __name__ == "__main__":
	app.run()
		