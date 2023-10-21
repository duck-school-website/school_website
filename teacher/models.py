from django.db import models

class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pswd = models.CharField(max_length=255)
    


