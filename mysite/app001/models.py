from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import datetime
from django.utils import timezone



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



# 2016-11-24
class T01(models.Model):
    f02 = models.CharField("B",max_length=30)
    f03 = models.CharField("C",max_length=30)
    f04 = models.CharField("D",max_length=30)
    def __str__(self):
        return self.f02


# class Customer(models.Model):
#     field1 = models.CharField(max_length=200)
#     field2 = models.CharField(max_length=200)
#     field3 = models.CharField(max_length=200)
#     field4 = models.CharField(max_length=200)
#     field5 = models.CharField(max_length=200)
#     def __str__(self):
#         return self.field1

class Spec(models.Model):
    field1 = models.IntegerField()
    field2 = models.CharField(max_length=200,verbose_name="規格說明")
    field3 = models.CharField(max_length=200,null=True)
    # field4 = models.CharField(max_length=200)
    # field5 = models.CharField(max_length=200)
    def __str__(self):
        return self.field2
class Cust(models.Model):
    field1 = models.IntegerField()
    field2 = models.CharField(max_length=200)
    field3 = models.CharField(max_length=200,null=True)
    # field4 = models.CharField(max_length=200)
    # field5 = models.CharField(max_length=200)
    def __str__(self):
        return self.field2


class Item000(models.Model):
    field1 = models.CharField(max_length=200)
    field2 = models.CharField(max_length=200)
    field3 = models.CharField(max_length=200)
    field4 = models.CharField(max_length=200)
    field5 = models.CharField(max_length=200)
    field6 = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.field1

class Item001(models.Model):
    field1 = models.CharField(primary_key=True,max_length=200,verbose_name="幾號機")
    field1a = models.CharField(default=".",max_length=200,verbose_name="噸位")
    r01c6 = models.CharField(default=".",max_length=99,verbose_name="人員")
    r01c8 = models.CharField(default=".",max_length=99,verbose_name="日期")


#--- code1 for model.py (start) -----

    r03c3 = models.CharField(default=".",max_length=99,verbose_name="格林柱-零件")
    r03c4 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度一")
    r03c5 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度二")
    r03c6 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度三")
    r03c7 = models.CharField(default=".",max_length=99,verbose_name="格林柱-備註說明")
    r04c3 = models.CharField(default=".",max_length=99,verbose_name="機架底座-零件")
    r04c4 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度一")
    r04c5 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度二")
    r04c6 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度三")
    r04c7 = models.CharField(default=".",max_length=99,verbose_name="機架底座-備註說明")
    r05c3 = models.CharField(default=".",max_length=99,verbose_name="模板-零件")
    r05c4 = models.CharField(default=".",max_length=99,verbose_name="模板-進度一")
    r05c5 = models.CharField(default=".",max_length=99,verbose_name="模板-進度二")
    r05c6 = models.CharField(default=".",max_length=99,verbose_name="模板-進度三")
    r05c7 = models.CharField(default=".",max_length=99,verbose_name="模板-備註說明")
    r06c3 = models.CharField(default=".",max_length=99,verbose_name="合模-零件")
    r06c4 = models.CharField(default=".",max_length=99,verbose_name="合模-進度一")
    r06c5 = models.CharField(default=".",max_length=99,verbose_name="合模-進度二")
    r06c6 = models.CharField(default=".",max_length=99,verbose_name="合模-進度三")
    r06c7 = models.CharField(default=".",max_length=99,verbose_name="合模-備註說明")
    r07c3 = models.CharField(default=".",max_length=99,verbose_name="間隙-零件")
    r07c4 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度一")
    r07c5 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度二")
    r07c6 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度三")
    r07c7 = models.CharField(default=".",max_length=99,verbose_name="間隙-備註說明")
    r08c3 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-零件")
    r08c4 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度一")
    r08c5 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度二")
    r08c6 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度三")
    r08c7 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-備註說明")
    r10c3 = models.CharField(default=".",max_length=99,verbose_name="油管-零件")
    r10c4 = models.CharField(default=".",max_length=99,verbose_name="油管-進度一")
    r10c5 = models.CharField(default=".",max_length=99,verbose_name="油管-進度二")
    r10c6 = models.CharField(default=".",max_length=99,verbose_name="油管-進度三")
    r10c7 = models.CharField(default=".",max_length=99,verbose_name="油管-備註說明")
    r11c3 = models.CharField(default=".",max_length=99,verbose_name="過濾-零件")
    r11c4 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度一")
    r11c5 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度二")
    r11c6 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度三")
    r11c7 = models.CharField(default=".",max_length=99,verbose_name="過濾-備註說明")
    r12c3 = models.CharField(default=".",max_length=99,verbose_name="油箱-零件")
    r12c4 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度一")
    r12c5 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度二")
    r12c6 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度三")
    r12c7 = models.CharField(default=".",max_length=99,verbose_name="油箱-備註說明")
    r13c3 = models.CharField(default=".",max_length=99,verbose_name="馬達-零件")
    r13c4 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度一")
    r13c5 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度二")
    r13c6 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度三")
    r13c7 = models.CharField(default=".",max_length=99,verbose_name="馬達-備註說明")
    r15c3 = models.CharField(default=".",max_length=99,verbose_name="潤滑-零件")
    r15c4 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度一")
    r15c5 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度二")
    r15c6 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度三")
    r15c7 = models.CharField(default=".",max_length=99,verbose_name="潤滑-備註說明")
    r16c3 = models.CharField(default=".",max_length=99,verbose_name="氮氣-零件")
    r16c4 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度一")
    r16c5 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度二")
    r16c6 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度三")
    r16c7 = models.CharField(default=".",max_length=99,verbose_name="氮氣-備註說明")
    r17c3 = models.CharField(default=".",max_length=99,verbose_name="電控-零件")
    r17c4 = models.CharField(default=".",max_length=99,verbose_name="電控-進度一")
    r17c5 = models.CharField(default=".",max_length=99,verbose_name="電控-進度二")
    r17c6 = models.CharField(default=".",max_length=99,verbose_name="電控-進度三")
    r17c7 = models.CharField(default=".",max_length=99,verbose_name="電控-備註說明")
    r18c3 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-零件")
    r18c4 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度一")
    r18c5 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度二")
    r18c6 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度三")
    r18c7 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-備註說明")
    r19c3 = models.CharField(default=".",max_length=99,verbose_name="自動取出-零件")
    r19c4 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度一")
    r19c5 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度二")
    r19c6 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度三")
    r19c7 = models.CharField(default=".",max_length=99,verbose_name="自動取出-備註說明")
    r20c3 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-零件")
    r20c4 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度一")
    r20c5 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度二")
    r20c6 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度三")
    r20c7 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-備註說明")

#--- code1 for model.py (end) -----


    def __str__(self):
        return self.field1
# 客戶	品名	欠料量	欠備庫量	客訴量	模具壽命?%	客戶	品名	欠料量	欠備庫量	客訴量	模具壽命?%

class Item003v2(models.Model):
    CHOICE01 = (
        ('---','---'),
        ('正常','正常'),
        ('磨損','磨損'),
        ('無法修復','無法修復'),
    )
    CHOICE02 = (
        ('---','---'),
        ('正常','正常'),
        ('磨損','磨損'),
        ('裂縫','裂縫'),
        ('磨損、裂縫','磨損、裂縫'),
    )
    CHOICE03 = (
        ('---','---'),
        ('正常','正常'),
        ('平面變型','平面變型'),
        ('無法修復','無法修復'),
    )
    CHOICE04 = (
        ('---','---'),
        ('正常','正常'),
        ('平面變型','平面變型'),
        ('無法修復','無法修復'),
    )
    CHOICE05 = (
        ('---','---'),
        ('正常','正常'),
        ('合模缸漏油','合模缸漏油'),
        ('合模缸螺旋斷裂','合模缸螺旋斷裂'),
        ('合模活塞磨損','合模活塞磨損'),
        ('無法修復','無法修復'),
    )
    CHOICE06 = (
        ('---','---'),
        ('正常','正常'),
        ('磨損','磨損'),
        ('無法修復','無法修復'),
    )
    CHOICE07 = (
        ('---','---'),
        ('正常','正常'),
        ('磨損','磨損'),
        ('斷裂','斷裂'),
        ('無法修復','無法修復'),
    )
    CHOICE08 = (
        ('---','---'),
        ('正常','正常'),
        ('開關損壞','開關損壞'),
        ('線路不通','線路不通'),
        ('無法修復','無法修復'),
    )
    CHOICE09 = (
        ('---','---'),
        ('正常','正常'),
        ('無壓力','無壓力'),
        ('線路不通','線路不通'),
        ('壓射缸漏油','壓射缸漏油'),
        ('射杆彎曲','射杆彎曲'),
    )
    CHOICE10 = (
        ('---','---'),
        ('正常','正常'),
        ('斷線','斷線'),
        ('短路','短路'),
        ('鏈條斷','鏈條斷'),
        ('編碼器異常','編碼器異常'),
        ('銅套磨損','銅套磨損'),
    )
    CHOICE11 = (
        ('---','---'),
        ('正常','正常'),
        ('磨損','磨損'),
        ('斷裂','斷裂'),
        ('接頭滑絲','接頭滑絲'),
    )
    CHOICE12 = (
        ('---','---'),
        ('正常','正常'),
        ('破損','破損'),
        ('堵塞','堵塞'),
    )
    CHOICE13 = (
        ('---','---'),
        ('正常','正常'),
        ('油品變質','油品變質'),
    )
    CHOICE14 = (
        ('---','---'),
        ('正常','正常'),
        ('磨損','磨損'),
        ('軸心斷裂','軸心斷裂'),
    )
    CHOICE15 = (
        ('---','---'),
        ('正常','正常'),
        ('線路不通','線路不通'),
        ('閥心斷裂','閥心斷裂'),
    )
    CHOICE16 = (
        ('---','---'),
        ('正常','正常'),
        ('管道不通','管道不通'),
        ('管道斷裂','管道斷裂'),
        ('泵心磨損','泵心磨損'),
    )
    CHOICE17 = (
        ('---','---'),
        ('正常','正常'),
        ('鋼瓶裂縫','鋼瓶裂縫'),
        ('壓力過高','壓力過高'),
        ('壓力過低','壓力過低'),
    )
    CHOICE18 = (
        ('---','---'),
        ('正常','正常'),
        ('線路不通','線路不通'),
        ('短路','短路'),
    )
    CHOICE19 = (
        ('---','---'),
        ('正常','正常'),
        ('霧化器損壞','霧化器損壞'),
        ('線路不通','線路不通'),
        ('緩衝彈簧斷裂','緩衝彈簧斷裂'),
    )
    CHOICE20 = (
        ('---','---'),
        ('正常','正常'),
        ('開關損壞','開關損壞'),
        ('軸承磨損','軸承磨損'),
        ('緩衝器斷裂','緩衝器斷裂'),
        ('線路不通','線路不通'),
        ('編碼器異常','編碼器異常'),
    )
    CHOICE21 = (
        ('---','---'),
        ('正常','正常'),
        ('尺寸NG','尺寸NG'),
        ('模崩','模崩'),
        ('模芯斷','模芯斷'),
        ('重覆修模','重覆修模'),
        ('待修模','待修模'),
    )



