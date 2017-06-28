
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

# 2017-05-11
# by Mark,  together with 张韬 韜, 張 张一翔
from  .models import TechNote

# 2017-05-27
# by Mark,  together with 张韬 韜, 張 张一翔
from  .models import T100Todo

# 2017-05-27
# by Mark,  together with 张韬 韜, 張 张一翔
# from  .models import T100Todo2

# 2017-06-23
# by 張 张一翔,  together with  Mark,张韬 韜, 吴楠
from  .models import TrackT100

# 2017-06-23
# by 吴楠,  together with  Mark,张韬 韜,张一翔
from  .models import TrackPda

# 2017-06-23
# by 张韬,  together with  Mark,张韬 韜,张一翔
from  .models import TrackT100Report

# 2017-06-23
# by 张韬,  together with  Mark,张韬 韜
from  .models import TrackReport01

# 2017-06-23
# by 张韬,  together with  Mark,张韬 韜
from  .models import TrackReport00

# 2017-06-27
# by Mark
from  .models import T100Dept
from  .models import T100DeptTEST

#
class T100DeptResource(resources.ModelResource):
    class Meta:
        model = T100Dept
class T100DeptAdmin(ImportExportModelAdmin):
    list_display=['id','t100DeptId','t100DeptName','D0','D1','D2','D3','D4','D5','D6']
    ordering = ['t100DeptId']
    resource_class = T100DeptResource
admin.site.register(T100Dept,T100DeptAdmin)

#
class T100DeptTESTResource(resources.ModelResource):
    class Meta:
        model = T100DeptTEST
class T100DeptTESTAdmin(ImportExportModelAdmin):
    list_display=['t100Dept','note']
    ordering = ['t100Dept']
    resource_class = T100DeptTESTResource
admin.site.register(T100DeptTEST,T100DeptTESTAdmin)






class TransResource(resources.ModelResource):
    class Meta:
        model = Trans
class RptResource(resources.ModelResource):
    class Meta:
        model = Rpt



class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee

class TechNoteResource(resources.ModelResource):
    class Meta:
        model = TechNote

class T100TodoResource(resources.ModelResource):
    class Meta:
        model = T100Todo

# class T100Todo2Resource(resources.ModelResource):
#     class Meta:
#         model = T100Todo2

class TrackT100Resource(resources.ModelResource):
    class Meta:
        model = TrackT100

class TrackT100ReportResource(resources.ModelResource):
    class Meta:
        model = TrackT100Report

class TrackReport01Resource(resources.ModelResource):
    class Meta:
        model = TrackReport01

class TrackReport00Resource(resources.ModelResource):
    class Meta:
        model = TrackReport00

class TrackPdaResource(resources.ModelResource):
    class Meta:
        model = TrackPda


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



class TechNoteAdmin(ImportExportModelAdmin):
    list_display=['a','b','c']

    # https://www.djangoproject.com/start/
    list_filter = ('c',)

    ordering = ['a','b','c']

    # http://stackoverflow.com/questions/28512710/how-to-add-custom-search-box-in-django-admin
    search_fields = ('a', 'b', 'c')
    resource_class = TechNoteResource
admin.site.register(TechNote,TechNoteAdmin)


class T100TodoAdmin(ImportExportModelAdmin):
    list_display=['a','b','c','d','e','f']

    # https://www.djangoproject.com/start/
    # list_filter = ('f',)

    ordering = ['a','b','c','d','e']

    # http://stackoverflow.com/questions/28512710/how-to-add-custom-search-box-in-django-admin
    # search_fields = ('f')
    resource_class = T100TodoResource
admin.site.register(T100Todo,T100TodoAdmin)

# class T100Todo2Admin(ImportExportModelAdmin):
#     list_display=['a','b','c','d','e','f']
#
#     # https://www.djangoproject.com/start/
#     # list_filter = ('f',)
#
#     ordering = ['a','b','c','d','e']
#
#     # http://stackoverflow.com/questions/28512710/how-to-add-custom-search-box-in-django-admin
#     # search_fields = ('f')
#     resource_class = T100Todo2Resource
# admin.site.register(T100Todo2,T100Todo2Admin)

class TrackT100Admin(ImportExportModelAdmin):
    list_display=['a','b','c','d','e','f']

    # https://www.djangoproject.com/start/
    # list_filter = ('f',)

    ordering = ['a','b','c','d','e']

    # http://stackoverflow.com/questions/28512710/how-to-add-custom-search-box-in-django-admin
    # search_fields = ('f')
    resource_class = TrackT100Resource
admin.site.register(TrackT100,TrackT100Admin)

class TrackT100ReportAdmin(ImportExportModelAdmin):
    list_display=['a','b','c','d','e','f']

    # https://www.djangoproject.com/start/
    # list_filter = ('f',)

    ordering = ['a','b','c','d','e']

    # http://stackoverflow.com/questions/28512710/how-to-add-custom-search-box-in-django-admin
    # search_fields = ('f')
    resource_class = TrackT100ReportResource
admin.site.register(TrackT100Report,TrackT100ReportAdmin)

class TrackReport01Admin(ImportExportModelAdmin):
    list_display=['a','b','c','d','e','f']

    # https://www.djangoproject.com/start/
    # list_filter = ('f',)

    ordering = ['a','b','c','d','e']

    # http://stackoverflow.com/questions/28512710/how-to-add-custom-search-box-in-django-admin
    # search_fields = ('f')
    resource_class = TrackReport01Resource
admin.site.register(TrackReport01,TrackReport01Admin)

class TrackReport00Admin(ImportExportModelAdmin):
    # list_display=['t100DeptId','deptId','dept','a','b','c','d','e','f','h','k']
    list_display=['deptId','dept','a','b','c','d','e','f','h','k']

    # https://www.djangoproject.com/start/
    # list_filter = ('f',)

    ordering = ['dept','a']

    # http://stackoverflow.com/questions/28512710/how-to-add-custom-search-box-in-django-admin
    # search_fields = ('f')
    resource_class = TrackReport00Resource
admin.site.register(TrackReport00,TrackReport00Admin)

class TrackPdaAdmin(ImportExportModelAdmin):
    list_display=['a','b','c','d','e','f']

    # https://www.djangoproject.com/start/
    # list_filter = ('f',)

    ordering = ['a','b','c','d','e']

    # http://stackoverflow.com/questions/28512710/how-to-add-custom-search-box-in-django-admin
    # search_fields = ('f')
    resource_class = TrackPdaResource
admin.site.register(TrackPda,TrackPdaAdmin)


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
