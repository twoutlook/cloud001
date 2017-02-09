from django.contrib import admin

# from .models import Choice, Question,Feedback, Choice2
from .models import Choice, Question,Feedback


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
