# from import_export import resources
# from core.models import Book

# class BookResource(resources.ModelResource):

#     class Meta:
#         model = Book


from django.contrib import admin
from import_export.admin import ImportMixin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# from .models import Customer
from .models import Item000
from .models import Item001
from .models import Item002v2
# from .models import Item003
from .models import Item003v2

# from .models import Item004
from .models import Item005
from .models import Item006
from .models import Item007
from .models import Item008
from .models import Item009
from .models import Item010

from .models import Item012

# from .models import T01



from .models import Spec
# from .models import Cust

# class Item004Resource(resources.ModelResource):
#     class Meta:
#         model = Item004


from import_export.admin import ImportExportModelAdmin

# class BookAdmin(ImportExportModelAdmin):
#     pass

from .models import Flowchart, Flowchartprocess

class ProcessInline(admin.TabularInline):
    model = Flowchartprocess
    extra = 3


# class FlowchartAdmin(admin.ModelAdmin):
#     list_display = ('part_name','cust_name','by1')
#     fieldsets = [
#         (None,               {'fields': ['part_name','cust_name',]}),
#         ('基礎信息', {'fields': ['c1','c2','e1','e2','g1','g2',], 'classes': ['collapse']}),
#
#         ('人員日期', {'fields': ['by1','by1date','by2','by2date','by3','by3date',], 'classes': ['collapse']}),
#         # ('人員日期', {'fields': ['by1','by1date','by2','by2date','by2','by2date',], 'classes': ['collapse']}),
#     ]
#     inlines = [ProcessInline]
#
# admin.site.register(Flowchart, FlowchartAdmin)

class FlowchartAdmin(ImportExportModelAdmin):
    list_display = ('part_name','cust_name','by1')
    fieldsets = [
        (None,               {'fields': ['part_name','cust_name',]}),
        ('基礎信息', {'fields': ['c1','c2','e1','e2','g1','g2',], 'classes': ['collapse']}),

        ('人員日期', {'fields': ['by1','by1date','by2','by2date','by3','by3date',], 'classes': ['collapse']}),
        # ('人員日期', {'fields': ['by1','by1date','by2','by2date','by2','by2date',], 'classes': ['collapse']}),
    ]
    inlines = [ProcessInline]
admin.site.register(Flowchart,FlowchartAdmin)


class FlowchartprocessAdmin(ImportExportModelAdmin):
    list_display=['flowchart','a','b','c','d','e','f','g','h']
admin.site.register(Flowchartprocess,FlowchartprocessAdmin)


# 2016-12-05, by Mark
# 要廢丟這個小實驗，admin 畫面不再出現 APP001/T01s
# class T01Admin(admin.ModelAdmin):
#     list_display=['f02','f03','f04']
# admin.site.register(T01,T01Admin)



class Item000Admin(admin.ModelAdmin):
    list_display=['field1','field2','field3','field4','field5','field6']
admin.site.register(Item000,Item000Admin)


class SpecAdmin(admin.ModelAdmin):
    list_display=['field1','field2']
admin.site.register(Spec,SpecAdmin)

# class CustAdmin(admin.ModelAdmin):
#     list_display=['field1','field2']
# admin.site.register(Cust,CustAdmin)

# class Item002Admin(admin.ModelAdmin):
#     list_display=['field1','field2','field3','field4','field5','field6','field7']
# admin.site.register(Item002,Item002Admin)

# class Item004Admin(admin.ModelAdmin):
#     list_display=['f01','f02','f03','f04','f05','f06','f07','f08','f09','f10','f11','f12',]
# from import_export.admin import ImportExportModelAdmin
# class Item004Admin(ImportExportModelAdmin):
#     pass
# admin.site.register(Item004,Item004Admin)

class Item005Admin(ImportExportModelAdmin):
    pass
admin.site.register(Item005,Item005Admin)

class Item006Admin(ImportExportModelAdmin):
    pass
admin.site.register(Item006,Item006Admin)

# class Item007Admin(ImportExportModelAdmin):
#     pass
# admin.site.register(Item007,Item007Admin)

class Item008Admin(ImportExportModelAdmin):
    pass
admin.site.register(Item008,Item008Admin)

class Item009Admin(ImportExportModelAdmin):
    pass
admin.site.register(Item009,Item009Admin)

class Item010Admin(ImportExportModelAdmin):
    pass
admin.site.register(Item010,Item010Admin)

class Item012Admin(ImportExportModelAdmin):
    pass
admin.site.register(Item012,Item012Admin)


class Item001Admin(ImportExportModelAdmin):
    pass
admin.site.register(Item001,Item001Admin)



class Item002v2Admin(ImportExportModelAdmin):
    pass
admin.site.register(Item002v2,Item002v2Admin)


# class Item003Admin(ImportExportModelAdmin):
#     pass
# admin.site.register(Item003,Item003Admin)