# generated by make-code-item003.py
    headera = models.CharField(default=".",max_length=99,verbose_name="幾號機")
    headerb = models.CharField(default=".",max_length=99,verbose_name="噸位")
    headerc = models.CharField(default=".",max_length=99,verbose_name="人員")
    headerd = models.DateField(verbose_name="日期")
    data01a = models.CharField(default=".",max_length=99,verbose_name="格林柱-零件")
    data01b = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度一")
    data01c = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度二")
    data01d = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度三")
    data01e = models.CharField(default=".",max_length=99,verbose_name="格林柱-備註說明", choices=CHOICE01)
    data02a = models.CharField(default=".",max_length=99,verbose_name="機架底座-零件")
    data02b = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度一")
    data02c = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度二")
    data02d = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度三")
    data02e = models.CharField(default=".",max_length=99,verbose_name="機架底座-備註說明", choices=CHOICE02)
    data03a = models.CharField(default=".",max_length=99,verbose_name="模板(定)-零件")
    data03b = models.CharField(default=".",max_length=99,verbose_name="模板(定)-進度一")
    data03c = models.CharField(default=".",max_length=99,verbose_name="模板(定)-進度二")
    data03d = models.CharField(default=".",max_length=99,verbose_name="模板(定)-進度三")
    data03e = models.CharField(default=".",max_length=99,verbose_name="模板(定)-備註說明", choices=CHOICE03)
    data04a = models.CharField(default=".",max_length=99,verbose_name="模板(動)-零件")
    data04b = models.CharField(default=".",max_length=99,verbose_name="模板(動)-進度一")
    data04c = models.CharField(default=".",max_length=99,verbose_name="模板(動)-進度二")
    data04d = models.CharField(default=".",max_length=99,verbose_name="模板(動)-進度三")
    data04e = models.CharField(default=".",max_length=99,verbose_name="模板(動)-備註說明", choices=CHOICE04)
    data05a = models.CharField(default=".",max_length=99,verbose_name="合模-零件")
    data05b = models.CharField(default=".",max_length=99,verbose_name="合模-進度一")
    data05c = models.CharField(default=".",max_length=99,verbose_name="合模-進度二")
    data05d = models.CharField(default=".",max_length=99,verbose_name="合模-進度三")
    data05e = models.CharField(default=".",max_length=99,verbose_name="合模-備註說明", choices=CHOICE05)
    data06a = models.CharField(default=".",max_length=99,verbose_name="曲軸-零件")
    data06b = models.CharField(default=".",max_length=99,verbose_name="曲軸-進度一")
    data06c = models.CharField(default=".",max_length=99,verbose_name="曲軸-進度二")
    data06d = models.CharField(default=".",max_length=99,verbose_name="曲軸-進度三")
    data06e = models.CharField(default=".",max_length=99,verbose_name="曲軸-備註說明", choices=CHOICE06)
    data07a = models.CharField(default=".",max_length=99,verbose_name="鋼帶-零件")
    data07b = models.CharField(default=".",max_length=99,verbose_name="鋼帶-進度一")
    data07c = models.CharField(default=".",max_length=99,verbose_name="鋼帶-進度二")
    data07d = models.CharField(default=".",max_length=99,verbose_name="鋼帶-進度三")
    data07e = models.CharField(default=".",max_length=99,verbose_name="鋼帶-備註說明", choices=CHOICE07)
    data08a = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-零件")
    data08b = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度一")
    data08c = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度二")
    data08d = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度三")
    data08e = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-備註說明", choices=CHOICE08)
    data09a = models.CharField(default=".",max_length=99,verbose_name="壓射系統-零件")
    data09b = models.CharField(default=".",max_length=99,verbose_name="壓射系統-進度一")
    data09c = models.CharField(default=".",max_length=99,verbose_name="壓射系統-進度二")
    data09d = models.CharField(default=".",max_length=99,verbose_name="壓射系統-進度三")
    data09e = models.CharField(default=".",max_length=99,verbose_name="壓射系統-備註說明", choices=CHOICE09)
    data10a = models.CharField(default=".",max_length=99,verbose_name="澆注系統-零件")
    data10b = models.CharField(default=".",max_length=99,verbose_name="澆注系統-進度一")
    data10c = models.CharField(default=".",max_length=99,verbose_name="澆注系統-進度二")
    data10d = models.CharField(default=".",max_length=99,verbose_name="澆注系統-進度三")
    data10e = models.CharField(default=".",max_length=99,verbose_name="澆注系統-備註說明", choices=CHOICE10)
    data11a = models.CharField(default=".",max_length=99,verbose_name="油管-零件")
    data11b = models.CharField(default=".",max_length=99,verbose_name="油管-進度一")
    data11c = models.CharField(default=".",max_length=99,verbose_name="油管-進度二")
    data11d = models.CharField(default=".",max_length=99,verbose_name="油管-進度三")
    data11e = models.CharField(default=".",max_length=99,verbose_name="油管-備註說明", choices=CHOICE11)
    data12a = models.CharField(default=".",max_length=99,verbose_name="過濾網-零件")
    data12b = models.CharField(default=".",max_length=99,verbose_name="過濾網-進度一")
    data12c = models.CharField(default=".",max_length=99,verbose_name="過濾網-進度二")
    data12d = models.CharField(default=".",max_length=99,verbose_name="過濾網-進度三")
    data12e = models.CharField(default=".",max_length=99,verbose_name="過濾網-備註說明", choices=CHOICE12)
    data13a = models.CharField(default=".",max_length=99,verbose_name="油箱-零件")
    data13b = models.CharField(default=".",max_length=99,verbose_name="油箱-進度一")
    data13c = models.CharField(default=".",max_length=99,verbose_name="油箱-進度二")
    data13d = models.CharField(default=".",max_length=99,verbose_name="油箱-進度三")
    data13e = models.CharField(default=".",max_length=99,verbose_name="油箱-備註說明", choices=CHOICE13)
    data14a = models.CharField(default=".",max_length=99,verbose_name="馬達-零件")
    data14b = models.CharField(default=".",max_length=99,verbose_name="馬達-進度一")
    data14c = models.CharField(default=".",max_length=99,verbose_name="馬達-進度二")
    data14d = models.CharField(default=".",max_length=99,verbose_name="馬達-進度三")
    data14e = models.CharField(default=".",max_length=99,verbose_name="馬達-備註說明", choices=CHOICE14)
    data15a = models.CharField(default=".",max_length=99,verbose_name="電磁閥-零件")
    data15b = models.CharField(default=".",max_length=99,verbose_name="電磁閥-進度一")
    data15c = models.CharField(default=".",max_length=99,verbose_name="電磁閥-進度二")
    data15d = models.CharField(default=".",max_length=99,verbose_name="電磁閥-進度三")
    data15e = models.CharField(default=".",max_length=99,verbose_name="電磁閥-備註說明", choices=CHOICE15)
    data16a = models.CharField(default=".",max_length=99,verbose_name="潤滑系統-零件")
    data16b = models.CharField(default=".",max_length=99,verbose_name="潤滑系統-進度一")
    data16c = models.CharField(default=".",max_length=99,verbose_name="潤滑系統-進度二")
    data16d = models.CharField(default=".",max_length=99,verbose_name="潤滑系統-進度三")
    data16e = models.CharField(default=".",max_length=99,verbose_name="潤滑系統-備註說明", choices=CHOICE16)
    data17a = models.CharField(default=".",max_length=99,verbose_name="氮氣-零件")
    data17b = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度一")
    data17c = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度二")
    data17d = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度三")
    data17e = models.CharField(default=".",max_length=99,verbose_name="氮氣-備註說明", choices=CHOICE17)
    data18a = models.CharField(default=".",max_length=99,verbose_name="電路控制-零件")
    data18b = models.CharField(default=".",max_length=99,verbose_name="電路控制-進度一")
    data18c = models.CharField(default=".",max_length=99,verbose_name="電路控制-進度二")
    data18d = models.CharField(default=".",max_length=99,verbose_name="電路控制-進度三")
    data18e = models.CharField(default=".",max_length=99,verbose_name="電路控制-備註說明", choices=CHOICE18)
    data19a = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-零件")
    data19b = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度一")
    data19c = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度二")
    data19d = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度三")
    data19e = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-備註說明", choices=CHOICE19)
    data20a = models.CharField(default=".",max_length=99,verbose_name="自動取出-零件")
    data20b = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度一")
    data20c = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度二")
    data20d = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度三")
    data20e = models.CharField(default=".",max_length=99,verbose_name="自動取出-備註說明", choices=CHOICE20)
    data21a = models.CharField(default=".",max_length=99,verbose_name="模具-零件")
    data21b = models.CharField(default=".",max_length=99,verbose_name="模具-進度一")
    data21c = models.CharField(default=".",max_length=99,verbose_name="模具-進度二")
    data21d = models.CharField(default=".",max_length=99,verbose_name="模具-進度三")
    data21e = models.CharField(default=".",max_length=99,verbose_name="模具-備註說明", choices=CHOICE21)
    def __str__(self):
        return self.headera



class Item008(models.Model):
    CHOICE00 = (
        ('---','---'),
        ('正常','正常'),
        ('不正常','不正常'),
    )

# updated 2016-08-29: 新增一資料欄位 "机台状态" 下拉單選 [正常生产，设备故障，无订单，
# 无人操作，外发大修，无模具]
# 。(requested by 陶素鳳, coded by ...施工中)
    CHOICE_STATUS = (
        ('正常生产','正常生产'),
        ('设备故障','设备故障'),
        ('无订单','无订单'),
        ('无人操作','无人操作'),
        ('外发大修','外发大修'),
        ('无模具','无模具'),
    )
    # data02e = models.CharField(default=".",max_length=99,verbose_name="機架底座-備註說明", choices=CHOICE02)

