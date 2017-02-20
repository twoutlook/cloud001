from django.db import models

class Smm(models.Model):
    DESIGNATION_CHOICES = (
       ('A356','A356'),
       ('A380','A380'),
       ('ADC12','ADC12'),
       ('Zamak3','Zamak3'),
       ('Zamak5','Zamak5'),
       ('Zn99.995','Zn99.995'),
    )

    MONTH_CHOICES = (
      (1,1),
       (2,2),
       (3,3),
       (4,4),
       (5,5),
       (6,6),
       (7,7),
       (8,8),
       (9,9),
       (10,10),
       (11,11),
       (12,12),

    )
    QUARTER_CHOICES = (
    (1,1),
       (2,2),
       (3,3),
       (4,4),
    )
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    # designation = models.CharField(max_length=32,verbose_name="牌号")
    designation = models.CharField(default='???', choices = DESIGNATION_CHOICES, max_length=32,verbose_name="牌号")
    pricedate = models.DateField(max_length=10,verbose_name="行情日期")
    priceavg = models.DecimalField(max_digits=9, decimal_places=2,verbose_name="平均价")
    yearnum = models.IntegerField(default=2016, verbose_name="年")
    monthnum = models.IntegerField(default=12, choices = MONTH_CHOICES,verbose_name="月")
    quarternum = models.IntegerField(default=4, choices = QUARTER_CHOICES, verbose_name="季")

    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.designation
    class Meta:
        verbose_name = "上海有色網"
        verbose_name_plural = "上海有色網"
        # http://stackoverflow.com/questions/23137420/enforcing-unique-combinations-of-fields-in-django
        # 同一牌號同一天只允許一筆資料
        unique_together = ('designation', 'pricedate')





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
        return str(self.id)
    class Meta:
        verbose_name = "生產工藝流程卡"
        verbose_name_plural = "生產工藝流程卡"

#
class Flowchartprocess(models.Model):
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    flowchart = models.ForeignKey(Flowchart, on_delete=models.CASCADE)
    a = models.IntegerField(blank=True, null=True,verbose_name="序號")
    b = models.CharField(default = '.', max_length=32,verbose_name="部門")
    c = models.CharField(max_length=32,verbose_name="工序")
    d = models.CharField(max_length=128,verbose_name="過程描述")
    e = models.CharField(default= ".", max_length=256,verbose_name="品質要求")
    f = models.CharField(blank=True, null=True,  max_length=32,verbose_name="設備")
    g = models.CharField(blank=True, null=True,  max_length=32,verbose_name="刀、治、模具")
    h = models.CharField(blank=True, null=True,  max_length=32,verbose_name="檢具")


    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.c
    class Meta:
        verbose_name = "流程"
        verbose_name_plural = "流程"

class Employee(models.Model):
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    # flowchart = models.ForeignKey(Flowchart, on_delete=models.CASCADE)
    # a = models.IntegerField(blank=True, null=True,verbose_name="序號")
    a = models.CharField(default = '.', max_length=32,verbose_name="工号")
    b = models.CharField(default = '.', max_length=32,verbose_name="姓名")
    c = models.CharField(max_length=128,verbose_name="部门名称")
    d = models.CharField(max_length=128,verbose_name="班组名称")
    e = models.CharField(default= ".", max_length=256,verbose_name="职位名称")
    f = models.CharField(default= ".", max_length=32,verbose_name="人员性质")


    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.a
    class Meta:
        verbose_name = "員工"
        verbose_name_plural = "員工"


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

class Trans(models.Model):
    # 日期  产品代码    产品品名    原料代码    原料品名    重量  数量  单据号码    备注
    MONTH_CHOICES = (
          ("2017-01","2017-01"),
          ("2017-02","2017-02"),
          ("2017-03","2017-03"),
          ("2017-04","2017-04"),
          ("2017-05","2017-05"),
          ("2017-06","2017-06"),
          ("2017-07","2017-07"),
          ("2017-08","2017-08"),
          ("2017-09","2017-09"),
          ("2017-10","2017-10"),
          ("2017-11","2017-11"),
          ("2017-12","2017-12"),
        )
    # CAT_CHOICES = (
    #       (1,"期初"),
    #       (2,"购进"),
    #       (3,"领用"),)
    CAT_CHOICES = (
          ("期初","期初"),
          ("购进","购进"),
          ("领用","领用"),
          # ("结存","结存"),
          )
    yrmonth = models.CharField("年月",default='2017-01',  max_length=7,choices = MONTH_CHOICES)

    # cat= models.IntegerField("类型",default=2,choices = CAT_CHOICES)
    cat=  models.CharField("类型",default='购进',  max_length=2,choices =CAT_CHOICES)
    
    a = models.DateField(blank=False, null=False,verbose_name="日期")
    b = models.CharField(default = '.', max_length=32,verbose_name="产品代码")
    c = models.CharField(default = '.', max_length=32,verbose_name="产品品名")
    d = models.CharField(default = '.', max_length=32,verbose_name="原料代码")
    e = models.CharField(default = '.', max_length=32,verbose_name="原料品名")
    h = models.CharField(default = '.', max_length=32,verbose_name="单据号码")
    i = models.CharField(default = '.', max_length=32,verbose_name="备注+")

    f =models.DecimalField("重量", max_digits=10, decimal_places=2)
    g =models.DecimalField("数量",default =0, max_digits=10, decimal_places=2)
    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.b
    class Meta:
        verbose_name = "原材料收发"
        verbose_name_plural = "原材料收发"

