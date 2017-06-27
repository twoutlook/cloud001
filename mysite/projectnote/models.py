from django.db import models



# 2017-05-11 技術梗…
class TechNote(models.Model):
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    # flowchart = models.ForeignKey(Flowchart, on_delete=models.CASCADE)
    # a = models.IntegerField(blank=True, null=True,verbose_name="序號")
    a = models.CharField(default = 'BPM開發', max_length=32,verbose_name="類別")
    b = models.CharField(default = '.', max_length=32,verbose_name="姓名")
    c = models.CharField(max_length=512,verbose_name="內容")


    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.c
    class Meta:
        verbose_name = "技術梗"
        verbose_name_plural = "技術梗"

# 2017-05-27 …T100问题处理进度追踪
class T100Todo(models.Model):
    # 项次	提报时间	富鈦提报人	问题类型		问题点

    # num = models.IntegerField(default=0,verbose_name="第幾式")
    # flowchart = models.ForeignKey(Flowchart, on_delete=models.CASCADE)
    # a = models.IntegerField(blank=True, null=True,verbose_name="序號")
    a = models.IntegerField(default = 0,verbose_name="项次")
    b = models.DateField(blank=True, null=True, max_length=32,verbose_name="提报时间")
    c = models.CharField(default = '.', max_length=32,verbose_name="富鈦提报人")
    d=models.CharField(default = '.', max_length=32,verbose_name="问题类型")
    e=models.CharField(default = '.', max_length=32,verbose_name="鼎捷责任人")
    f = models.CharField(default = '.',max_length=512,verbose_name="问题点")
    g = models.CharField(default = '.',max_length=512,verbose_name="问题点示例")
    h = models.CharField(default = '.',max_length=512,verbose_name="讨论结果")
    i = models.CharField(default = '.',max_length=512,verbose_name="顾问回复处理结果")
    j = models.CharField(default = '.',max_length=512,verbose_name="验证结果")
    # k = models.CharField(default = '.', max_length=32,verbose_name="计划完成日期")
    # l = models.CharField(default = '.', max_length=32,verbose_name="实际完成日期")
    k = models.DateField(blank=True, null=True, max_length=32,verbose_name="计划完成日期")
    l = models.DateField(blank=True, null=True, max_length=32,verbose_name="实际完成日期")
    m = models.CharField(default = '.', max_length=32,verbose_name="用户确认")


    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.f
    class Meta:
        verbose_name = "T100问题处理进度追踪"
        verbose_name_plural = "T100问题处理进度追踪"



# 2017-06-23 …
# 张一翔/张韬/吴楠
class TrackT100(models.Model):
    # 项次	提报时间	富鈦提报人	问题类型		问题点
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    # flowchart = models.ForeignKey(Flowchart, on_delete=models.CASCADE)
    # a = models.IntegerField(blank=True, null=True,verbose_name="序號")
    a = models.IntegerField(default = 0,verbose_name="序号")
    b = models.DateField(blank=True, null=True, max_length=32,verbose_name="提报时间")
    c = models.CharField(default = '.', max_length=32,verbose_name="提报人员")
    d = models.CharField(default = '.', max_length=32,verbose_name="鼎捷责任人")
    e = models.CharField(default = '.', max_length=32,verbose_name="问题分类")
    f = models.CharField(default = '.',max_length=512,verbose_name="问题描述")
    g = models.CharField(default = '.',max_length=512,verbose_name="问题分析")
    h = models.CharField(default = '.',max_length=512,verbose_name="解决方案")
    i = models.DateField(blank=True, null=True, max_length=32,verbose_name="计划完成时间")
    j = models.DateField(blank=True, null=True, max_length=32,verbose_name="实际完成时间")
    k = models.CharField(default = '.',max_length=512,verbose_name="进度状态")
    l = models.CharField(default = '.',max_length=512,verbose_name="用户确认")
    m = models.CharField(default = '.', max_length=32,verbose_name="备注")


    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.f
    class Meta:
        verbose_name = "全制程--T100问题追踪表"
        verbose_name_plural = "全制程--T100问题追踪表"

