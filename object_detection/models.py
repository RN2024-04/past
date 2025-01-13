from django.db import models


class PeopleReg(models.Model):
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    password2=models.CharField(max_length=150)
    USERNAME_FIELD = 'username'

# cd detection_site
# python manage.py makemigrations
# python manage.py migrate

