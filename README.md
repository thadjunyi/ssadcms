# Software System Analysis and Design Crisis Management System

# Creating a Django Project and run it locally
1. Create a virtual environment (virutalenv venv) and enter the venv (activate)
2. Install packages in the newly created environment (pip install django, requests)
3. Creating the application 
4. python manage.py startapp herokuapp
5. Add 'herokuapp' to installed apps in settings.py
6. Migrate the database (python manage.py migrate)
7. Start the development server (python manage.py runserver)

# Deploy Application to Heroku
1. In the virutal environment (activate), cd to current location
2. Login to heroku (heroku login)
3. Enter your heroku credentials
4. Add a Procfile file with (web: gunicorn CMS.wsgi)
5. Install the following packages (pip install gunicorn dj-database-url whitenoise psycopg2)
6. Install Django-heroku packages (pip install django-heroku)
7. Add a requirements.txt file (pip freeze > requirements.txt)
8. Add stuff to settings.py file
	import django_heroku (top)
	# Activate Django-Heroku. (end)
	django_heroku.settings(locals()) (end)
9. Set up the static assets by editing the settings.py
	# Static files (CSS, JavaScript, Images)
	# https://docs.djangoproject.com/en/1.11/howto/static-files/
	PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))
	STATIC_ROOT  =   os.path.join(PROJECT_ROOT, 'staticfiles')
	STATIC_URL = '/static/'

	# Extra lookup directories for collectstatic to find static files
	STATICFILES_DIRS = (
		os.path.join(PROJECT_ROOT, 'static'),
	)

	#  Add configuration for static files storage using whitenoise
	STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
10. Add whitenoise middleware at the top of the middleware list in settings.py
	MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	]
11. Update Database Configuration in settings.py (at the bottom of the file)
	import dj_database_url 
	prod_db  =  dj_database_url.config(conn_max_age=500)
	DATABASES['default'].update(prod_db)
12. Create application in Heroku from terminal (heroku create CMS)
13. Add your app domain name to ALLOWED_HOSTS in settings.py
	ALLOWED_HOSTS = ['CMS.herokuapp.com']
14. Initialize Git and connect your new app (or exiting one) to Heroku Git remote repository 
	git init
	heroku git:remote -a CMS
15. Add files to the staging area and commit changes
	git add .
	git commit -m "Initial commit"
16. Push the project to the remote repository (deploy app to Heroku)
	git push heroku master
17. If you get an error message with collectstatic, simply disable it by instructing Heroku to ignore running the manage.py collecstatic command during the deployment process.
	heroku config:set DISABLE_COLLECTSTATIC=1
18. Then, rerun
	git push heroku master
19. Migrate the database
	heroku run python manage.py migrate



 