
from django.contrib import admin
from import_export.admin import ImportMixin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# from .models import Customer

from import_export.admin import ImportExportModelAdmin

# class BookAdmin(ImportExportModelAdmin):
#     pass

from .models import  Note
from  .models import Smm, Employee,Trans,Rpt,Sop,Sopitem

class TransResource(resources.ModelResource):
    class Meta:
        model = Trans
class RptResource(resources.ModelResource):
    class Meta:
        model = Rpt



class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee
class SmmResource(resources.ModelResource):
    class Meta:
        model = Smm

class EmployeeAdmin(ImportExportModelAdmin):
    list_display=['a','b','c','d','e','f']
    ordering = ['c','d','e','a']
    resource_class = EmployeeResource
admin.site.register(Employee,EmployeeAdmin)

class SmmAdmin(ImportExportModelAdmin):
    list_display=['designation','pricedate','priceavg','yearnum','monthnum','quarternum']
    ordering = ['designation','pricedate']
    resource_class = SmmResource
admin.site.register(Smm,SmmAdmin)


class TransAdmin(ImportExportModelAdmin):
    list_display=['yrmonth','cat','a','b','c','d','e','f','g','h','i']
    ordering = ['yrmonth','cat','a','b']
    resource_class = TransResource
admin.site.register(Trans,TransAdmin)
class RptAdmin(ImportExportModelAdmin):
    list_display=['yrmonth','a','b','e','g','i','k']
    ordering = ['yrmonth','a','b']
    resource_class = RptResource
admin.site.register(Rpt,RptAdmin)

class NoteAdmin(ImportExportModelAdmin):
    list_display=['date1','tag','where','note','date2','fix']
admin.site.register(Note,NoteAdmin)

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

# 2017-02-17 SOP start
class SopitemInline(admin.TabularInline):
    model = Sopitem
    extra = 3

class SopAdmin(ImportExportModelAdmin):
    list_display = ('code', 'ver', 'ver_date','title','dept','editor','page_num')

    fieldsets = [
        (None,               {'fields': ['code','ver','ver_date','title','intro','page_num']}),
        ('负责单位|修改人员', {'fields': ['dept','editor'], 'classes': ['collapse']}),
    ]
    inlines = [SopitemInline]
admin.site.register(Sop,SopAdmin)
# 2017-02-17 SOP end
class SopitemAdmin(ImportExportModelAdmin):
    pass
admin.site.register(Sopitem,SopitemAdmin)