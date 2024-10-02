from django.db import models

# Create your models here.
class LoginData(models.Model):
    url_name = models.CharField(max_length=100)
    login_url = models.CharField(max_length=200)
    login_id = models.CharField(max_length=150)
    login_pw = models.CharField(max_length=150)