# class Item001Admin(admin.ModelAdmin):
#     fieldsets = [
#         ('壓鑄機', {'fields': ['field1',]}),
#         ('噸位人員日期', {'fields': [ 'field1a','r01c6','r01c8',], 'classes': ['collapse']}),
#         # ('結構 - 格林柱', {'fields': ['r03c3','r03c4','r03c5','r03c6','r03c7',], 'classes': ['collapse']}),
#         # ('結構 - 機架底座', {'fields': ['r04c3','r04c4','r04c5','r04c6','r04c7',], 'classes': ['collapse']}),
# #--- code3 for admin.py (start) -----

#         ('結構-格林柱', {'fields': ['r03c3','r03c4','r03c5','r03c6','r03c7',], 'classes': ['collapse']}),
#         ('結構-機架底座', {'fields': ['r04c3','r04c4','r04c5','r04c6','r04c7',], 'classes': ['collapse']}),
#         ('結構-模板', {'fields': ['r05c3','r05c4','r05c5','r05c6','r05c7',], 'classes': ['collapse']}),
#         ('結構-合模', {'fields': ['r06c3','r06c4','r06c5','r06c6','r06c7',], 'classes': ['collapse']}),
#         ('結構-間隙', {'fields': ['r07c3','r07c4','r07c5','r07c6','r07c7',], 'classes': ['collapse']}),
#         ('結構-膜厚調節', {'fields': ['r08c3','r08c4','r08c5','r08c6','r08c7',], 'classes': ['collapse']}),
#         ('液壓油-油管', {'fields': ['r10c3','r10c4','r10c5','r10c6','r10c7',], 'classes': ['collapse']}),
#         ('液壓油-過濾', {'fields': ['r11c3','r11c4','r11c5','r11c6','r11c7',], 'classes': ['collapse']}),
#         ('液壓油-油箱', {'fields': ['r12c3','r12c4','r12c5','r12c6','r12c7',], 'classes': ['collapse']}),
#         ('液壓油-馬達', {'fields': ['r13c3','r13c4','r13c5','r13c6','r13c7',], 'classes': ['collapse']}),
#         ('潤滑', {'fields': ['r15c3','r15c4','r15c5','r15c6','r15c7',], 'classes': ['collapse']}),
#         ('氮氣', {'fields': ['r16c3','r16c4','r16c5','r16c6','r16c7',], 'classes': ['collapse']}),
#         ('電控', {'fields': ['r17c3','r17c4','r17c5','r17c6','r17c7',], 'classes': ['collapse']}),
#         ('自動噴霧', {'fields': ['r18c3','r18c4','r18c5','r18c6','r18c7',], 'classes': ['collapse']}),
#         ('自動取出', {'fields': ['r19c3','r19c4','r19c5','r19c6','r19c7',], 'classes': ['collapse']}),
#         ('自動切邊去毛', {'fields': ['r20c3','r20c4','r20c5','r20c6','r20c7',], 'classes': ['collapse']}),
#     ]
# #--- code3 for admin.py (end) -----    ]

#     list_display=[
#         'field1', 'field1a','r01c6','r01c8',
#         # 'r03c3','r03c4','r03c5','r03c6','r03c7',
#         # 'r04c3','r04c4','r04c5','r04c6','r04c7',

#      ]
# admin.site.register(Item001,Item001Admin)


# class Item003Admin(admin.ModelAdmin):
#     fieldsets = [
#         ('壓鑄機', {'fields': ['field1',]}),
#         ('噸位人員日期', {'fields': [ 'field1a','r01c6','r01c8',], 'classes': ['collapse']}),
#         # ('結構 - 格林柱', {'fields': ['r03c3','r03c4','r03c5','r03c6','r03c7',], 'classes': ['collapse']}),
#         # ('結構 - 機架底座', {'fields': ['r04c3','r04c4','r04c5','r04c6','r04c7',], 'classes': ['collapse']}),
# #--- code3 for admin.py (start) -----

#         ('結構-格林柱', {'fields': ['r03c3','r03c4','r03c5','r03c6','r03c7',], 'classes': ['collapse']}),
#         ('結構-機架底座', {'fields': ['r04c3','r04c4','r04c5','r04c6','r04c7',], 'classes': ['collapse']}),
#         ('結構-模板', {'fields': ['r05c3','r05c4','r05c5','r05c6','r05c7',], 'classes': ['collapse']}),
#         ('結構-合模', {'fields': ['r06c3','r06c4','r06c5','r06c6','r06c7',], 'classes': ['collapse']}),
#         ('結構-間隙', {'fields': ['r07c3','r07c4','r07c5','r07c6','r07c7',], 'classes': ['collapse']}),
#         ('結構-膜厚調節', {'fields': ['r08c3','r08c4','r08c5','r08c6','r08c7',], 'classes': ['collapse']}),
#         ('液壓油-油管', {'fields': ['r10c3','r10c4','r10c5','r10c6','r10c7',], 'classes': ['collapse']}),
#         ('液壓油-過濾', {'fields': ['r11c3','r11c4','r11c5','r11c6','r11c7',], 'classes': ['collapse']}),
#         ('液壓油-油箱', {'fields': ['r12c3','r12c4','r12c5','r12c6','r12c7',], 'classes': ['collapse']}),
#         ('液壓油-馬達', {'fields': ['r13c3','r13c4','r13c5','r13c6','r13c7',], 'classes': ['collapse']}),
#         ('潤滑', {'fields': ['r15c3','r15c4','r15c5','r15c6','r15c7',], 'classes': ['collapse']}),
#         ('氮氣', {'fields': ['r16c3','r16c4','r16c5','r16c6','r16c7',], 'classes': ['collapse']}),
#         ('電控', {'fields': ['r17c3','r17c4','r17c5','r17c6','r17c7',], 'classes': ['collapse']}),
#         ('自動噴霧', {'fields': ['r18c3','r18c4','r18c5','r18c6','r18c7',], 'classes': ['collapse']}),
#         ('自動取出', {'fields': ['r19c3','r19c4','r19c5','r19c6','r19c7',], 'classes': ['collapse']}),
#         ('自動切邊去毛', {'fields': ['r20c3','r20c4','r20c5','r20c6','r20c7',], 'classes': ['collapse']}),
#     ]
# #--- code3 for admin.py (end) -----    ]