class Rpt(models.Model):
    # 日期  产品代码    产品品名    原料代码    原料品名    重量  数量  单据号码    备注
    MONTH_CHOICES = (
          ("2017-01","2017-01"),
          ("2017-02","2017-02"),
          ("2017-03","2017-03"),
          ("2017-04","2017-04"),
          ("2017-05","2017-05"),
          ("2017-06","2017-06"),
          ("2017-07","2017-07"),
          ("2017-08","2017-08"),
          ("2017-09","2017-09"),
          ("2017-10","2017-10"),
          ("2017-11","2017-11"),
          ("2017-12","2017-12"),
        )
    # CAT_CHOICES = (
    #       (1,"期初"),
    #       (2,"购进"),
    #       (3,"领用"),)
    # CAT_CHOICES = (
    #       ("期初","期初"),
    #       ("购进","购进"),
    #       ("领用","领用"),
    #       # ("结存","结存"),
    #       )
    yrmonth = models.CharField("年月",default='2017-01',  max_length=7,choices = MONTH_CHOICES)

    # cat= models.IntegerField("类型",default=2,choices = CAT_CHOICES)
    # cat=  models.CharField("类型",default='购进',  max_length=2,choices =CAT_CHOICES)
    
    # a = models.DateField(blank=False, null=False,verbose_name="日期")
    # b = models.CharField(default = '.', max_length=32,verbose_name="产品代码")
    # c = models.CharField(default = '.', max_length=32,verbose_name="产品品名")
    a = models.CharField(default = '.', max_length=32,verbose_name="原料代码")
    b = models.CharField(default = '.', max_length=32,verbose_name="原料品名")
    # h = models.CharField(default = '.', max_length=32,verbose_name="单据号码")
    # i = models.CharField(default = '.', max_length=32,verbose_name="备注+")

    e =models.DecimalField("期初", max_digits=10, decimal_places=2)
    g=models.DecimalField("购进", max_digits=10, decimal_places=2)
    i =models.DecimalField("领用", max_digits=10, decimal_places=2)
    k =models.DecimalField("结存", max_digits=10, decimal_places=2)
    
    # g =models.DecimalField("数量",default =0, max_digits=10, decimal_places=2)
    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.b
    class Meta:
        verbose_name = "原材料收发统计表"
        verbose_name_plural = "原材料收发统计表"

# 2017-02-17 SOP start

CAT_CHOICES = (
     ('ABM产品结构','ABM产品结构'),
     ('AIC多角贸易','AIC多角贸易'),
     ('AIM料件','AIM料件'),
     ('AIN库存','AIN库存'),
     ('AMR模具','AMR模具'),
     ('AOO集团架构','AOO集团架构'),
     ('APM采购','APM采购'),
     ('APS排程','APS排程'),
     ('AQC质量','AQC质量'),
     ('ASF生产','ASF生产'),
     ('AXM销售','AXM销售'),
     ('AZZ整体','AZZ整体'),
  )


class Sop(models.Model):
    cat = models.CharField(default='???', choices = CAT_CHOICES, max_length=32,verbose_name="CAT")
   
    code = models.CharField('流程编号',max_length=16)
    ver = models.CharField('版本',max_length=8)
    ver_date = models.DateField('修订日期')
    title = models.CharField(max_length=200)
    dept = models.CharField('负责单位',max_length=16)
    editor = models.CharField('修改人员',max_length=16)
    page_num = models.CharField('页次',max_length=16)
    intro = models.CharField('流程定义',max_length=200)
    is_active=models.BooleanField("是否活躍", default=True )
    # 2017-02-17
    # 和吳楠協議,流程圖命名以 FT_XXX.svg
    # 因此直接使用流程编号
    # diagram = models.CharField('流程图',max_length=200,default="mark002.svg")
    class Meta:
        verbose_name = "SOP "
        verbose_name_plural = "SOP "

class Sopitem(models.Model):
    sop= models.ForeignKey(Sop, models.SET_NULL, null=True)
    item_seq = models.IntegerField(default=0)
    item_text = models.CharField(max_length=600)
# 2017-02-17 SOP end    