# 2017-06-23 …
# 张一翔/张韬/吴楠
class TrackReport01(models.Model):
    	# 项次	需求类型	作业程序	业务需求	讨论结果	讨论日期	确认日期	客制否	BPM	工时	备注	客制状态	客制完成否


    # 项次	提报时间	富鈦提报人	问题类型		问题点
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    # flowchart = models.ForeignKey(Flowchart, on_delete=models.CASCADE)
    # a = models.IntegerField(blank=True, null=True,verbose_name="序號")
    a = models.IntegerField(default = 0,verbose_name="项次")
    b = models.CharField(default = '.', max_length=32,verbose_name="需求类型")
    c = models.CharField(default = '.', max_length=32,verbose_name="作业程序")
    d = models.CharField(default = '.', max_length=32,verbose_name="业务需求")
    e = models.CharField(default = '.', max_length=32,verbose_name="讨论结果")
    f = models.DateField(blank=True, null=True, max_length=32,verbose_name="讨论日期")
    g = models.DateField(blank=True, null=True, max_length=32,verbose_name="确认日期")
    h = models.CharField(default = '.',max_length=512,verbose_name="客制否")
    i = models.CharField(default = '.',max_length=512,verbose_name="BPM")
    j = models.IntegerField(default = 0,verbose_name="工时")
    k = models.CharField(default = '.',max_length=512,verbose_name="备注")
    l = models.CharField(default = '.',max_length=512,verbose_name="客制状态")
    m = models.CharField(default = '.', max_length=32,verbose_name="客制完成否")


    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.d
    class Meta:
        verbose_name = "全制程--报表-业务"
        verbose_name_plural = "全制程--报表-业务"



# 2017-06-23 …
# 张一翔/张韬/吴楠
class TrackReport00(models.Model):
    	# 项次	需求类型	作业程序	业务需求	讨论结果	讨论日期	确认日期	客制否	BPM	工时	备注	客制状态	客制完成否


    # 项次	提报时间	富鈦提报人	问题类型		问题点
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    # flowchart = models.ForeignKey(Flowchart, on_delete=models.CASCADE)
    # a = models.IntegerField(blank=True, null=True,verbose_name="序號")
    deptId = models.CharField(default = '0000', max_length=16,verbose_name="DEPT_ID")
    dept = models.CharField(default = '.', max_length=16,verbose_name="DEPT")

    a = models.IntegerField(default = 0,verbose_name="项次")
    b = models.CharField(default = '.', max_length=32,verbose_name="需求类型")
    c = models.CharField(default = '.', max_length=32,verbose_name="作业程序")
    d = models.CharField(default = '.', max_length=32,verbose_name="业务需求")
    e = models.CharField(default = '.', max_length=32,verbose_name="讨论结果")
    f = models.DateField(blank=True, null=True, max_length=32,verbose_name="讨论日期")
    g = models.DateField(blank=True, null=True, max_length=32,verbose_name="确认日期")
    h = models.CharField(default = '.',max_length=512,verbose_name="盤點現況")
    i = models.CharField(default = '.',max_length=512,verbose_name="BPM")
    j = models.IntegerField(default = 0,verbose_name="工时")
    k = models.CharField(default = '.',max_length=512,verbose_name="备注")
    l = models.CharField(default = '.',max_length=512,verbose_name="客制状态")
    m = models.CharField(default = '.', max_length=32,verbose_name="客制完成否")


    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.d
    class Meta:
        verbose_name = "全制程--报表-业务-and others"
        verbose_name_plural = "全制程--报表-业务-and others"

