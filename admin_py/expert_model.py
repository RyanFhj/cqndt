import web

db = web.database(dbn='mysql',host='115.29.224.23',db='cqndt',user='ryan',charset='utf8')

def get_posts():
	return db.select('expert',order='id DESC')

def get_post(id):
	try:
		return db.select('expert',where='id = $id',vars=locals())[0]
	except IndexError:
		return None

def new_post(name,title,intro,work_exp,honor,img):
	return db.insert('expert',name=name,title=title,intro=intro,work_exp=work_exp,honor=honor,img=img)

def del_post(id):
	return db.delete('expert',where='id=$id',vars=locals())

def update_post(id,name,title,intro,work_exp,honor,img):
	return db.update('expert',where='id=$id',name=name,title=title,intro=intro,work_exp=work_exp,honor=honor,img=img)
