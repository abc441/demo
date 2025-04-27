# models.py
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'

class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    sex = models.BooleanField(default=False)