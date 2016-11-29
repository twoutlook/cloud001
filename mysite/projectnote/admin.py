
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
