import web

db = web.database(dbn='mysql',host='115.29.224.23',db='cqndt',user='ryan',charset='utf8')

def get_posts():
	return db.select('orgnization')
def get_post(id):
	try:
		return db.select('orgnization',where='id=$id',vars=locals())[0]
	except IndexError:	
		return None	
def update(id,title,org_img):
	return db.update('orgnization',where='id=$id',vars=locals(),title=title,org_img=org_img)
