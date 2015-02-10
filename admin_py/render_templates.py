import web

def get_admin_templates(t_globals):
	return web.template.render('../templates/admin',base='base',globals=t_globals)

def get_front_templates(t_globals):
	return web.template.render('../templates/front',base='base',globals=t_globals)

def get_nobase_templates(t_globals):
	return web.template.render('../templates/front',globals=t_globals)