# generated by make-code-item003.py
    headera = models.CharField(default=".",max_length=99,verbose_name="幾號機")
    headerb = models.CharField(default=".",max_length=99,verbose_name="噸位")
    headerc = models.CharField(default=".",max_length=99,verbose_name="人員")
    headerd = models.DateField(verbose_name="到廠日期")
    headere = models.DateTimeField(auto_now=True,  verbose_name="資料維護日期時間")
    headerf = models.CharField(default=".",max_length=99,verbose_name="机台状态", choices=CHOICE_STATUS)
    ########################################
  ### source code for models
  ### source code for models
    ### source code for models
    row01c01 = models.BooleanField(default=False, verbose_name="外部主件 格林柱 零件 => 格林柱")
    row01d00 = models.CharField(default=".",max_length=99,verbose_name="外部主件 格林柱 進度一")
    row01e00 = models.CharField(default=".",max_length=99,verbose_name="外部主件 格林柱 進度二")
    row01f00 = models.CharField(default=".",max_length=99,verbose_name="外部主件 格林柱 進度三")
    row01g00 = models.BooleanField(default=True,verbose_name="外部主件 格林柱 備註說明  正常")
    row01g01 = models.BooleanField(default=False, verbose_name="外部主件 格林柱 備註說明 => 磨損")
    row01g02 = models.BooleanField(default=False, verbose_name="外部主件 格林柱 備註說明 => 無法修復")
    row02c01 = models.BooleanField(default=False, verbose_name=" 機架底座 零件 => 機架底座")
    row02d00 = models.CharField(default=".",max_length=99,verbose_name=" 機架底座 進度一")
    row02e00 = models.CharField(default=".",max_length=99,verbose_name=" 機架底座 進度二")
    row02f00 = models.CharField(default=".",max_length=99,verbose_name=" 機架底座 進度三")
    row02g00 = models.BooleanField(default=True,verbose_name=" 機架底座 備註說明  正常")
    row02g01 = models.BooleanField(default=False, verbose_name=" 機架底座 備註說明 => 磨損")
    row02g02 = models.BooleanField(default=False, verbose_name=" 機架底座 備註說明 => 裂縫")
    row02g03 = models.BooleanField(default=False, verbose_name=" 機架底座 備註說明 => 漏油")
    row03c01 = models.BooleanField(default=False, verbose_name=" 模板(定) 零件 => 模板(定)")
    row03d00 = models.CharField(default=".",max_length=99,verbose_name=" 模板(定) 進度一")
    row03e00 = models.CharField(default=".",max_length=99,verbose_name=" 模板(定) 進度二")
    row03f00 = models.CharField(default=".",max_length=99,verbose_name=" 模板(定) 進度三")
    row03g00 = models.BooleanField(default=True,verbose_name=" 模板(定) 備註說明  正常")
    row03g01 = models.BooleanField(default=False, verbose_name=" 模板(定) 備註說明 => 平面變型")
    row03g02 = models.BooleanField(default=False, verbose_name=" 模板(定) 備註說明 => 無法修復")
    row04c01 = models.BooleanField(default=False, verbose_name=" 模板(動) 零件 => 模板(動)")
    row04d00 = models.CharField(default=".",max_length=99,verbose_name=" 模板(動) 進度一")
    row04e00 = models.CharField(default=".",max_length=99,verbose_name=" 模板(動) 進度二")
    row04f00 = models.CharField(default=".",max_length=99,verbose_name=" 模板(動) 進度三")
    row04g00 = models.BooleanField(default=True,verbose_name=" 模板(動) 備註說明  正常")
    row04g01 = models.BooleanField(default=False, verbose_name=" 模板(動) 備註說明 => 平面變型")
    row04g02 = models.BooleanField(default=False, verbose_name=" 模板(動) 備註說明 => 無法修復")
    row05c01 = models.BooleanField(default=False, verbose_name=" 合模 零件 => 油路板")
    row05c02 = models.BooleanField(default=False, verbose_name=" 合模 零件 => 合模油缸")
    row05d00 = models.CharField(default=".",max_length=99,verbose_name=" 合模 進度一")
    row05e00 = models.CharField(default=".",max_length=99,verbose_name=" 合模 進度二")
    row05f00 = models.CharField(default=".",max_length=99,verbose_name=" 合模 進度三")
    row05g00 = models.BooleanField(default=True,verbose_name=" 合模 備註說明  正常")
    row05g01 = models.BooleanField(default=False, verbose_name=" 合模 備註說明 => 合模缸漏油")
    row05g02 = models.BooleanField(default=False, verbose_name=" 合模 備註說明 => 合模缸螺旋斷裂")
    row05g03 = models.BooleanField(default=False, verbose_name=" 合模 備註說明 => 合模活塞磨損")
    row05g04 = models.BooleanField(default=False, verbose_name=" 合模 備註說明 => 無法修復")
    row06c01 = models.BooleanField(default=False, verbose_name=" 曲軸 零件 => 曲轴销")
    row06c02 = models.BooleanField(default=False, verbose_name=" 曲軸 零件 => 衬套")
    row06d00 = models.CharField(default=".",max_length=99,verbose_name=" 曲軸 進度一")
    row06e00 = models.CharField(default=".",max_length=99,verbose_name=" 曲軸 進度二")
    row06f00 = models.CharField(default=".",max_length=99,verbose_name=" 曲軸 進度三")
    row06g00 = models.BooleanField(default=True,verbose_name=" 曲軸 備註說明  正常")
    row06g01 = models.BooleanField(default=False, verbose_name=" 曲軸 備註說明 => 磨損")
    row06g02 = models.BooleanField(default=False, verbose_name=" 曲軸 備註說明 => 無法修復")
    row07c01 = models.BooleanField(default=False, verbose_name=" 鋼帶 零件 => 鋼帶")
    row07d00 = models.CharField(default=".",max_length=99,verbose_name=" 鋼帶 進度一")
    row07e00 = models.CharField(default=".",max_length=99,verbose_name=" 鋼帶 進度二")
    row07f00 = models.CharField(default=".",max_length=99,verbose_name=" 鋼帶 進度三")
    row07g00 = models.BooleanField(default=True,verbose_name=" 鋼帶 備註說明  正常")
    row07g01 = models.BooleanField(default=False, verbose_name=" 鋼帶 備註說明 => 磨損")
    row07g02 = models.BooleanField(default=False, verbose_name=" 鋼帶 備註說明 => 斷裂")
    row07g03 = models.BooleanField(default=False, verbose_name=" 鋼帶 備註說明 => 無法修復")
    row08c01 = models.BooleanField(default=False, verbose_name=" 保温炉 零件 => 炉盖")
    row08c02 = models.BooleanField(default=False, verbose_name=" 保温炉 零件 => 加热管")
    row08c03 = models.BooleanField(default=False, verbose_name=" 保温炉 零件 => 电线")
    row08c04 = models.BooleanField(default=False, verbose_name=" 保温炉 零件 => 感温棒")
    row08d00 = models.CharField(default=".",max_length=99,verbose_name=" 保温炉 進度一")
    row08e00 = models.CharField(default=".",max_length=99,verbose_name=" 保温炉 進度二")
    row08f00 = models.CharField(default=".",max_length=99,verbose_name=" 保温炉 進度三")
    row08g00 = models.BooleanField(default=True,verbose_name=" 保温炉 備註說明  正常")
    row08g01 = models.BooleanField(default=False, verbose_name=" 保温炉 備註說明 => 磨損")
    row08g02 = models.BooleanField(default=False, verbose_name=" 保温炉 備註說明 => 斷裂")
    row08g03 = models.BooleanField(default=False, verbose_name=" 保温炉 備註說明 => 無法修復")
    row08g04 = models.BooleanField(default=False, verbose_name=" 保温炉 備註說明 => 炉盖损坏")
    row08g05 = models.BooleanField(default=False, verbose_name=" 保温炉 備註說明 => 加热管断")
    row08g06 = models.BooleanField(default=False, verbose_name=" 保温炉 備註說明 => 电路断")
    row08g07 = models.BooleanField(default=False, verbose_name=" 保温炉 備註說明 => 温度不准")
    row09c01 = models.BooleanField(default=False, verbose_name="控制系统 膜厚調節 零件 => 开关")
    row09d00 = models.CharField(default=".",max_length=99,verbose_name="控制系统 膜厚調節 進度一")
    row09e00 = models.CharField(default=".",max_length=99,verbose_name="控制系统 膜厚調節 進度二")
    row09f00 = models.CharField(default=".",max_length=99,verbose_name="控制系统 膜厚調節 進度三")
    row09g00 = models.BooleanField(default=True,verbose_name="控制系统 膜厚調節 備註說明  正常")
    row09g01 = models.BooleanField(default=False, verbose_name="控制系统 膜厚調節 備註說明 => 開關損壞")
    row09g02 = models.BooleanField(default=False, verbose_name="控制系统 膜厚調節 備註說明 => 線路不通")
    row09g03 = models.BooleanField(default=False, verbose_name="控制系统 膜厚調節 備註說明 => 短路")
    row09g04 = models.BooleanField(default=False, verbose_name="控制系统 膜厚調節 備註說明 => 無法修復")
    row10c01 = models.BooleanField(default=False, verbose_name=" 主电箱 零件 => 电路板")
    row10c02 = models.BooleanField(default=False, verbose_name=" 主电箱 零件 => 保险丝")
    row10c03 = models.BooleanField(default=False, verbose_name=" 主电箱 零件 => 保温炉控制器")
    row10d00 = models.CharField(default=".",max_length=99,verbose_name=" 主电箱 進度一")
    row10e00 = models.CharField(default=".",max_length=99,verbose_name=" 主电箱 進度二")
    row10f00 = models.CharField(default=".",max_length=99,verbose_name=" 主电箱 進度三")
    row10g00 = models.BooleanField(default=True,verbose_name=" 主电箱 備註說明  正常")
    row10g01 = models.BooleanField(default=False, verbose_name=" 主电箱 備註說明 => 保险丝烧坏")
    row10g02 = models.BooleanField(default=False, verbose_name=" 主电箱 備註說明 => 線路不通")
    row10g03 = models.BooleanField(default=False, verbose_name=" 主电箱 備註說明 => 無法修復")
    row11c01 = models.BooleanField(default=False, verbose_name=" 操作面板 零件 => 控制面板")
    row11d00 = models.CharField(default=".",max_length=99,verbose_name=" 操作面板 進度一")
    row11e00 = models.CharField(default=".",max_length=99,verbose_name=" 操作面板 進度二")
    row11f00 = models.CharField(default=".",max_length=99,verbose_name=" 操作面板 進度三")
    row11g00 = models.BooleanField(default=True,verbose_name=" 操作面板 備註說明  正常")
    row11g01 = models.BooleanField(default=False, verbose_name=" 操作面板 備註說明 => 按键损坏")
    row11g02 = models.BooleanField(default=False, verbose_name=" 操作面板 備註說明 => 系统坏")
    row11g03 = models.BooleanField(default=False, verbose_name=" 操作面板 備註說明 => 無法修復")
    row12c01 = models.BooleanField(default=False, verbose_name="压射系统  零件 => 行程开关")
    row12c02 = models.BooleanField(default=False, verbose_name="压射系统  零件 => 射杆连接板")
    row12c03 = models.BooleanField(default=False, verbose_name="压射系统  零件 => 料管")
    row12c04 = models.BooleanField(default=False, verbose_name="压射系统  零件 => 射杆接头")
    row12d00 = models.CharField(default=".",max_length=99,verbose_name="压射系统  進度一")
    row12e00 = models.CharField(default=".",max_length=99,verbose_name="压射系统  進度二")
    row12f00 = models.CharField(default=".",max_length=99,verbose_name="压射系统  進度三")
    row12g00 = models.BooleanField(default=True,verbose_name="压射系统  備註說明  正常")
    row12g01 = models.BooleanField(default=False, verbose_name="压射系统  備註說明 => 無壓力")
    row12g02 = models.BooleanField(default=False, verbose_name="压射系统  備註說明 => 線路不通")
    row12g03 = models.BooleanField(default=False, verbose_name="压射系统  備註說明 => 壓射缸漏油")
    row12g04 = models.BooleanField(default=False, verbose_name="压射系统  備註說明 => 射杆彎曲")
    row12g05 = models.BooleanField(default=False, verbose_name="压射系统  備註說明 => 连接板断裂")
    row12g06 = models.BooleanField(default=False, verbose_name="压射系统  備註說明 => 开关无信号")
    row12g07 = models.BooleanField(default=False, verbose_name="压射系统  備註說明 => 料管磨损")
    row12g08 = models.BooleanField(default=False, verbose_name="压射系统  備註說明 => 接头断")
    row13c01 = models.BooleanField(default=False, verbose_name="澆注系統  零件 => 链条齿轮")
    row13c02 = models.BooleanField(default=False, verbose_name="澆注系統  零件 => 链条")
    row13c03 = models.BooleanField(default=False, verbose_name="澆注系統  零件 => 铜套")
    row13c04 = models.BooleanField(default=False, verbose_name="澆注系統  零件 => 编码器")
    row13c05 = models.BooleanField(default=False, verbose_name="澆注系統  零件 => 接触开关")
    row13d00 = models.CharField(default=".",max_length=99,verbose_name="澆注系統  進度一")
    row13e00 = models.CharField(default=".",max_length=99,verbose_name="澆注系統  進度二")
    row13f00 = models.CharField(default=".",max_length=99,verbose_name="澆注系統  進度三")
    row13g00 = models.BooleanField(default=True,verbose_name="澆注系統  備註說明  正常")
    row13g01 = models.BooleanField(default=False, verbose_name="澆注系統  備註說明 => 链条断")
    row13g02 = models.BooleanField(default=False, verbose_name="澆注系統  備註說明 => 齿轮滑牙斷")
    row13g03 = models.BooleanField(default=False, verbose_name="澆注系統  備註說明 => 編碼器異常")
    row13g04 = models.BooleanField(default=False, verbose_name="澆注系統  備註說明 => 銅套磨損")
    row14c01 = models.BooleanField(default=False, verbose_name="油壓系統  零件 => 油管")
    row14c02 = models.BooleanField(default=False, verbose_name="油壓系統  零件 => 過濾網")
    row14c03 = models.BooleanField(default=False, verbose_name="油壓系統  零件 => 油箱")
    row14c04 = models.BooleanField(default=False, verbose_name="油壓系統  零件 => 馬達")
    row14c05 = models.BooleanField(default=False, verbose_name="油壓系統  零件 => 電磁閥")
    row14d00 = models.CharField(default=".",max_length=99,verbose_name="油壓系統  進度一")
    row14e00 = models.CharField(default=".",max_length=99,verbose_name="油壓系統  進度二")
    row14f00 = models.CharField(default=".",max_length=99,verbose_name="油壓系統  進度三")
    row14g00 = models.BooleanField(default=True,verbose_name="油壓系統  備註說明  正常")
    row14g01 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 破損")
    row14g02 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 斷裂")
    row14g03 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 接頭滑絲")
    row14g04 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 堵塞")
    row14g05 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 油品變質")
    row14g06 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 磨損")
    row14g07 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 軸心斷裂")
    row14g08 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 線路不通")
    row14g09 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 閥心斷裂")
    row15c01 = models.BooleanField(default=False, verbose_name="潤滑系統  零件 => 油嘴")
    row15c02 = models.BooleanField(default=False, verbose_name="潤滑系統  零件 => 分油器")
    row15c03 = models.BooleanField(default=False, verbose_name="潤滑系統  零件 => 油管")
    row15c04 = models.BooleanField(default=False, verbose_name="潤滑系統  零件 => 油泵")
    row15d00 = models.CharField(default=".",max_length=99,verbose_name="潤滑系統  進度一")
    row15e00 = models.CharField(default=".",max_length=99,verbose_name="潤滑系統  進度二")
    row15f00 = models.CharField(default=".",max_length=99,verbose_name="潤滑系統  進度三")
    row15g00 = models.BooleanField(default=True,verbose_name="潤滑系統  備註說明  正常")
    row15g01 = models.BooleanField(default=False, verbose_name="潤滑系統  備註說明 => 管道不通")
    row15g02 = models.BooleanField(default=False, verbose_name="潤滑系統  備註說明 => 管道斷裂")
    row15g03 = models.BooleanField(default=False, verbose_name="潤滑系統  備註說明 => 泵心磨損")
    row16c01 = models.BooleanField(default=False, verbose_name="氮氣  零件 => 氮气钢瓶")
    row16c02 = models.BooleanField(default=False, verbose_name="氮氣  零件 => 氮气瓶油封")
    row16c03 = models.BooleanField(default=False, verbose_name="氮氣  零件 => 轴承带")
    row16d00 = models.CharField(default=".",max_length=99,verbose_name="氮氣  進度一")
    row16e00 = models.CharField(default=".",max_length=99,verbose_name="氮氣  進度二")
    row16f00 = models.CharField(default=".",max_length=99,verbose_name="氮氣  進度三")
    row16g00 = models.BooleanField(default=True,verbose_name="氮氣  備註說明  正常")
    row16g01 = models.BooleanField(default=False, verbose_name="氮氣  備註說明 => 鋼瓶裂縫")
    row16g02 = models.BooleanField(default=False, verbose_name="氮氣  備註說明 => 壓力過高")
    row16g03 = models.BooleanField(default=False, verbose_name="氮氣  備註說明 => 壓力過低")
    row16g04 = models.BooleanField(default=False, verbose_name="氮氣  備註說明 => 磨损")
    row17c01 = models.BooleanField(default=False, verbose_name="锁模系统  零件 => 电子尺")
    row17d00 = models.CharField(default=".",max_length=99,verbose_name="锁模系统  進度一")
    row17e00 = models.CharField(default=".",max_length=99,verbose_name="锁模系统  進度二")
    row17f00 = models.CharField(default=".",max_length=99,verbose_name="锁模系统  進度三")
    row17g00 = models.BooleanField(default=True,verbose_name="锁模系统  備註說明  正常")
    row17g01 = models.BooleanField(default=False, verbose_name="锁模系统  備註說明 => 读数不准")
    row18c01 = models.BooleanField(default=False, verbose_name="自動噴霧  零件 => 雾化器")
    row18c02 = models.BooleanField(default=False, verbose_name="自動噴霧  零件 => 喷雾机板")
    row18c03 = models.BooleanField(default=False, verbose_name="自動噴霧  零件 => 铜管")
    row18c04 = models.BooleanField(default=False, verbose_name="自動噴霧  零件 => 电磁阀")
    row18c05 = models.BooleanField(default=False, verbose_name="自動噴霧  零件 => 缓冲器")
    row18d00 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧  進度一")
    row18e00 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧  進度二")
    row18f00 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧  進度三")
    row18g00 = models.BooleanField(default=True,verbose_name="自動噴霧  備註說明  正常")
    row18g01 = models.BooleanField(default=False, verbose_name="自動噴霧  備註說明 => 霧化器損壞")
    row18g02 = models.BooleanField(default=False, verbose_name="自動噴霧  備註說明 => 線路不通")
    row18g03 = models.BooleanField(default=False, verbose_name="自動噴霧  備註說明 => 緩衝彈簧斷裂")
    row18g04 = models.BooleanField(default=False, verbose_name="自動噴霧  備註說明 => 喷头螺丝滑牙")
    row18g05 = models.BooleanField(default=False, verbose_name="自動噴霧  備註說明 => 断裂")
    row18g06 = models.BooleanField(default=False, verbose_name="自動噴霧  備註說明 => 漏水")
    row19c01 = models.BooleanField(default=False, verbose_name="自動取出  零件 => 取件机手臂")
    row19c02 = models.BooleanField(default=False, verbose_name="自動取出  零件 => 缓冲器")
    row19c03 = models.BooleanField(default=False, verbose_name="自動取出  零件 => 夹手")
    row19c04 = models.BooleanField(default=False, verbose_name="自動取出  零件 => 轴承")
    row19c05 = models.BooleanField(default=False, verbose_name="自動取出  零件 => 马达")
    row19d00 = models.CharField(default=".",max_length=99,verbose_name="自動取出  進度一")
    row19e00 = models.CharField(default=".",max_length=99,verbose_name="自動取出  進度二")
    row19f00 = models.CharField(default=".",max_length=99,verbose_name="自動取出  進度三")
    row19g00 = models.BooleanField(default=True,verbose_name="自動取出  備註說明  正常")
    row19g01 = models.BooleanField(default=False, verbose_name="自動取出  備註說明 => 手臂断裂")
    row19g02 = models.BooleanField(default=False, verbose_name="自動取出  備註說明 => 夹手磨损")
    row19g03 = models.BooleanField(default=False, verbose_name="自動取出  備註說明 => 缓冲器坏")
    row19g04 = models.BooleanField(default=False, verbose_name="自動取出  備註說明 => 手臂轴承坏")
    row19g05 = models.BooleanField(default=False, verbose_name="自動取出  備註說明 => 内部烧坏")
    row20c01 = models.BooleanField(default=False, verbose_name="模具  零件 => 模芯")
    row20c02 = models.BooleanField(default=False, verbose_name="模具  零件 => 顶针")
    row20c03 = models.BooleanField(default=False, verbose_name="模具  零件 => 滑块")
    row20c04 = models.BooleanField(default=False, verbose_name="模具  零件 => 定模仁")
    row20c05 = models.BooleanField(default=False, verbose_name="模具  零件 => 动模仁")
    row20c06 = models.BooleanField(default=False, verbose_name="模具  零件 => 油缸")
    row20d00 = models.CharField(default=".",max_length=99,verbose_name="模具  進度一")
    row20e00 = models.CharField(default=".",max_length=99,verbose_name="模具  進度二")
    row20f00 = models.CharField(default=".",max_length=99,verbose_name="模具  進度三")
    row20g00 = models.BooleanField(default=True,verbose_name="模具  備註說明  正常")
    row20g01 = models.BooleanField(default=False, verbose_name="模具  備註說明 => 尺寸NG")
    row20g02 = models.BooleanField(default=False, verbose_name="模具  備註說明 => 模崩")
    row20g03 = models.BooleanField(default=False, verbose_name="模具  備註說明 => 模芯斷")
    row20g04 = models.BooleanField(default=False, verbose_name="模具  備註說明 => 顶针斷")
    row20g05 = models.BooleanField(default=False, verbose_name="模具  備註說明 => 重覆修模")
    row20g06 = models.BooleanField(default=False, verbose_name="模具  備註說明 => 待修模")

    def __str__(self):
        return self.headera

