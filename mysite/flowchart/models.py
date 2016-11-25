from django.db import models


# Create your models here.
class Flowchart(models.Model):
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    part_name = models.CharField(max_length=32,verbose_name="品名")
    c1 = models.CharField(default= ".", max_length=32,verbose_name="模號")
    c2 = models.CharField(default= ".", max_length=32,verbose_name="模穴")
    e1 = models.CharField(default= ".", max_length=32,verbose_name="圖面版本")
    e2 = models.CharField(default= ".", max_length=32,verbose_name="表面等級")
    g1 = models.CharField(default= ".", max_length=32,verbose_name="版序")
    g2 = models.CharField(default= ".", max_length=32,verbose_name="材質")
    by1= models.CharField(default= ".", max_length=32,verbose_name="編制")
    by1date= models.DateField(  blank=True, null=True,verbose_name="編制日期")
    by2= models.CharField( blank=True, null=True, max_length=32,verbose_name="審核")
    by2date= models.DateField( blank=True, null=True, verbose_name="審核日期")
    by3= models.CharField( blank=True, null=True, max_length=32,verbose_name="批准")
    by3date= models.DateField( blank=True, null=True, verbose_name="批准日期")


    cust_name = models.CharField(max_length=32,verbose_name="客戶名稱")
    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.part_name
    class Meta:
        verbose_name = "生產工藝流程卡"
        verbose_name_plural = "生產工藝流程卡"

#
class Flowchartprocess(models.Model):
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    flowchart = models.ForeignKey(Flowchart, on_delete=models.CASCADE)
    a = models.IntegerField(blank=True, null=True, verbose_name="序號")
    b = models.CharField(default = '.', max_length=32,verbose_name="部門")
    c = models.CharField(max_length=32,verbose_name="工序")
    d = models.CharField(max_length=128,verbose_name="過程描述")
    e = models.CharField(default= ".", max_length=256,verbose_name="品質要求")
    f = models.CharField(default= ".", max_length=32,verbose_name="設備")
    g = models.CharField(default= ".", max_length=32,verbose_name="刀、治、模具")
    h = models.CharField(default= ".", max_length=32,verbose_name="檢具")


    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.c
    class Meta:
        verbose_name = "流程"
        verbose_name_plural = "流程"
