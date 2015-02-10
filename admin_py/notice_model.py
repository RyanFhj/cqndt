import web

db = web.database(dbn='mysql',host='115.29.224.23',db='cqndt',user='ryan',charset='utf8')

def getall_notice():
	return db.select('notice',order='date DESC')
	