from django.contrib import admin

# from .models import Choice, Question,Feedback, Choice2
from .models import Choice, Question,Feedback, Sop, Sopitem
from import_export.admin import ImportExportModelAdmin

# class ChoiceInline(admin.StackedInline):
# https://docs.djangoproject.com/en/1.10/intro/tutorial07/
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
# class FeedbackInline(admin.TabularInline):
#     model = Feedback
#     extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'is_active','was_published_recently','is_future_blog')

    fieldsets = [
        (None,               {'fields': ['is_active','question_text',]}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # inlines = [FeedbackInline]


admin.site.register(Question, QuestionAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('question', 'feedback', 'username','created')

admin.site.register(Feedback,FeedbackAdmin)


# 2017-02-17
# code = models.CharField('流程编号',max_length=16)
#     ver = models.CharField('版本',max_length=8)
#     ver_date = models.DateField('修订日期')
#     title = models.CharField(max_length=200)
#     dept = models.CharField('负责单位',max_length=16)
#     editor = models.CharField('修改人员',max_length=16)
#     page_num = models.CharField('页次',max_length=16)
#     intro = models



# 2017-02-17 SOP start
class SopitemInline(admin.TabularInline):
    model = Sopitem
    extra = 3
class SopAdmin(ImportExportModelAdmin):
    list_display = ('code', 'ver', 'ver_date','title','dept','editor','page_num')

    fieldsets = [
        (None,               {'fields': ['code','ver','ver_date','title','intro','diagram','page_num']}),
        ('负责单位|修改人员', {'fields': ['dept','editor'], 'classes': ['collapse']}),
    ]
    inlines = [SopitemInline]
admin.site.register(Sop,SopAdmin)
# 2017-02-17 SOP end
class SopitemAdmin(ImportExportModelAdmin):
    pass
admin.site.register(Sopitem,SopitemAdmin)