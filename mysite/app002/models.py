from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import datetime
from django.utils import timezone

# class Customer(models.Model):
#     field1 = models.CharField(max_length=200)
#     field2 = models.CharField(max_length=200)
#     field3 = models.CharField(max_length=200)
#     field4 = models.CharField(max_length=200)
#     field5 = models.CharField(max_length=200)
#     def __str__(self):
#         return self.field1


class Item000(models.Model):
    field1 = models.CharField(max_length=200)
    field2 = models.CharField(max_length=200)
    field3 = models.CharField(max_length=200)
    field4 = models.CharField(max_length=200)
    field5 = models.CharField(max_length=200)
    field6 = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.field1

class T01(models.Model):
    f02 = models.CharField("B",max_length=30)
    f03 = models.CharField("C",max_length=30)
    f04 = models.CharField("D",max_length=30)
    def __str__(self):
        return self.f02