class Item009(models.Model):
    CHOICE00 = (
        ('---','---'),
        ('正常','正常'),
        ('不正常','不正常'),
    )

# updated 2016-08-29: 新增一資料欄位 "机台状态" 下拉單選 [正常生产，设备故障，无订单，
# 无人操作，外发大修，无模具]
# 。(requested by 陶素鳳, coded by ...施工中)
    CHOICE_STATUS = (
        ('正常生产','正常生产'),
        ('设备故障','设备故障'),
        ('无订单','无订单'),
        ('无人操作','无人操作'),
        ('外发大修','外发大修'),
        ('无模具','无模具'),
    )
    # data02e = models.CharField(default=".",max_length=99,verbose_name="機架底座-備註說明", choices=CHOICE02)

# generated by make-code-item003.py
    headera = models.CharField(default=".",max_length=99,verbose_name="幾號機")
    headerb = models.CharField(default=".",max_length=99,verbose_name="噸位")
    headerc = models.CharField(default=".",max_length=99,verbose_name="人員")
    headerd = models.DateField(verbose_name="到廠日期")
    headere = models.DateTimeField(auto_now=True,  verbose_name="資料維護日期時間")
    headerf = models.CharField(default=".",max_length=99,verbose_name="机台状态", choices=CHOICE_STATUS)
    ########################################
  ### source code for models
  ### source code for models
    ### source code for models
    row01c01 = models.BooleanField(default=False, verbose_name="外部主件 格林柱 零件 => 格林柱")
    row01d00 = models.CharField(default=".",max_length=99,verbose_name="外部主件 格林柱 進度一")
    row01e00 = models.CharField(default=".",max_length=99,verbose_name="外部主件 格林柱 進度二")
    row01f00 = models.CharField(default=".",max_length=99,verbose_name="外部主件 格林柱 進度三")
    row01g00 = models.BooleanField(default=True,verbose_name="外部主件 格林柱 備註說明  正常")
    row01g01 = models.BooleanField(default=False, verbose_name="外部主件 格林柱 備註說明 => 磨損")
    row01g02 = models.BooleanField(default=False, verbose_name="外部主件 格林柱 備註說明 => 無法修復")
    row02c01 = models.BooleanField(default=False, verbose_name=" 機架底座 零件 => 機架底座")
    row02d00 = models.CharField(default=".",max_length=99,verbose_name=" 機架底座 進度一")
    row02e00 = models.CharField(default=".",max_length=99,verbose_name=" 機架底座 進度二")
    row02f00 = models.CharField(default=".",max_length=99,verbose_name=" 機架底座 進度三")
    row02g00 = models.BooleanField(default=True,verbose_name=" 機架底座 備註說明  正常")
    row02g01 = models.BooleanField(default=False, verbose_name=" 機架底座 備註說明 => 磨損")
    row02g02 = models.BooleanField(default=False, verbose_name=" 機架底座 備註說明 => 裂縫")
    row02g03 = models.BooleanField(default=False, verbose_name=" 機架底座 備註說明 => 漏油")
    row03c01 = models.BooleanField(default=False, verbose_name=" 模板(定) 零件 => 模板(定)")
    row03d00 = models.CharField(default=".",max_length=99,verbose_name=" 模板(定) 進度一")
    row03e00 = models.CharField(default=".",max_length=99,verbose_name=" 模板(定) 進度二")
    row03f00 = models.CharField(default=".",max_length=99,verbose_name=" 模板(定) 進度三")
    row03g00 = models.BooleanField(default=True,verbose_name=" 模板(定) 備註說明  正常")
    row03g01 = models.BooleanField(default=False, verbose_name=" 模板(定) 備註說明 => 平面變型")
    row03g02 = models.BooleanField(default=False, verbose_name=" 模板(定) 備註說明 => 無法修復")
    row04c01 = models.BooleanField(default=False, verbose_name=" 模板(動) 零件 => 模板(動)")
    row04d00 = models.CharField(default=".",max_length=99,verbose_name=" 模板(動) 進度一")
    row04e00 = models.CharField(default=".",max_length=99,verbose_name=" 模板(動) 進度二")
    row04f00 = models.CharField(default=".",max_length=99,verbose_name=" 模板(動) 進度三")
    row04g00 = models.BooleanField(default=True,verbose_name=" 模板(動) 備註說明  正常")
    row04g01 = models.BooleanField(default=False, verbose_name=" 模板(動) 備註說明 => 平面變型")
    row04g02 = models.BooleanField(default=False, verbose_name=" 模板(動) 備註說明 => 無法修復")
    row05c01 = models.BooleanField(default=False, verbose_name=" 合模 零件 => 油路板")
    row05c02 = models.BooleanField(default=False, verbose_name=" 合模 零件 => 合模油缸")
    row05d00 = models.CharField(default=".",max_length=99,verbose_name=" 合模 進度一")
    row05e00 = models.CharField(default=".",max_length=99,verbose_name=" 合模 進度二")
    row05f00 = models.CharField(default=".",max_length=99,verbose_name=" 合模 進度三")
    row05g00 = models.BooleanField(default=True,verbose_name=" 合模 備註說明  正常")
    row05g01 = models.BooleanField(default=False, verbose_name=" 合模 備註說明 => 合模缸漏油")
    row05g02 = models.BooleanField(default=False, verbose_name=" 合模 備註說明 => 合模缸螺旋斷裂")
    row05g03 = models.BooleanField(default=False, verbose_name=" 合模 備註說明 => 合模活塞磨損")
    row05g04 = models.BooleanField(default=False, verbose_name=" 合模 備註說明 => 無法修復")
    row06c01 = models.BooleanField(default=False, verbose_name=" 曲軸 零件 => 曲轴销")
    row06c02 = models.BooleanField(default=False, verbose_name=" 曲軸 零件 => 衬套")
    row06d00 = models.CharField(default=".",max_length=99,verbose_name=" 曲軸 進度一")
    row06e00 = models.CharField(default=".",max_length=99,verbose_name=" 曲軸 進度二")
    row06f00 = models.CharField(default=".",max_length=99,verbose_name=" 曲軸 進度三")
    row06g00 = models.BooleanField(default=True,verbose_name=" 曲軸 備註說明  正常")
    row06g01 = models.BooleanField(default=False, verbose_name=" 曲軸 備註說明 => 磨損")
    row06g02 = models.BooleanField(default=False, verbose_name=" 曲軸 備註說明 => 無法修復")
    row07c01 = models.BooleanField(default=False, verbose_name=" 鋼帶 零件 => 鋼帶")
    row07d00 = models.CharField(default=".",max_length=99,verbose_name=" 鋼帶 進度一")
    row07e00 = models.CharField(default=".",max_length=99,verbose_name=" 鋼帶 進度二")
    row07f00 = models.CharField(default=".",max_length=99,verbose_name=" 鋼帶 進度三")
    row07g00 = models.BooleanField(default=True,verbose_name=" 鋼帶 備註說明  正常")
    row07g01 = models.BooleanField(default=False, verbose_name=" 鋼帶 備註說明 => 磨損")
    row07g02 = models.BooleanField(default=False, verbose_name=" 鋼帶 備註說明 => 斷裂")
    row07g03 = models.BooleanField(default=False, verbose_name=" 鋼帶 備註說明 => 無法修復")
    row08c01 = models.BooleanField(default=False, verbose_name=" 保温炉 零件 => 炉盖")
    row08c02 = models.BooleanField(default=False, verbose_name=" 保温炉 零件 => 加热管")
    row08c03 = models.BooleanField(default=False, verbose_name=" 保温炉 零件 => 电线")
    row08c04 = models.BooleanField(default=False, verbose_name=" 保温炉 零件 => 感温棒")
    row08d00 = models.CharField(default=".",max_length=99,verbose_name=" 保温炉 進度一")
    row08e00 = models.CharField(default=".",max_length=99,verbose_name=" 保温炉 進度二")
    row08f00 = models.CharField(default=".",max_length=99,verbose_name=" 保温炉 進度三")
    row08g00 = models.BooleanField(default=True,verbose_name=" 保温炉 備註說明  正常")
    row08g01 = models.BooleanField(default=False, verbose_name=" 保温炉 備註說明 => 磨損")
    row08g02 = models.BooleanField(default=False, verbose_name=" 保温炉 備註說明 => 斷裂")
    row08g03 = models.BooleanField(default=False, verbose_name=" 保温炉 備註說明 => 無���修復")
    row08g04 = models.BooleanField(default=False, verbose_name=" 保温炉 備註說明 => 炉盖损坏")
    row08g05 = models.BooleanField(default=False, verbose_name=" 保温炉 備註說明 => 加热管断")
    row08g06 = models.BooleanField(default=False, verbose_name=" 保温炉 備註說明 => 电路断")
    row08g07 = models.BooleanField(default=False, verbose_name=" 保温炉 備註說明 => 温度不准")
    row09c01 = models.BooleanField(default=False, verbose_name="控制系统 膜厚調節 零件 => 开关")
    row09d00 = models.CharField(default=".",max_length=99,verbose_name="控制系统 膜厚調節 進度一")
    row09e00 = models.CharField(default=".",max_length=99,verbose_name="控制系统 膜厚調節 進度二")
    row09f00 = models.CharField(default=".",max_length=99,verbose_name="控制系统 膜厚調節 進度三")
    row09g00 = models.BooleanField(default=True,verbose_name="控制系统 膜厚調節 備註說明  正常")
    row09g01 = models.BooleanField(default=False, verbose_name="控制系统 膜厚調節 備註說明 => 開關損壞")
    row09g02 = models.BooleanField(default=False, verbose_name="控制系统 膜厚調節 備註說明 => 線路不通")
    row09g03 = models.BooleanField(default=False, verbose_name="控制系统 膜厚調節 備註說明 => 短路")
    row09g04 = models.BooleanField(default=False, verbose_name="控制系统 膜厚調節 備註說明 => 無法修復")
    row10c01 = models.BooleanField(default=False, verbose_name=" 主电箱 零件 => 电路板")
    row10c02 = models.BooleanField(default=False, verbose_name=" 主电箱 零件 => 保险丝")
    row10c03 = models.BooleanField(default=False, verbose_name=" 主电箱 零件 => 保温炉控制器")
    row10d00 = models.CharField(default=".",max_length=99,verbose_name=" 主电箱 進度一")
    row10e00 = models.CharField(default=".",max_length=99,verbose_name=" 主电箱 進度二")
    row10f00 = models.CharField(default=".",max_length=99,verbose_name=" 主电箱 進度三")
    row10g00 = models.BooleanField(default=True,verbose_name=" 主电箱 備註說明  正常")
    row10g01 = models.BooleanField(default=False, verbose_name=" 主电箱 備註說明 => 保险丝烧坏")
    row10g02 = models.BooleanField(default=False, verbose_name=" 主电箱 備註說明 => 線路不通")
    row10g03 = models.BooleanField(default=False, verbose_name=" 主电箱 備註說明 => 無法修復")
    row11c01 = models.BooleanField(default=False, verbose_name=" 操作面板 零件 => 控制面板")
    row11d00 = models.CharField(default=".",max_length=99,verbose_name=" 操作面板 進度一")
    row11e00 = models.CharField(default=".",max_length=99,verbose_name=" 操作面板 進度二")
    row11f00 = models.CharField(default=".",max_length=99,verbose_name=" 操作面板 進度三")
    row11g00 = models.BooleanField(default=True,verbose_name=" 操作面板 備註說明  正常")
    row11g01 = models.BooleanField(default=False, verbose_name=" 操作面板 備註說明 => 按键损坏")
    row11g02 = models.BooleanField(default=False, verbose_name=" 操作面板 備註說明 => 系统坏")
    row11g03 = models.BooleanField(default=False, verbose_name=" 操作面板 備註說明 => 無法修復")
    row12c01 = models.BooleanField(default=False, verbose_name="压射系统  零件 => 行程开关")
    row12c02 = models.BooleanField(default=False, verbose_name="压射系统  零件 => 射杆连接板")
    row12c03 = models.BooleanField(default=False, verbose_name="压射系统  零件 => 料管")
    row12c04 = models.BooleanField(default=False, verbose_name="压射系统  零件 => 射杆接头")
    row12d00 = models.CharField(default=".",max_length=99,verbose_name="压射系统  進度一")
    row12e00 = models.CharField(default=".",max_length=99,verbose_name="压射系统  進度二")
    row12f00 = models.CharField(default=".",max_length=99,verbose_name="压射系统  進度三")
    row12g00 = models.BooleanField(default=True,verbose_name="压射系统  備註說明  正常")
    row12g01 = models.BooleanField(default=False, verbose_name="压射系统  備註說明 => 無壓力")
    row12g02 = models.BooleanField(default=False, verbose_name="压射系统  備註說明 => 線路不通")
    row12g03 = models.BooleanField(default=False, verbose_name="压射系统  備註說明 => 壓射缸漏油")
    row12g04 = models.BooleanField(default=False, verbose_name="压射系统  備註說明 => 射杆彎曲")
    row12g05 = models.BooleanField(default=False, verbose_name="压射系统  備註說明 => 连接板断裂")
    row12g06 = models.BooleanField(default=False, verbose_name="压射系统  備註說明 => 开关无信号")
    row12g07 = models.BooleanField(default=False, verbose_name="压射系统  備註說明 => 料管磨损")
    row12g08 = models.BooleanField(default=False, verbose_name="压射系统  備註說明 => 接头断")
    row13c01 = models.BooleanField(default=False, verbose_name="澆注系統  零件 => 链条齿轮")
    row13c02 = models.BooleanField(default=False, verbose_name="澆注系統  零件 => 链条")
    row13c03 = models.BooleanField(default=False, verbose_name="澆注系統  零件 => 铜套")
    row13c04 = models.BooleanField(default=False, verbose_name="澆注系統  零件 => 编码器")
    row13c05 = models.BooleanField(default=False, verbose_name="澆注系統  零件 => 接触开关")
    row13d00 = models.CharField(default=".",max_length=99,verbose_name="澆注系統  進度一")
    row13e00 = models.CharField(default=".",max_length=99,verbose_name="澆注系統  進度二")
    row13f00 = models.CharField(default=".",max_length=99,verbose_name="澆注系統  進度三")
    row13g00 = models.BooleanField(default=True,verbose_name="澆注系統  備註說明  正常")
    row13g01 = models.BooleanField(default=False, verbose_name="澆注系統  備註說明 => 链条断")
    row13g02 = models.BooleanField(default=False, verbose_name="澆注系統  備註說明 => 齿轮滑牙斷")
    row13g03 = models.BooleanField(default=False, verbose_name="澆注系統  備註說明 => 編碼器異常")
    row13g04 = models.BooleanField(default=False, verbose_name="澆注系統  備註說明 => 銅套磨損")
    row14c01 = models.BooleanField(default=False, verbose_name="油壓系統  零件 => 油管")
    row14c02 = models.BooleanField(default=False, verbose_name="油壓系統  零件 => 過濾網")
    row14c03 = models.BooleanField(default=False, verbose_name="油壓系統  零件 => 油箱")
    row14c04 = models.BooleanField(default=False, verbose_name="油壓系統  零件 => 馬達")
    row14c05 = models.BooleanField(default=False, verbose_name="油壓系統  零件 => 電磁閥")
    row14d00 = models.CharField(default=".",max_length=99,verbose_name="油壓系統  進度一")
    row14e00 = models.CharField(default=".",max_length=99,verbose_name="油壓系統  進度二")
    row14f00 = models.CharField(default=".",max_length=99,verbose_name="油壓系統  進度三")
    row14g00 = models.BooleanField(default=True,verbose_name="油壓系統  備註說明  正常")
    row14g01 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 破損")
    row14g02 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 斷裂")
    row14g03 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 接頭滑絲")
    row14g04 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 堵塞")
    row14g05 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 油品變質")
    row14g06 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 磨損")
    row14g07 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 軸心斷裂")
    row14g08 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 線路不通")
    row14g09 = models.BooleanField(default=False, verbose_name="油壓系統  備註說明 => 閥心斷裂")
    row15c01 = models.BooleanField(default=False, verbose_name="潤滑系統  零件 => 油嘴")
    row15c02 = models.BooleanField(default=False, verbose_name="潤滑系統  零件 => 分油器")
    row15c03 = models.BooleanField(default=False, verbose_name="潤滑系統  零件 => 油管")
    row15c04 = models.BooleanField(default=False, verbose_name="潤滑系統  零件 => 油泵")
    row15d00 = models.CharField(default=".",max_length=99,verbose_name="潤滑系統  進度一")
    row15e00 = models.CharField(default=".",max_length=99,verbose_name="潤滑系統  進度二")
    row15f00 = models.CharField(default=".",max_length=99,verbose_name="潤滑系統  進度三")
    row15g00 = models.BooleanField(default=True,verbose_name="潤滑系統  備註說明  正常")
    row15g01 = models.BooleanField(default=False, verbose_name="潤滑系統  備註說明 => 管道不通")
    row15g02 = models.BooleanField(default=False, verbose_name="潤滑系統  備註說明 => 管道斷裂")
    row15g03 = models.BooleanField(default=False, verbose_name="潤滑系統  備註說明 => 泵心磨損")
    row16c01 = models.BooleanField(default=False, verbose_name="氮氣  零件 => 氮气钢瓶")
    row16c02 = models.BooleanField(default=False, verbose_name="氮氣  零件 => 氮气瓶油封")
    row16c03 = models.BooleanField(default=False, verbose_name="氮氣  零件 => 轴承带")
    row16d00 = models.CharField(default=".",max_length=99,verbose_name="氮氣  進度一")
    row16e00 = models.CharField(default=".",max_length=99,verbose_name="氮氣  進度二")
    row16f00 = models.CharField(default=".",max_length=99,verbose_name="氮氣  進度三")
    row16g00 = models.BooleanField(default=True,verbose_name="氮氣  備註說明  正常")
    row16g01 = models.BooleanField(default=False, verbose_name="氮氣  備註說明 => 鋼瓶裂縫")
    row16g02 = models.BooleanField(default=False, verbose_name="氮氣  備註說明 => 壓力過高")
    row16g03 = models.BooleanField(default=False, verbose_name="氮氣  備註說明 => 壓力過低")
    row16g04 = models.BooleanField(default=False, verbose_name="氮氣  備註說明 => 磨损")
    row17c01 = models.BooleanField(default=False, verbose_name="锁模系统  零件 => 电子尺")
    row17d00 = models.CharField(default=".",max_length=99,verbose_name="锁模系统  進度一")
    row17e00 = models.CharField(default=".",max_length=99,verbose_name="锁模系统  進度二")
    row17f00 = models.CharField(default=".",max_length=99,verbose_name="锁模系统  進度三")
    row17g00 = models.BooleanField(default=True,verbose_name="锁模系统  備註說明  正常")
    row17g01 = models.BooleanField(default=False, verbose_name="锁模系统  備註說明 => 读数不准")
    row18c01 = models.BooleanField(default=False, verbose_name="自動噴霧  零件 => 雾化器")
    row18c02 = models.BooleanField(default=False, verbose_name="自動噴霧  零件 => 喷雾机板")
    row18c03 = models.BooleanField(default=False, verbose_name="自動噴霧  零件 => 铜管")
    row18c04 = models.BooleanField(default=False, verbose_name="自動噴霧  零件 => 电磁阀")
    row18c05 = models.BooleanField(default=False, verbose_name="自動噴霧  零件 => 缓冲器")
    row18d00 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧  進度一")
    row18e00 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧  進度二")
    row18f00 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧  進度三")
    row18g00 = models.BooleanField(default=True,verbose_name="自動噴霧  備註說明  正常")
    row18g01 = models.BooleanField(default=False, verbose_name="自動噴霧  備註說明 => 霧化器損壞")
    row18g02 = models.BooleanField(default=False, verbose_name="自動噴霧  備註說明 => 線路不通")
    row18g03 = models.BooleanField(default=False, verbose_name="自動噴霧  備註說明 => 緩衝彈簧斷裂")
    row18g04 = models.BooleanField(default=False, verbose_name="自動噴霧  備註說明 => 喷头螺丝滑牙")
    row18g05 = models.BooleanField(default=False, verbose_name="自動噴霧  備註說明 => 断裂")
    row18g06 = models.BooleanField(default=False, verbose_name="自動噴霧  備註說明 => 漏水")
    row19c01 = models.BooleanField(default=False, verbose_name="自動取出  零件 => 取件机手臂")
    row19c02 = models.BooleanField(default=False, verbose_name="自動取出  零件 => 缓冲器")
    row19c03 = models.BooleanField(default=False, verbose_name="自動取出  零件 => 夹手")
    row19c04 = models.BooleanField(default=False, verbose_name="自動取出  零件 => 轴承")
    row19c05 = models.BooleanField(default=False, verbose_name="自動取出  零件 => 马达")
    row19d00 = models.CharField(default=".",max_length=99,verbose_name="自動取出  進度一")
    row19e00 = models.CharField(default=".",max_length=99,verbose_name="自動取出  進度二")
    row19f00 = models.CharField(default=".",max_length=99,verbose_name="自動取出  進度三")
    row19g00 = models.BooleanField(default=True,verbose_name="自動取出  備註說明  正常")
    row19g01 = models.BooleanField(default=False, verbose_name="自動取出  備註說明 => 手臂断裂")
    row19g02 = models.BooleanField(default=False, verbose_name="自動取出  備註說明 => 夹手磨损")
    row19g03 = models.BooleanField(default=False, verbose_name="自動取出  備註說明 => 缓冲器坏")
    row19g04 = models.BooleanField(default=False, verbose_name="自動取出  備註說明 => 手臂轴承坏")
    row19g05 = models.BooleanField(default=False, verbose_name="自動取出  備註說明 => 内部烧坏")
    row20c01 = models.BooleanField(default=False, verbose_name="模具  零件 => 模芯")
    row20c02 = models.BooleanField(default=False, verbose_name="模具  零件 => 顶针")
    row20c03 = models.BooleanField(default=False, verbose_name="模具  零件 => 滑块")
    row20c04 = models.BooleanField(default=False, verbose_name="模具  零件 => 定模仁")
    row20c05 = models.BooleanField(default=False, verbose_name="模具  零件 => 动模仁")
    row20c06 = models.BooleanField(default=False, verbose_name="模具  零件 => 油缸")
    row20d00 = models.CharField(default=".",max_length=99,verbose_name="模具  進度一")
    row20e00 = models.CharField(default=".",max_length=99,verbose_name="模具  進度二")
    row20f00 = models.CharField(default=".",max_length=99,verbose_name="模具  進度三")
    row20g00 = models.BooleanField(default=True,verbose_name="模具  備註說明  正常")
    row20g01 = models.BooleanField(default=False, verbose_name="模具  備註說明 => 尺寸NG")
    row20g02 = models.BooleanField(default=False, verbose_name="模具  備註說明 => 模崩")
    row20g03 = models.BooleanField(default=False, verbose_name="模具  備註說明 => 模芯斷")
    row20g04 = models.BooleanField(default=False, verbose_name="模具  備註說明 => 顶针斷")
    row20g05 = models.BooleanField(default=False, verbose_name="模具  備註說明 => 重覆修模")
    row20g06 = models.BooleanField(default=False, verbose_name="模具  備註說明 => 待修模")

    def __str__(self):
        return self.headera

