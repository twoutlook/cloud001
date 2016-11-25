from django.contrib import admin

# Register your models here.
from .models import Flowchart, Flowchartprocess

class ProcessInline(admin.TabularInline):
    model = Flowchartprocess
    extra = 3


class FlowchartAdmin(admin.ModelAdmin):
    list_display = ('part_name','cust_name','by1')
    fieldsets = [
        (None,               {'fields': ['part_name','cust_name',]}),
        ('基礎信息', {'fields': ['c1','c2','e1','e2','g1','g2',], 'classes': ['collapse']}),

        ('人員日期', {'fields': ['by1','by1date','by2','by2date','by3','by3date',], 'classes': ['collapse']}),
        # ('人員日期', {'fields': ['by1','by1date','by2','by2date','by2','by2date',], 'classes': ['collapse']}),
    ]
    inlines = [ProcessInline]

admin.site.register(Flowchart, FlowchartAdmin)
