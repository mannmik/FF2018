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

    def __str__(self):
        return self.code

    def set_code(self, teamcode):
        self.code = teamcode

    def set_fullName(self, fname):
        self.fullName = fname
    
    def set_byeWeek(self, bye):
        self.byeWeek = byeWeek

    def set_code(self, sname):
        self.shortName = sname
    
    def get_code(self):
        return self.code

    def get_fullName(self):
        return self.fullName

    def get_shortName(self):
        return self.shortName
    


    