class Item003(models.Model):
    field1 = models.CharField(primary_key=True,max_length=200,verbose_name="壓鑄機編號")
    field1a = models.CharField(default=".",max_length=200,verbose_name="噸位")
    r01c6 = models.CharField(default=".",max_length=99,verbose_name="人員")
    r01c8 = models.CharField(default=".",max_length=99,verbose_name="日期")


#--- code1 for model.py (start) -----

    r03c3 = models.CharField(default=".",max_length=99,verbose_name="格林柱-零件")
    r03c4 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度一")
    r03c5 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度二")
    r03c6 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度三")
    r03c7 = models.CharField(default=".",max_length=99,verbose_name="格林柱-備註說明")
    r04c3 = models.CharField(default=".",max_length=99,verbose_name="機架底座-零件")
    r04c4 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度一")
    r04c5 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度二")
    r04c6 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度三")
    r04c7 = models.CharField(default=".",max_length=99,verbose_name="機架底座-備註說明")
    r05c3 = models.CharField(default=".",max_length=99,verbose_name="模板-零件")
    r05c4 = models.CharField(default=".",max_length=99,verbose_name="模板-進度一")
    r05c5 = models.CharField(default=".",max_length=99,verbose_name="模板-進度二")
    r05c6 = models.CharField(default=".",max_length=99,verbose_name="模板-進度三")
    r05c7 = models.CharField(default=".",max_length=99,verbose_name="模板-備註說明")
    r06c3 = models.CharField(default=".",max_length=99,verbose_name="合模-零件")
    r06c4 = models.CharField(default=".",max_length=99,verbose_name="合模-進度一")
    r06c5 = models.CharField(default=".",max_length=99,verbose_name="合模-進度二")
    r06c6 = models.CharField(default=".",max_length=99,verbose_name="合模-進度三")
    r06c7 = models.CharField(default=".",max_length=99,verbose_name="合模-備註說明")
    r07c3 = models.CharField(default=".",max_length=99,verbose_name="間隙-零件")
    r07c4 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度一")
    r07c5 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度二")
    r07c6 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度三")
    r07c7 = models.CharField(default=".",max_length=99,verbose_name="間隙-備註說明")
    r08c3 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-零件")
    r08c4 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度一")
    r08c5 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度二")
    r08c6 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度三")
    r08c7 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-備註說明")
    r10c3 = models.CharField(default=".",max_length=99,verbose_name="油管-零件")
    r10c4 = models.CharField(default=".",max_length=99,verbose_name="油管-進度一")
    r10c5 = models.CharField(default=".",max_length=99,verbose_name="油管-進度二")
    r10c6 = models.CharField(default=".",max_length=99,verbose_name="油管-進度三")
    r10c7 = models.CharField(default=".",max_length=99,verbose_name="油管-備註說明")
    r11c3 = models.CharField(default=".",max_length=99,verbose_name="過濾-零件")
    r11c4 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度一")
    r11c5 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度二")
    r11c6 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度三")
    r11c7 = models.CharField(default=".",max_length=99,verbose_name="過濾-備註說明")
    r12c3 = models.CharField(default=".",max_length=99,verbose_name="油箱-零件")
    r12c4 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度一")
    r12c5 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度二")
    r12c6 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度三")
    r12c7 = models.CharField(default=".",max_length=99,verbose_name="油箱-備註說明")
    r13c3 = models.CharField(default=".",max_length=99,verbose_name="馬達-零件")
    r13c4 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度一")
    r13c5 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度二")
    r13c6 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度三")
    r13c7 = models.CharField(default=".",max_length=99,verbose_name="馬達-備註說明")
    r15c3 = models.CharField(default=".",max_length=99,verbose_name="潤滑-零件")
    r15c4 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度一")
    r15c5 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度二")
    r15c6 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度三")
    r15c7 = models.CharField(default=".",max_length=99,verbose_name="潤滑-備註說明")
    r16c3 = models.CharField(default=".",max_length=99,verbose_name="氮氣-零件")
    r16c4 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度一")
    r16c5 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度二")
    r16c6 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度三")
    r16c7 = models.CharField(default=".",max_length=99,verbose_name="氮氣-備註說明")
    r17c3 = models.CharField(default=".",max_length=99,verbose_name="電控-零件")
    r17c4 = models.CharField(default=".",max_length=99,verbose_name="電控-進度一")
    r17c5 = models.CharField(default=".",max_length=99,verbose_name="電控-進度二")
    r17c6 = models.CharField(default=".",max_length=99,verbose_name="電控-進度三")
    r17c7 = models.CharField(default=".",max_length=99,verbose_name="電控-備註說明")
    r18c3 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-零件")
    r18c4 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度一")
    r18c5 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度二")
    r18c6 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度三")
    r18c7 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-備註說明")
    r19c3 = models.CharField(default=".",max_length=99,verbose_name="自動取出-零件")
    r19c4 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度一")
    r19c5 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度二")
    r19c6 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度三")
    r19c7 = models.CharField(default=".",max_length=99,verbose_name="自動取出-備註說明")
    r20c3 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-零件")
    r20c4 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度一")
    r20c5 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度二")
    r20c6 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度三")
    r20c7 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-備註說明")



