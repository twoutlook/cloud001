
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
