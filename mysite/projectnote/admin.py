
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
from  .models import Smm, Employee,Trans,Rpt,Sop,Sopitem, Dept, Cat,Sopdata, T100,T100item,Prog, Drill, Drillstep, Dailywork

# 2017-03-20
# 唐婷婷/叶盼
from  .models import Bpm

# 2017-04-06
# 唐婷婷/叶盼
from  .models import SqlStatement




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

    # https://www.djangoproject.com/start/
    list_filter = ('c',)

    ordering = ['c','d','e','a']

    # http://stackoverflow.com/questions/28512710/how-to-add-custom-search-box-in-django-admin
    search_fields = ('a', 'b', 'e')
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

class T100itemInline(admin.TabularInline):
    model = T100item
    extra = 3


class DeptAdmin(ImportExportModelAdmin):
    list_display = ('dept_name','order_seq')
admin.site.register(Dept,DeptAdmin)   


 # empe_name = models.CharField('姓名',max_length=16)
 #    work_date = models.DateField('日期')
 #    work_brief = models.CharField('工作要點',max_length=512)
 #    work_desc = models.CharField('工作內容',max_length=512)
 #    remarks = models.CharField('備註',max_length=512)
class DailyworkAdmin(ImportExportModelAdmin):
    list_display = ('empe_name','work_date','remarks','work_brief','work_desc')
    list_filter = ('work_date','empe_name')
    search_fields = ('remarks','work_brief', 'work_desc')
  
admin.site.register(Dailywork,DailyworkAdmin)   

# 2017-0-3-20
# 唐婷婷/叶盼
class BpmAdmin(ImportExportModelAdmin):
    
    list_display = ('dept_name','sop_name','bpm_type','note1','note2','note3','to_print','qry_t100','wait_t100','concern','dev_by','man_hr','form_name','process_name','step1_by','step2_by','step3_by','step4_by','complete_date')
    list_filter = ('dept_name','bpm_type','dev_by')
    search_fields = ('dept_name','sop_name')
  
admin.site.register(Bpm,BpmAdmin) 

class SopdataAdmin(ImportExportModelAdmin):
    list_display = ('cat','seq','sys','procedure')
admin.site.register(Sopdata,SopdataAdmin)   




class CatAdmin(ImportExportModelAdmin):
    list_display = ('cat_name','cat_seq')
admin.site.register(Cat,CatAdmin)   

class SopAdmin(ImportExportModelAdmin):
    list_display = ('dept2','cat2','cat','code', 'ver', 'ver_date','title','dept','editor','by2','is_active','is_bpm')
    search_fields = ('code', 'title')
    ordering = ['code']
    fieldsets = [
        (None,               {'fields': ['dept2','cat2','cat','code','ver','ver_date','title','intro','page_num','is_active','is_bpm']}),
        ('负责单位|修改人员|审核人员', {'fields': ['dept','editor','by2'], 'classes': ['collapse']}),
    ]
    inlines = [SopitemInline]
admin.site.register(Sop,SopAdmin)
# 2017-02-17 SOP end


class T100Admin(ImportExportModelAdmin):
    list_display = ('sop','code','name')
    search_fields = ('code', 'name')
    ordering = ['code']
    inlines = [T100itemInline]
    # fieldsets = [
    #     (None,               {'fields': ['dept2','cat2','cat','code','ver','ver_date','title','intro','page_num','is_active','is_bpm']}),
    #     ('负责单位|修改人员|审核人员', {'fields': ['dept','editor','by2'], 'classes': ['collapse']}),
    # ]
    # inlines = [SopitemInline]
admin.site.register(T100,T100Admin)


class SopitemAdmin(ImportExportModelAdmin):
    pass
admin.site.register(Sopitem,SopitemAdmin)

class ProgAdmin(ImportExportModelAdmin):
    list_display=['code','name']
    ordering = ['code']
admin.site.register(Prog,ProgAdmin)


#  2017-04-06, Mark

class SqlStatementAdmin(ImportExportModelAdmin):
    list_display=['prj','seq','title','vcode','prog']
    ordering = ['prj','seq',]
admin.site.register(SqlStatement,SqlStatementAdmin)


class DrillstepInline(admin.TabularInline):
    model = Drillstep
    extra = 3

class DrillAdmin(ImportExportModelAdmin):
    list_display=['code','name']
    inlines = [DrillstepInline]
    
admin.site.register(Drill,DrillAdmin)