# 2017-06-23 …
# 张一翔/张韬/吴楠
class TrackPda(models.Model):
    # 项次	提报时间	富鈦提报人	问题类型		问题点
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    # flowchart = models.ForeignKey(Flowchart, on_delete=models.CASCADE)
    # a = models.IntegerField(blank=True, null=True,verbose_name="序號")
    a = models.IntegerField(default = 0,verbose_name="序号")
    b = models.DateField(blank=True, null=True, max_length=32,verbose_name="提报时间")
    c = models.CharField(default = '.', max_length=32,verbose_name="提报人员")
    d = models.CharField(default = '.', max_length=32,verbose_name="鼎捷责任人")
    e = models.CharField(default = '.', max_length=32,verbose_name="问题分类")
    f = models.CharField(default = '.',max_length=512,verbose_name="问题描述")
    g = models.CharField(default = '.',max_length=512,verbose_name="问题分析")
    h = models.CharField(default = '.',max_length=512,verbose_name="解决方案")
    i = models.DateField(blank=True, null=True, max_length=32,verbose_name="计划完成时间")
    j = models.DateField(blank=True, null=True, max_length=32,verbose_name="实际完成时间")
    k = models.CharField(default = '.',max_length=512,verbose_name="进度状态")
    l = models.CharField(default = '.',max_length=512,verbose_name="用户确认")
    m = models.CharField(default = '.', max_length=32,verbose_name="备注")


    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.f
    class Meta:
        verbose_name = "全制程--智能物流问题追踪表"
        verbose_name_plural = "全制程--智能物流问题追踪表"

# 2017-06-23 …
# 张韬/张一翔/Mark
class TrackT100Report(models.Model):
    # 项次	提报时间	富鈦提报人	问题类型		问题点
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    # flowchart = models.ForeignKey(Flowchart, on_delete=models.CASCADE)
    # a = models.IntegerField(blank=True, null=True,verbose_name="序號")
    a = models.CharField(default = '.', max_length=32,verbose_name="序号")
    b = models.DateField(blank=True, null=True, max_length=32,verbose_name="提报时间")
    c = models.CharField(default = '.', max_length=32,verbose_name="提报人员")
    d = models.CharField(default = '.', max_length=32,verbose_name="部门")
    e = models.CharField(default = '.', max_length=32,verbose_name="T100作业")
    f = models.CharField(default = '.',max_length=512,verbose_name="repot名称")
    g = models.CharField(default = '.',max_length=512,verbose_name="功能简述")
    h = models.CharField(default = '.',max_length=512,verbose_name="SQL语句")
    i = models.DateField(blank=True, null=True, max_length=32,verbose_name="计划完成时间")
    j = models.DateField(blank=True, null=True, max_length=32,verbose_name="实际完成时间")
    k = models.CharField(default = '.',max_length=512,verbose_name="进度状态")
    l = models.CharField(default = '.',max_length=512,verbose_name="用户确认")
    m = models.CharField(default = '备注', max_length=512,verbose_name="备注")


    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.g
    class Meta:
        verbose_name = "全制程--T100报表现况"
        verbose_name_plural = "全制程--T100报表现况"






# class T100Todo2(models.Model):
#     # 项次	提报时间	富鈦提报人	问题类型		问题点
#
#     # num = models.IntegerField(default=0,verbose_name="第幾式")
#     # flowchart = models.ForeignKey(Flowchart, on_delete=models.CASCADE)
#     # a = models.IntegerField(blank=True, null=True,verbose_name="序號")
#     a = models.IntegerField(default = '.', max_length=32,verbose_name="项次")
#     b = models.DateField(blank=True, null=True, max_length=32,verbose_name="提报日期")
#     c = models.CharField(default = '.', max_length=32,verbose_name="提报人员")
#     d=models.CharField(default = '.', max_length=32,verbose_name="鼎捷责任人")
#     e=models.CharField(default = '.', max_length=32,verbose_name="需求类型")
#     f = models.CharField(default = '.',max_length=512,verbose_name="需求")
#     g = models.CharField(default = '.',max_length=512,verbose_name="表单格式打包")
#     h = models.CharField(default = '.',max_length=512,verbose_name="讨论结果")
#     i = models.CharField(default = '.',max_length=512,verbose_name="顾问回复处理结果")
#     j = models.CharField(default = '.',max_length=512,verbose_name="计划需求确认完成日期")
#     # k = models.CharField(default = '.', max_length=32,verbose_name="计划完成日期")
#     # l = models.CharField(default = '.', max_length=32,verbose_name="实际完成日期")
#     k = models.DateField(blank=True, null=True, max_length=32,verbose_name="计划开发完成日期")
#     l = models.DateField(blank=True, null=True, max_length=32,verbose_name="实际完成日期")
#     m = models.CharField(default = '.', max_length=32,verbose_name="备注")
#
#
#     # remarks = models.CharField(max_length=200)
#     def __str__(self):
#         return self.f
#     class Meta:
#         verbose_name = "各部门需求处理进度追踪"
#         verbose_name_plural = "各部门需求处理进度追踪"


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

