Install Django:
-> pip install django

Django Start Prosjekt:
->django-admin startproject mysite
->C:\Users\guest1\Desktop\django-tutorials>django-admin startproject mysite

Run Server:
->C:\Users\guest1\Desktop\django-tutorials\mysite>C:/python27/python manage.py runserver

Url For Server:
-> http://127.0.0.1:8000/

Stop Server:
->CTRL + FN + pause


Create app: 
->C:\Users\guest1\Desktop\django-tutorials\mysite>C:/python27/python manage.py startapp webapp

//DATABASE::::##############################################################################################
Transer database to django:
->C:\Users\guest1\Desktop\django-tutorials\mysite>C:/python27/python manage.py migrate

->C:\Users\guest1\Desktop\django-tutorials\mysite>C:/python27/python manage.py makemigrations

only transfer database to specific app:
->C:\Users\guest1\Desktop\django-tutorials\mysite>C:/python27/python manage.py makemigrations blog

Check sql query who is sended:
->C:\Users\guest1\Desktop\django-tutorials\mysite>C:/python27/python manage.py sqlmigrate blog 0001

//END####################################################################### 

//Add database to administration panel:##############################################################################################
1. Open file admin.py inside blog:
Add the following:

from django.contrib import admin
from blog.models import Post
# Register your models here.

admin.site.register(Post) ( Post = name of the table in the database )
//END#######################################################################

CREATE USER:##############################################################################################
create super user:
->C:\Users\guest1\Desktop\django-tutorials\mysite>C:/python27/python manage.py createsuperuser
END##############################################################################################

##########################################################
##########################################################
##########################################################
Create database tables and rows:
# Create your models here.
class Post(models.Model): // create table
    title = models.CharField()  // create row
    body = models.TextField()
    date = models.DateTimeField()



// https://www.youtube.com/watch?v=W66TcJ7i-Bk&ebc=ANyPxKoALr6zBdc0zWBML3j1VfptBcH7ljDkyZOYmkHz7yvOxWcodIZTaACidpb15u_OkSHoZfqCAzuL9ya4DGvDRvaoR31wZQ



1. startproject mysite
2. startapp webapp
3. add app to settings
4. create file url at app
5. add app url to main url
6. Create model ( database)
7. create tables with manage.py makemigrations and then migrate
8. Add db to admin in admin.py in app
9. create superuser
