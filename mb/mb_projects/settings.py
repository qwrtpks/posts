# mb_projects/setting.py

INSTALLED_APPS =[
 'posts.apps.Postsconfig', #new
 'django.contrib.admin',
 'django.contrib.auth',
 'django,contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
]

TEMPLATES = [
	{
	...
	'DIRS':[os.path.join(BASE_DIR,'templates')], #new
	...
	},
]

