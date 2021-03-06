# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()


db.define_table(
		auth.settings.table_user_name,
		Field('first_name', length=128, default='',unique=True,readable=False,writable=False),
		#Field('last_name', length=128, default=''),
		Field('username'),
		Field('choose',requires=IS_IN_SET(['company','jobfinders'])),
		Field('email', length=128, default='', unique=True), # required
		Field('password', 'password', length=512, # required
			readable=False, label='Password'),
		Field('registration_key', length=512, # required
			writable=False, readable=False, default=''),
		Field('reset_password_key', length=512, # required
			writable=False, readable=False, default=''),
		Field('registration_id', length=512, # required
			writable=False, readable=False, default=''),
		)

			                    # do not forget valida
custom_auth_table = db[auth.settings.table_user_name] # get the custom_auth_table
custom_auth_table.first_name.requires = IS_NOT_EMPTY(error_message=auth.messages.is_empty)
			       #custom_auth_table.last_name.requires = IS_NOT_EMPTY(error_message=auth.messages.is_empty)
custom_auth_table.password.requires = CRYPT()
custom_auth_table.email.requires = [IS_NOT_IN_DB(db, custom_auth_table.email)]
custom_auth_table.username.requires= [IS_NOT_IN_DB(db, custom_auth_table.username)]
auth.settings.table_user = custom_auth_table # tell auth to use custom_auth_table
				     ## create all tables needed by auth if not custom tables

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'smtp.gmail.com:587'
mail.settings.sender = 'jvash123@gmail.com'
mail.settings.login = 'jvash123:abcdefgh12345678'

## configure auth policy
auth.settings.registration_requires_verification = True
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth, filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################


db.define_table('profile1',
		Field('stid'),
		Field('first_name','string',label="First Name",required=True),
		Field('last_name','string',label="Last Name",required=True),
		Field('father_name','string',label="Father's Name"),
		Field('chirunama','text',label='Address',required=True),
		Field('phoneno','string',label="Phone number",required=True),
		Field('profilepic','upload',"Profile Pic(Optional)")
		)
db.define_table('profile2',
		Field('stid'),
		Field('schoolname','string',label="School",required=True),
		#Field('address','text',label='Address'),
		Field('passoutyear','integer',label="Passoutyear",required=True),
		#Field('percentage','double'),
		Field('percentage','double',label="Percentage(10th finals)",requires=IS_FLOAT_IN_RANGE(1,100),required=True),
		)

db.define_table('profile3',
		Field('stid'),
		Field('collegename','string',label="College"),
		Field('course','string',label="Branch(CSE/ECE/...)"),
		#Field('address','text',label='Address of instution'),
		Field('passoutyear','integer',label='Passoutyear'),
		Field('cgpa','double',label="CGPA",requires=IS_FLOAT_IN_RANGE(1,10),required=True),
		)
db.define_table('profile4',
		Field('stid'),
		Field('istam','text',label='Personal Hobbies/Interests'),
		Field('projects','text',label='Works/Projects with description',required=True),
		#Field('pani','text',label='Work experience with A')
		)
db.define_table('profile5',
		Field('stid'),
		Field('workedin','string',label='Name of the Company'),
		Field('post','string',label='Worked as'),
		Field('pani','double',label='Worked for(years)')
		)
db.define_table('companyprofile',
		Field('stid'),
		Field('name','string',label="Name",required=True),
		Field('country','string',label='Based in(country)',required=True),
		Field('states','string',label='Revenue',required=True),
		#New field down one
		Field('workers','integer',label='Workforce',required=True),
		Field('chairperson','string',label='President/Chairperson',required=True),
		)
db.define_table('messaging',
		Field('frome',label='From(Username)',required=True),
		Field('toe',label="To(Username)",required=True),
		Field('subject',label="Subject"),
		Field('matter','text',label="Content",required=True),
		Field('filematter','upload',label="Attachments")
		)
db.define_table('notifye',
		Field('bye',label="By(company)",required=True),
		Field('title',label="Title",required=True),
		Field('matter','text',label="Notice",required=True)
		)
## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