#     list_display=[
#         'field1', 'field1a','r01c6','r01c8',
#         # 'r03c3','r03c4','r03c5','r03c6','r03c7',
#         # 'r04c3','r04c4','r04c5','r04c6','r04c7',

#      ]
# admin.site.register(Item003,Item003Admin)

class Item003v2Admin(ImportExportModelAdmin):
    pass
admin.site.register(Item003v2,Item003v2Admin)


# class Item003v2Admin(admin.ModelAdmin):
#     fieldsets = [
#         ('壓鑄機', {'fields': ['headera',]}),
#         ('噸位人員日期', {'fields': [ 'headerb','headerc','headerd',], 'classes': ['collapse']}),

#         # ('結構-格林柱', {'fields': ['data01a','data01b','data01c','data01d','data01e',], 'classes': ['collapse']}),

# ('結構 --  格林柱',{'fields':['data01a','data01b','data01c','data01d','data01e',], 'classes': ['collapse']}),
# ('結構 --  機架底座',{'fields':['data02a','data02b','data02c','data02d','data02e',], 'classes': ['collapse']}),
# ('結構 --  模板(定)',{'fields':['data03a','data03b','data03c','data03d','data03e',], 'classes': ['collapse']}),
# ('結構 --  模板(動)',{'fields':['data04a','data04b','data04c','data04d','data04e',], 'classes': ['collapse']}),
# ('結構 --  合模',{'fields':['data05a','data05b','data05c','data05d','data05e',], 'classes': ['collapse']}),
# ('結構 --  曲軸',{'fields':['data06a','data06b','data06c','data06d','data06e',], 'classes': ['collapse']}),
# ('結構 --  鋼帶',{'fields':['data07a','data07b','data07c','data07d','data07e',], 'classes': ['collapse']}),
# ('結構 --  膜厚調節',{'fields':['data08a','data08b','data08c','data08d','data08e',], 'classes': ['collapse']}),
# ('壓射系統  ',{'fields':['data09a','data09b','data09c','data09d','data09e',], 'classes': ['collapse']}),
# ('澆注系統 ',{'fields':['data10a','data10b','data10c','data10d','data10e',], 'classes': ['collapse']}),
# ('油壓系統 --  油管',{'fields':['data11a','data11b','data11c','data11d','data11e',], 'classes': ['collapse']}),
# ('油壓系統 --  過濾網',{'fields':['data12a','data12b','data12c','data12d','data12e',], 'classes': ['collapse']}),
# ('油壓系統 --  油箱',{'fields':['data13a','data13b','data13c','data13d','data13e',], 'classes': ['collapse']}),
# ('油壓系統 --  馬達',{'fields':['data14a','data14b','data14c','data14d','data14e',], 'classes': ['collapse']}),
# ('油壓系統 --  電磁閥',{'fields':['data15a','data15b','data15c','data15d','data15e',], 'classes': ['collapse']}),
# ('潤滑系統 ',{'fields':['data16a','data16b','data16c','data16d','data16e',], 'classes': ['collapse']}),
# ('氮氣 ',{'fields':['data17a','data17b','data17c','data17d','data17e',], 'classes': ['collapse']}),
# ('電路控制 ',{'fields':['data18a','data18b','data18c','data18d','data18e',], 'classes': ['collapse']}),
# ('自動噴霧 ',{'fields':['data19a','data19b','data19c','data19d','data19e',], 'classes': ['collapse']}),
# ('自動取出 ',{'fields':['data20a','data20b','data20c','data20d','data20e',], 'classes': ['collapse']}),
# ('模具 ',{'fields':['data21a','data21b','data21c','data21d','data21e',], 'classes': ['collapse']}),



#     ]
#     list_display=[
#         'headera','headerb','headerc','headerd'
#     ]
# admin.site.register(Item003v2,Item003v2Admin)
