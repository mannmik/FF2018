from django.db import models

class UserAccount(models.Model):
    userId = models.AutoField(primary_key = True)
    usrEmail = models.TextField()
    usrPassword = models.CharField(max_length = 25)
    usrName = models.CharField(max_length = 25)