class Item007(models.Model):
    field1 = models.CharField(primary_key=True,max_length=200,verbose_name="壓鑄機編號")
    field1a = models.CharField(default=".",max_length=200,verbose_name="噸位")
    r01c6 = models.CharField(default=".",max_length=99,verbose_name="人員")
    r01c8 = models.CharField(default=".",max_length=99,verbose_name="日期")


#--- code1 for model.py (start) -----

    r03c3 = models.CharField(default=".",max_length=99,verbose_name="格林柱-零件")
    r03c4 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度一")
    r03c5 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度二")
    r03c6 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度三")
    r03c7 = models.CharField(default=".",max_length=99,verbose_name="格林柱-備註說明")
    r03c7xx0 = models.NullBooleanField(verbose_name="格林柱-備註說明-正常")
    r03c7xx1 = models.NullBooleanField(verbose_name="格林柱-備註說明-磨損")
    r03c7xx2 = models.NullBooleanField(verbose_name="格林柱-備註說明-磨無法修復")


    r04c3 = models.CharField(default=".",max_length=99,verbose_name="機架底座-零件")
    r04c4 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度一")
    r04c5 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度二")
    r04c6 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度三")
    r04c7 = models.CharField(default=".",max_length=99,verbose_name="機架底座-備註說明")
    r05c3 = models.CharField(default=".",max_length=99,verbose_name="模板-零件")
    r05c4 = models.CharField(default=".",max_length=99,verbose_name="模板-進度一")
    r05c5 = models.CharField(default=".",max_length=99,verbose_name="模板-進度二")
    r05c6 = models.CharField(default=".",max_length=99,verbose_name="模板-進度三")
    r05c7 = models.CharField(default=".",max_length=99,verbose_name="模板-備註說明")
    r06c3 = models.CharField(default=".",max_length=99,verbose_name="合模-零件")
    r06c4 = models.CharField(default=".",max_length=99,verbose_name="合模-進度一")
    r06c5 = models.CharField(default=".",max_length=99,verbose_name="合模-進度二")
    r06c6 = models.CharField(default=".",max_length=99,verbose_name="合模-進度三")
    r06c7 = models.CharField(default=".",max_length=99,verbose_name="合模-備註說明")
    r07c3 = models.CharField(default=".",max_length=99,verbose_name="間隙-零件")
    r07c4 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度一")
    r07c5 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度二")
    r07c6 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度三")
    r07c7 = models.CharField(default=".",max_length=99,verbose_name="間隙-備註說明")
    r08c3 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-零件")
    r08c4 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度一")
    r08c5 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度二")
    r08c6 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度三")
    r08c7 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-備註說明")
    r10c3 = models.CharField(default=".",max_length=99,verbose_name="油管-零件")
    r10c4 = models.CharField(default=".",max_length=99,verbose_name="油管-進度一")
    r10c5 = models.CharField(default=".",max_length=99,verbose_name="油管-進度二")
    r10c6 = models.CharField(default=".",max_length=99,verbose_name="油管-進度三")
    r10c7 = models.CharField(default=".",max_length=99,verbose_name="油管-備註說明")
    r11c3 = models.CharField(default=".",max_length=99,verbose_name="過濾-零件")
    r11c4 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度一")
    r11c5 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度二")
    r11c6 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度三")
    r11c7 = models.CharField(default=".",max_length=99,verbose_name="過濾-備註說明")
    r12c3 = models.CharField(default=".",max_length=99,verbose_name="油箱-零件")
    r12c4 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度一")
    r12c5 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度二")
    r12c6 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度三")
    r12c7 = models.CharField(default=".",max_length=99,verbose_name="油箱-備註說明")
    r13c3 = models.CharField(default=".",max_length=99,verbose_name="馬達-零件")
    r13c4 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度一")
    r13c5 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度二")
    r13c6 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度三")
    r13c7 = models.CharField(default=".",max_length=99,verbose_name="馬達-備註說明")
    r15c3 = models.CharField(default=".",max_length=99,verbose_name="潤滑-零件")
    r15c4 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度一")
    r15c5 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度二")
    r15c6 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度三")
    r15c7 = models.CharField(default=".",max_length=99,verbose_name="潤滑-備註說明")
    r16c3 = models.CharField(default=".",max_length=99,verbose_name="氮氣-零件")
    r16c4 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度一")
    r16c5 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度二")
    r16c6 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度三")
    r16c7 = models.CharField(default=".",max_length=99,verbose_name="氮氣-備註說明")
    r17c3 = models.CharField(default=".",max_length=99,verbose_name="電控-零件")
    r17c4 = models.CharField(default=".",max_length=99,verbose_name="電控-進度一")
    r17c5 = models.CharField(default=".",max_length=99,verbose_name="電控-進度二")
    r17c6 = models.CharField(default=".",max_length=99,verbose_name="電控-進度三")
    r17c7 = models.CharField(default=".",max_length=99,verbose_name="電控-備註說明")
    r18c3 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-零件")
    r18c4 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度一")
    r18c5 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度二")
    r18c6 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度三")
    r18c7 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-備註說明")
    r19c3 = models.CharField(default=".",max_length=99,verbose_name="自動取出-零件")
    r19c4 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度一")
    r19c5 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度二")
    r19c6 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度三")
    r19c7 = models.CharField(default=".",max_length=99,verbose_name="自動取出-備註說明")
    r20c3 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-零件")
    r20c4 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度一")
    r20c5 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度二")
    r20c6 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度三")
    r20c7 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-備註說明")


