from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class sitio(db.Model):
	__tablename__ = 'sitio'
	id = db.Column(db.Integer,primary_key=True)
	name_option = db.Column(db.String(),unique=True)
	value_option = db.Column(db.String(),unique=True)

class articles(db.Model):
	__tablename__ = 'articles'
	id = db.Column(db.Integer,primary_key=True)
	post_author = db.Column(db.String())
	post_title = db.Column(db.String(),unique=True)
	post_url = db.Column(db.String())
	post_state = db.Column(db.String())
	post_password = db.Column(db.String())
	post_content = db.Column(db.String())
	post_categorys = db.Column(db.String())

