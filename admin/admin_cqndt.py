# -*- coding:utf-8 -*-

#/admin 程序入口

import web
import admin_model

urls = (
	'/admin','admin',				#后台首页
	'/view/(\d+)','view',			#文章展示页
	'/edit/(\d+)','edit',			#文章编辑页
	'/delete/(\d+)','delete', 		#文章删除页
	'/new','new',					#增加新文章
)


t_globals = {
	'datestr':web.datestr
}

render = web.template.render('templates',base='base',globals=t_globals)

class admin:
	def GET(self):
		posts = admin_model.get_posts()
		return render.admin(posts)
		

class view:
	def GET(self,id):
		post = admin_model.get_post(int(id))
		return render.view(post)
		
		
class edit:
	def GET(self,id):
		post = admin_model.get_post(int(id))
		form = new.form()
		form.fill(post)
		return render.edit(post,form)
		
	def POST(self,id):
		form = new.form()
		post = admin_model.get_post(int(id))
		if not form.validates():
			return render.edit(post,form)
		admin_model.update_post(int(id),form.d.title,form.d.content)
		raise web.seeother('/admin')
		
class delete:
	def POST(self,id):
		admin_model.del_post(int(id))
		raise web.seeother('/admin')
		
class new:
	form = web.form.Form(
		web.form.Textbox('title',web.form.notnull,
			size=30,
			description="Post title:"),
		web.form.Textarea('content',web.form.notnull,
			rows=30,cols=80,
			description="Post Content:"),
		web.form.Button('Entry'),
	)
	def GET(self):
		form = self.form()
		return render.new(form)
		
	def POST(self):
		form = self.form()
		if not form.validates():
			return render.new(form)
		admin_model.new_post(form.d.title,form.d.content)
		raise web.seeother('/admin')
		
		
app = web.application(urls,globals())

if __name__ == '__main__':
	app.run()