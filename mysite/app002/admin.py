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
from .models import T01

from import_export.admin import ImportExportModelAdmin

# class BookAdmin(ImportExportModelAdmin):
#     pass



# class Item004Resource(resources.ModelResource):

#     class Meta:
#         model = Item004



class Item000Admin(admin.ModelAdmin):
    list_display=['field1','field2','field3','field4','field5','field6']
admin.site.register(Item000,Item000Admin)

class T01Admin(admin.ModelAdmin):
    list_display=['f02','f03','f04']
admin.site.register(T01,T01Admin)
