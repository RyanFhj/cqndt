import web

db = web.database(dbn="mysql",host="115.29.224.23",db="cqndt",user="ryan",charset="utf8")

def login(user,passwd):
	return db.select('admin',where='user="%s" and passwd="%s"'% (user,passwd))