#--- code1 for model.py (end) -----


    def __str__(self):
        return self.field1



class Item004(models.Model):
    def __str__(self):
        return self.f01+" "+self.f02+" "+self.f03+" "+str(self.f06)+" ";

    f01 = models.CharField(default=".", max_length=99,verbose_name="客戶")
    f02 = models.CharField(default=".", max_length=99,verbose_name="量產訂單號")
    f03 = models.CharField(default=".", max_length=99,verbose_name="產品代碼")
    f04 = models.CharField(default=".", max_length=99,verbose_name="產品名稱")

    f05 = models.CharField(default=".", max_length=99,verbose_name="計劃交期")
   # f05 = models.CharField(default=".", max_length=99,verbose_name="計劃交期")
    f05 = models.DateField(verbose_name="計劃交期")
    # f06 = models.CharField(default=".", max_length=99,verbose_name="訂單量")
    #  f07 = models.CharField(default=".", max_length=99,verbose_name="已交量")
    # f08 = models.CharField(default=".", max_length=99,verbose_name="未交量")
    # f09 = models.CharField(default=".", max_length=99,verbose_name="備庫量")
    # f10 = models.CharField(default=".", max_length=99,verbose_name="欠備庫量")
    # f11 = models.CharField(default=".", max_length=99,verbose_name="客訴量")
    # http://stackoverflow.com/questions/16527308/how-to-set-null-for-integerfield-instead-of-setting-0
    f06 = models.IntegerField(default=0,verbose_name="訂單量")

    f07 = models.IntegerField(default=0,verbose_name="已交量")
    f08 = models.IntegerField(default=0,verbose_name="未交量")
    f09 = models.IntegerField(default=0,verbose_name="備庫量")
    f10 = models.IntegerField(default=0,verbose_name="欠備庫量")
    f11 = models.IntegerField(default=0,verbose_name="客訴量")
    f12 = models.CharField(default=".", max_length=99,verbose_name="模具壽命")

