"""
Definition of models.
"""
from django.db import models

# Create your models here.
class dblist(models.Model):
    daiban = models.CharField(max_length=255)
    yiwancheng = models.CharField(max_length=255)

    def _str_(self):
        return self.daiban


class wenzhang(models.Model):
    nid = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)


    def _str_(self):
        return self.title






    