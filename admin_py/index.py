#!/usr/bin/env python
# -*- coding:utf-8 -*-

import web
import render_templates

import expert_model

urls=(
	'','index',
	'/about','about',
	'/organization','org',
	'/expert','all_expert',
	'/expert/(\d+)','get_expert',
	'/contact','contact',
	'/news','all_new',
	'/newss','get_new',
	'/notice','all_notice',
	'/process','all_process',
	'/table_download','table',
)

t_globals=dict(
	datestr=web.datestr,
	static='/static/front'
)


render = render_templates.get_front_templates(t_globals)


class index:
	def GET(self):
		return render.index()

class about:
	def GET(self):
		return render.about()

class org:
	def GET(self):
		return render.organization()

class all_expert:
	def GET(self):
		expert_info = render_templates.get_nobase_templates(t_globals)
		t_globals['render'] = expert_info
		expert1 = expert_model.get_posts()
		return render.expert(expert1)

class contact:
	def GET(self):
		return render.contact()

class all_new:
	def GET(self):
		return render.news()

class get_new:
	def GET(self):
		return render.news_post()

class all_notice:
	def GET(self):
		return render.notice()

class all_process:
	def GET(self):
		return render.process()

class table:
	def GET(self):
		return render.table_download()

app_index = web.application(urls,globals())