class Sopdata(models.Model):
    DATACAT_CHOICES = (
     ('整体','整体'),
     ('制造','制造'),
    )

    cat = models.CharField('分類',max_length=16, choices=DATACAT_CHOICES, default='整体')
    seq = models.IntegerField('序號',default=0)
    sys = models.CharField('系统',max_length=16)
    procedure = models.CharField('作业',max_length=16)
    program = models.CharField('程序',max_length=16,null=True)
    files = models.CharField('档案代号',max_length=255,null=True)
    notes = models.CharField('注意事项',max_length=255,null=True)
    recommend = models.CharField('建议',max_length=255,null=True)
    deadline = models.DateField('应完成日期', null=True)
    responsible = models.CharField('负责人员',max_length=64,null=True)
    supporter = models.CharField('来源单位、支持单位',max_length=64,null=True)
    is_required = models.BooleanField('必要',default=True)
    method = models.CharField('建置方式',max_length=16,null=True)
    remarks = models.CharField('备注',max_length=255,null=True)
    by_default = models.CharField('建议负责人员',max_length=64, null=True)




    def __str__(self):
        return self.procedure

# 参数及基本数据建置进度计划表
    class Meta:
        verbose_name = "参数及基本数据建置进度计划表"
        verbose_name_plural = "参数及基本数据建置进度计划表"

class Dept(models.Model):
    dept_name = models.CharField('部門',max_length=16)
    order_seq = models.IntegerField(default=0)
    def __str__(self):
        return self.dept_name

class Cat(models.Model):
    cat_name = models.CharField('分類',max_length=16)
    cat_seq = models.IntegerField(default=0)
    def __str__(self):
        return self.cat_name




class Sop(models.Model):
    dept2= models.ForeignKey(Dept, models.SET_NULL, null=True)
    cat2= models.ForeignKey(Cat, models.SET_NULL, null=True)

    cat = models.CharField(default='???', choices = CAT_CHOICES, max_length=32,verbose_name="CAT")

    code = models.CharField('流程编号',max_length=16)
    ver = models.CharField('版本',max_length=8)
    ver_date = models.DateField('修订日期')
    title = models.CharField(max_length=200)
    dept = models.CharField('负责单位',max_length=16)
    editor = models.CharField('修改人员',max_length=16)
    by2 = models.CharField('审核人员',max_length=16,default='...')
    page_num = models.CharField('页次',max_length=16)
    intro = models.CharField('流程定义',max_length=200)
    is_bpm=models.BooleanField("是否BPM", default=False )
    is_active=models.BooleanField("是否活躍", default=True )
    # 2017-02-17
    # 和吳楠協議,流程圖命名以 FT_XXX.svg
    # 因此直接使用流程编号
    # diagram = models.CharField('流程图',max_length=200,default="mark002.svg")
    class Meta:
        verbose_name = "SOP "
        verbose_name_plural = "SOP "
    def __str__(self):
        return self.code+"_"+self.title

class Dailywork(models.Model):
    empe_name = models.CharField('姓名',max_length=16)
    work_date = models.DateField('日期')
    work_brief = models.CharField('工作要點',max_length=512)
    work_desc = models.CharField('工作內容',max_length=512)
    remarks = models.CharField('TODO',max_length=512)
    class Meta:
        verbose_name = "每人每日工作記要"
        verbose_name_plural = "每人每日工作記要"
    def __str__(self):
        return self.empe_name+"_"+self.work_brief


