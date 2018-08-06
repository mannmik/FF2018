from django.db import models
from django.contrib.auth.models import User

class NFL_Team(models.Model):
    code = models.CharField(max_length = 4)
    fullName = models.CharField(max_length = 100)
    shortName = models.CharField(max_length = 50)
    byeWeek = models.IntegerField(default = -1)
    sos = models.IntegerField(default = -1)
    moneySOS = models.IntegerField(default = -1)
    wk10 = models.CharField(max_length = 4)
    wk11 = models.CharField(max_length = 4)
    wk12 = models.CharField(max_length = 4)
    wk13 = models.CharField(max_length = 4)
    wk14 = models.CharField(max_length = 4)
    wk15 = models.CharField(max_length = 4)
    wk16 = models.CharField(max_length = 4)
    qb_SOS = models.IntegerField(default = -1)
    rb_SOS = models.IntegerField(default = -1)
    wr_SOS = models.IntegerField(default = -1)
    te_SOS = models.IntegerField(default = -1)
    qb_Playoff = models.IntegerField(default = -1)
    rb_Playoff = models.IntegerField(default = -1)
    wr_Playoff = models.IntegerField(default = -1)
    te_Playoff = models.IntegerField(default = -1) 

    def __str__(self):
        return self.code

   


    


    