# by Mark,2016-08-24 10:20 copy Item004
# http://stackoverflow.com/questions/16527308/how-to-set-null-for-integerfield-instead-of-setting-0
class Item002v2(models.Model):
    f01 = models.CharField(default=".", max_length=99,verbose_name="客戶")
    f02 = models.CharField(default=".", max_length=99,verbose_name="量產訂單號")
    f03 = models.CharField(default=".", max_length=99,verbose_name="產品代碼")
    f04 = models.CharField(default=".", max_length=99,verbose_name="產品名稱")
    f05 = models.DateField(null=True, verbose_name="計劃交期")
    f06 = models.IntegerField(default=0,verbose_name="訂單量")
    f07 = models.IntegerField(default=0,verbose_name="已交量")
    f08 = models.IntegerField(default=0,verbose_name="未交量")
    f09 = models.IntegerField(default=0,verbose_name="備庫量")
    f10 = models.IntegerField(default=0,verbose_name="欠備庫量")
    f11 = models.IntegerField(default=0,verbose_name="客訴量")
    f12 = models.CharField(default=".", max_length=99,verbose_name="模具壽命")
    def __str__(self):
        return self.f01+" "+self.f02+" "+self.f03+" "+str(self.f06)+" ";


class Item005(models.Model):
    f01 = models.CharField(default=".", max_length=99,verbose_name="客戶")
    f02 = models.CharField(default=".", max_length=99,verbose_name="量產訂單號")
    f03 = models.CharField(default=".", max_length=99,verbose_name="產品代碼")
    f04 = models.CharField(default=".", max_length=99,verbose_name="產品名稱")
    f04a = models.CharField(default=".", max_length=99,verbose_name="單件品名")
    f04b = models.CharField(default=".", max_length=99,verbose_name="機台噸位")
    f05 = models.DateField(null=True, verbose_name="計劃交期")
    f06 = models.IntegerField(default=0,verbose_name="訂單量")
    f07 = models.IntegerField(default=0,verbose_name="已交量")
    f08 = models.IntegerField(default=0,verbose_name="未交量")
    # f09 = models.IntegerField(default=0,verbose_name="備庫量")
    f10 = models.IntegerField(default=0,verbose_name="欠備庫量")
    # f11 = models.IntegerField(default=0,verbose_name="客訴量")
    # f12 = models.CharField(default=".", max_length=99,verbose_name="模具壽命")
    stat1 = models.CharField(default=".", max_length=250,verbose_name="進度一")
    stat2 = models.CharField(default=".", max_length=250,verbose_name="進度二")
    stat3 = models.CharField(default=".", max_length=250,verbose_name="進度三")

    def __str__(self):
        return self.f01+" "+self.f02+" "+self.f03+" "+str(self.f06)+" ";

class Item006(models.Model):
    f01 = models.CharField(default=".", max_length=99,verbose_name="客戶")
    f02 = models.CharField(default=".", max_length=99,verbose_name="量產訂單號")
    f03 = models.CharField(default=".", max_length=99,verbose_name="產品代碼")
    f04 = models.CharField(default=".", max_length=99,verbose_name="產品名稱")
    f04a = models.CharField(default=".", max_length=99,verbose_name="單件品名")
    f04b = models.CharField(default=".", max_length=99,verbose_name="機台噸位")
    f05 = models.DateField(null=True, verbose_name="計劃交期")
    f06 = models.IntegerField(default=0,verbose_name="訂單量")
    f07 = models.IntegerField(default=0,verbose_name="已交量")
    f08 = models.IntegerField(default=0,verbose_name="未交量")
    # f09 = models.IntegerField(default=0,verbose_name="備庫量")
    f10 = models.IntegerField(default=0,verbose_name="欠備庫量")
    # f11 = models.IntegerField(default=0,verbose_name="客訴量")
    # f12 = models.CharField(default=".", max_length=99,verbose_name="模具壽命")
    stat1 = models.CharField(default=".", max_length=250,verbose_name="進度一")
    stat2 = models.CharField(default=".", max_length=250,verbose_name="進度二")
    stat3 = models.CharField(default=".", max_length=250,verbose_name="進度三")

    def __str__(self):
        return self.f01+" "+self.f02+" "+self.f03+" "+str(self.f06)+" ";

#   机台吨位	生产订单号	物料代码	物料说明	材料	订单数量	未生产数量
# 工时（M）	生产周期（H）	生产天数（D）

class Item010(models.Model):
    f01 = models.CharField(default=".", max_length=99,verbose_name="机台吨位")
    f02 = models.CharField(default=".", max_length=99,verbose_name="生产订单号")
    f03 = models.CharField(default=".", max_length=99,verbose_name="物料代码")
    f04 = models.CharField(default=".", max_length=99,verbose_name="物料说明")
    f05 = models.CharField(default=".", max_length=99,verbose_name="材料")
    f06 = models.IntegerField(default=0,verbose_name="订单数量")
    f07 = models.IntegerField(default=0,verbose_name="未生产数量")
    f08 = models.FloatField(default=0,verbose_name="工时")
    f09 = models.FloatField(default=0,verbose_name="生产周期")
    f10 = models.FloatField(default=0,verbose_name="生产天数")
    def __str__(self):
        return self.f01+" "+self.f02+" "+self.f03+" "+str(self.f06)+" ";
class Item011(models.Model):
    f01 = models.CharField(default=".", max_length=99,verbose_name="机台吨位")
    f02 = models.CharField(default=".", max_length=99,verbose_name="生产订单号")
    f03 = models.CharField(default=".", max_length=99,verbose_name="物料代码")
    f04 = models.CharField(default=".", max_length=99,verbose_name="物料说明")
    f05 = models.CharField(default=".", max_length=99,verbose_name="材料")
    f06 = models.IntegerField(default=0,verbose_name="订单数量")
    f07 = models.IntegerField(default=0,verbose_name="未生产数量")
    f08 = models.FloatField(default=0,verbose_name="工时")
    f09 = models.FloatField(default=0,verbose_name="生产周期")
    f10 = models.FloatField(default=0,verbose_name="生产天数")
    def __str__(self):
        return self.f01+" "+self.f02+" "+self.f03+" "+str(self.f06)+" ";


class Item012(models.Model):
    f01 = models.CharField(default=".", max_length=99,verbose_name="生产订单号")
    f02 = models.CharField(default=".", max_length=99,verbose_name="物料代码")
    f03 = models.CharField(default=".", max_length=99,verbose_name="物料说明")
    f04 = models.CharField(default=".", max_length=99,verbose_name="机台吨位")
    f05 = models.CharField(default=".", max_length=99,verbose_name="材质")
    f06 = models.FloatField(default=0,verbose_name="工时定额(分钟）")
    f07 = models.IntegerField(default=0,verbose_name="模穴")
    f08 = models.IntegerField(default=0,verbose_name="订单数量")
    f09 = models.IntegerField(default=0,verbose_name="已生产数量")
    f10 = models.IntegerField(default=0,verbose_name="未生产数量")
    f11 = models.FloatField(default=0,verbose_name="合计工时(小时）")
    f12 = models.DateField(verbose_name="下单日期")
    f13 = models.CharField(default=".", max_length=99,verbose_name="压铸交货日期")
    f14 = models.CharField(default=".", max_length=99,verbose_name="责任生管")

    def __str__(self):
        return self.f01+" "+self.f02+" "+self.f03+" "+str(self.f06)+" ";
