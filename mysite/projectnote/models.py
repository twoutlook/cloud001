from django.db import models


# Create your models here.
class Note(models.Model):
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    # flowchart = models.ForeignKey(Flowchart, on_delete=models.CASCADE)
    # a = models.IntegerField(blank=True, null=True,verbose_name="序號")
    date1 = models.DateField(blank=True, null=True,verbose_name="問題日期")
    where = models.CharField(default = '.', max_length=512,verbose_name="問題位置")
    whereurl = models.URLField(blank=True, null=True, max_length=512,verbose_name="URL")
    note = models.CharField(default = '.', max_length=512,verbose_name="問題描述")
    date2 = models.DateField(blank=True, null=True,verbose_name="解決日期")
    fix = models.CharField(default = '.', max_length=512,verbose_name="解決概要")
    tag = models.CharField(blank=True, null=True, max_length=512,verbose_name="標記")
    # c = models.CharField(max_length=32,verbose_name="工序")
    # d = models.CharField(max_length=128,verbose_name="過程描述")
    # e = models.CharField(default= ".", max_length=256,verbose_name="品質要求")
    # f = models.CharField(blank=True, null=True,  max_length=32,verbose_name="設備")
    # g = models.CharField(blank=True, null=True,  max_length=32,verbose_name="刀、治、模具")
    # h = models.CharField(blank=True, null=True,  max_length=32,verbose_name="檢具")