# 2017-03-20
# woring together with 盼盼 & 婷婷
class Bpm(models.Model):
    dept_name = models.CharField('部门',max_length=16)
    sop_name = models.CharField('SOP名称',max_length=512)
    bpm_type = models.CharField('单据类型',max_length=512, default=".")
    note1 = models.CharField('SOP',max_length=512, default=".")
    note2 = models.CharField('TIOO运行程序',max_length=512, default=".")
    note3 = models.CharField('T100表单名称',max_length=512, default=".")


    dev_by= models.CharField('建议开发人员',max_length=512, default=".")
    man_hr = models.IntegerField('预估实施工时（h）',default=0)

    #
    to_print= models.CharField('打印需求',max_length=512, default=".")
    qry_t100= models.CharField('查询T100数据',max_length=512, default=".")
    wait_t100= models.CharField('需待T100客制',max_length=512, default=".")
    concern= models.CharField('BPM-T100集成相关问题',max_length=512, default=".")

    form_name= models.CharField('BPM表单名称',max_length=512, default=".")
    process_name= models.CharField('流程名称',max_length=512, default=".")
    step1_by= models.CharField('UI',max_length=512, default=".")
    step2_by= models.CharField('JS',max_length=512, default=".")
    step3_by= models.CharField('流程外形',max_length=512, default=".")
    step4_by= models.CharField('流程代码',max_length=512, default=".")

    # NOTE
    # 2017-03-21 婷婷 feedback: on page admin, failed to save if date is blank
    complete_date = models.DateField("完成日期", null=True,blank=True)
    class Meta:
        verbose_name = "BPM列表"
        verbose_name_plural = "BPM列表"
    def __str__(self):
        return self.dept_name+"_"+self.sop_name
    class Meta:
        ordering = ('dept_name','sop_name',)


class Sopitem(models.Model):
    sop= models.ForeignKey(Sop, models.SET_NULL, null=True)
    item_seq = models.IntegerField(default=0)
    item_text = models.CharField(max_length=600)
# 2017-02-17 SOP end



class T100(models.Model):
    sop= models.ForeignKey(Sop, models.SET_NULL, null=True)
    code = models.CharField('運行程序',max_length=16)
    name = models.CharField('運行程序名稱',max_length=64)

class T100item(models.Model):
    t100= models.ForeignKey(T100, models.SET_NULL, null=True)
    item_seq = models.IntegerField(default=0)
    item_text = models.CharField(max_length=600)

class Prog(models.Model):
    code = models.CharField('運行程序',max_length=16, unique=True)
    name = models.CharField('運行程序名稱',max_length=64)
    def __str__(self):
        # return "【"+self.code+"】"+self.name
        return self.code+" "+self.name
        # 【品保】


class Drill (models.Model):
    code = models.CharField('演練代碼',max_length=16)
    name = models.CharField('演練名稱',max_length=64)

class Drillstep (models.Model):
    drill= models.ForeignKey(Drill, models.SET_NULL, null=True)
    seq = models.IntegerField(default=0)
    prog= models.ForeignKey(Prog, models.SET_NULL, null=True)
    note = models.CharField('筆記',max_length=512)
    problem = models.CharField('異常',max_length=512,default='...')
    sample = models.CharField('單號',max_length=512,default='...')

    class Meta:
        ordering = ('drill','seq',)

class SqlStatement(models.Model):
    prj = models.CharField('項目',default="monitor001",max_length=512)
    seq = models.IntegerField('序號',default=0)
    title = models.CharField('標題',max_length=512,default=".")
    sql = models.CharField('SQL語句',max_length=512,default=".",null=True, blank=True)
    lbl = models.CharField('Label',max_length=512,default=".",null=True, blank=True)
    vname = models.CharField('View Name',max_length=512,default=".",null=True, blank=True)
    vcode = models.CharField('View定義',max_length=512,default=".",null=True, blank=True)
    prog = models.CharField('T100運行程序',max_length=512,default=".",null=True, blank=True)
    # lbl_zh = models.CharField('Label中文',max_length=512,default=".",null=True, blank=True)
    remarks = models.CharField('備註',max_length=512,default="...")
    is_active = models.BooleanField('是否活躍',default=False)
    class Meta:
        ordering = ('prj','seq',)
    def __str__(self):
        # return "【"+self.code+"】"+self.name
        return self.prj+" "+str(self.seq)+" "+self.title
        # 【品保】
