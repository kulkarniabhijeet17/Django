This example includes referring external template, loop, if...else, MTV pattern, writing models, database migrations.

django-admin startproject SecondDjangoProject
python manage.py startapp TrevelloApp

Download external templates from: https://github.com/sahaib9747/TeluskoTutorial-TravelloTheme
Create "static" folder inside project (SecondDjangoProject), copy images, js, plugins, styles folder into it
Copy index.html into templates folder.

Make entry for this application inside setting.py file of project under INSTALLED_APPS
Register templates (html files) inside setting.py file of project within TEMPLATES as below-
    'DIRS': [os.path.join(BASE_DIR, 'templates')]
Make entry for static folder inside settings.py file of project as below-
	STATIC_URL = 'static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
Mention url path for this application inside urls.py as below-
    path(‘’, include(‘TrevelloApp.url’))
Create urls.py inside TrevelloApp application and mention urlpatterns:
    urlpatterns = [
        path('', views.index, name='index')
    ]
Modify path for src and href in index.html as below-
{% load static %}
{% static 'static/images' as baseUrl %}
<link rel="stylesheet" type="text/css" href="{% static 'styles/bootstrap4/bootstrap.min.css' %}">

Run below commands-
python manage.py collectstatic
python manage.py migrate

Install Pillow module to create models
pip install Pillow --user

Run project: python manage.py runserver
Hit URL: http://127.0.0.1:8000/