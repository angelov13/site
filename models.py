from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Admin_groups(db.Model):
	__tablename__ = 'admin_groups'
	id_group = db.Column(db.Integer,primary_key=True,nullable=False)
	name_group = db.Column(db.String(30),unique=True,nullable=False)
	admins = db.relationship('Admin', backref='admin_groups', lazy='dynamic')
	write_articles = db.Column(db.Boolean,default=False)
	edit_articles = db.Column(db.Boolean,default=False)
	read_data_users = db.Column(db.Boolean,default=False)
	edit_data_users = db.Column(db.Boolean,default=False)
	create_data_users = db.Column(db.Boolean,default=False)
	config_site = db.Column(db.Boolean,default=False)
	admin_tools = db.Column(db.Boolean,default=False)
	read_contact = db.Column(db.Boolean,default=False)
	write_contact = db.Column(db.Boolean,default=False)
	service_tools = db.Column(db.Boolean,default=False)
	marketing_tools = db.Column(db.Boolean,default=False)

	def __init__(self,name_group,write_articles,edit_articles,read_data_users,edit_data_users,create_data_users,config_site,admin_tools,read_contact,write_contact,service_tools,marketing_tools):
		self.name_group = name_group
		self.write_articles = write_articles
		self.edit_articles = edit_articles
		self.read_data_users = read_data_users
		self.edit_data_users = edit_data_users
		self.create_data_users = create_data_users
		self.config_site = config_site
		self.admin_tools = admin_tools
		self.read_contact = read_contact
		self.write_contact = write_contact
		self.service_tools = service_tools
		self.marketing_tools = marketing_tools

	def __repr__(self):
		return 'Group: {u}'.format(u=self.name_group)


class Admin(db.Model):
	__tablename__ = 'admins'
	id_admin = db.Column(db.Integer,primary_key=True,nullable=False)
	nick_name_admin = db.Column(db.String(30),unique=True,nullable=False)
	name_admin = db.Column(db.String(30),nullable=False)
	last_name_admin = db.Column(db.String(30))
	mail_admin = db.Column(db.String(55),unique=True,nullable=False)
	password_admin = db.Column(db.String(128),nullable=False)
	state_admin = db.Column(db.String(20),nullable=False)
	admin_group = db.Column(db.Integer, db.ForeignKey('admin_groups.id_group'),nullable=False)
	articles = db.relationship('Articles', backref='admins', lazy='dynamic')

	def __init__(self,nick_name_admin,name_admin,last_name_admin,mail_admin,password_admin,state_admin,admin_group):
		self.nick_name_admin = nick_name_admin
		self.name_admin = name_admin
		self.last_name_admin = last_name_admin
		self.mail_admin = mail_admin
		self.password_admin = password_admin
		self.state_admin = state_admin
		self.admin_group = admin_group

	def __repr__(self):
		return 'Admin: {u}'.format(u=self.nick_name_admin)


class Users(db.Model):
	__tablename__ = 'users'
	id_user = db.Column(db.Integer,primary_key=True,nullable=False)
	nick_name_user = db.Column(db.String(30),unique=True,nullable=False)
	name_user = db.Column(db.String(30))
	last_name_user = db.Column(db.String(30))
	mail_user = db.Column(db.String(55),unique=True,nullable=False)
	state_user = db.Column(db.String(20))

	def __init__(self,nick_name_user,name_user,last_name_user,mail_user,state_user):
		self.nick_name_user = nick_name_user
		self.name_user = name_user
		self.last_name_user = last_name_user
		self.mail_user = mail_user
		self.state_user = state_user

	def __repr__(self):
		return 'User: {u}'.format(u=self.nick_name_user)


class Articles(db.Model):
	__tablename__ = 'articles'
	id_post = db.Column(db.Integer,primary_key=True,nullable=False)
	type_post = db.Column(db.String(20))
	title_post = db.Column(db.String(100),unique=True,nullable=False)
	url_post = db.Column(db.String(100),unique=True,nullable=False)
	description_post = db.Column(db.String(200))
	content_post = db.Column(db.Text)
	author_post = db.Column(db.Integer,db.ForeignKey('admins.id_admin'),nullable=False)
	publish_date = db.Column(db.DateTime)
	state_post = db.Column(db.String(20))
	category = db.Column(db.Integer,db.ForeignKey('taxonomy.id_taxonomy'),nullable=False)

	def __init__(self,type_post,title_post,url_post,description_post,content_post,author_post,publish_date,state_post,category):
		self.type_post = type_post
		self.title_post = title_post
		self.url_post = url_post
		self.description_post = description_post
		self.content_post = content_post
		self.author_post = author_post
		self.publish_date = publish_date
		self.state_post = state_post
		self.category = category

	def __repr__(self):
		return 'Article: {u}'.format(u=self.title_post)

class Gallery(db.Model):
	__tablename__ = 'gallery'
	id_file = db.Column(db.Integer,primary_key=True,nullable=False)
	name_file = db.Column(db.String(100),nullable=False)
	text_alt_file = db.Column(db.String(100))
	url_file = db.Column(db.String(100),nullable=False)
	description_file = db.Column(db.String(200))

	def __init__(self,name_file,text_alt_file,url_file,description_file):
		self.name_file = name_file
		self.text_alt_file = text_alt_file
		self.url_file = url_file
		self.description_file = description_file

	def __repr__(self):
		return 'File: {u}'.format(u=self.name_file)


class Taxonomy(db.Model):
	__tablename__ = 'taxonomy'
	id_taxonomy = db.Column(db.Integer,primary_key=True,nullable=False)
	name_taxonomy = db.Column(db.String(30),unique=True,nullable=False)
	url_taxonomy = db.Column(db.String(100),unique=True,nullable=False)
	type_taxonomy = db.Column(db.String(30),nullable=False)
	childs = db.relationship('Articles', backref='taxonomy', lazy='dynamic')

	def __init__(self,name_taxonomy,url_taxonomy,type_taxonomy):
		self.name_taxonomy = name_taxonomy
		self.url_taxonomy = url_taxonomy
		self.type_taxonomy = type_taxonomy

	def __repr__(self):
		return 'Taxonomy: {u}'.format(u=self.name_taxonomy)


class Options(db.Model):
	__tablename__ = 'options'
	id_option = db.Column(db.Integer,primary_key=True,nullable=False)
	name_option = db.Column(db.String(50),unique=True,nullable=False)
	value_option = db.Column(db.Text,nullable=False)

	def __init__(self,name_option,value_option):
		self.name_option = name_option
		self.value_option = value_option

	def __repr__(self):
		return 'Option: {u}'.format(u=self.name_option)