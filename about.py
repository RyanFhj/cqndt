#!/usr/bin/env python
# -*- coding:utf8 -*-

import web
import about_model

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


render = web.template.render('templates/admin',base='base',globals=t_globals)

class about:
	def GET(self):
		posts = about_model.get_posts()
		return render.about(posts)

class view:
	def GET(self,id):
		posts = about_model.get_post(int(id))
		return render.about_view(posts)

class edit:
	def GET(self,id):
		posts = about_model.get_post(int(id))
		return render.about_edit(posts)
	def POST(self,id):
		data = web.input()
		excute = about_model.update_post(int(id),data.title,data.content,data.phonenum,data.email,data.address,data.img)
		if excute == 1:
			return 'Update done'
		else:
			return 'No data update'

class delete:
	def GET(self,id):
		excute = about_model.del_post(int(id))
		if excute ==1:
			return "Delete done"
		else:
			return "No data delete"
	def POST(self,id):
		excute = about_model.del_post(int(id))
		if excute ==1:
			return "Delete done"
		else:
			return "No data delete"

class new:
	def GET(self):
		data = web.input()
		return render.about_new(data)
	def POST(self):
		data = web.input()
		excute = about_model.new_post(data.title,data.content,data.phonenum,data.email,data.address,data.img)		
		if excute:
			return 'Add access'
		else:
			return 'Add fail'


app_about = web.application(urls,globals())