import web

db = web.database(dbn='mysql',host='115.29.224.23',db='cqndt',user='ryan',charset='utf8')



def get_post(id):
	return db.select('category',where='id=$id',vars=locals())[0]

def get_posts():
	return db.query("SELECT count( * ) as num,category.id, category.title FROM category, article WHERE category.id = article.category GROUP BY category.id ORDER BY id DESC")

def update_post(id,title):
	return db.update('category',where='id=$id',title=title,vars=locals())

def delete_post(id):
	return db.delete('category',where='id=$id',vars=locals())

def insert_post(title):
	return db.insert('category',title=title)