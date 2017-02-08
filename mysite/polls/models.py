from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    ISACTIVE_CHOICES = (
       ('Y','Y'),
       ('N','N'),
    )
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # is_active=models.CharField("是否活躍", default='Y',choices = ISACTIVE_CHOICES,max_length=1 )
    is_active=models.BooleanField("是否活躍", default=True )
    def __str__(self):
        return self.question_text

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # https://docs.djangoproject.com/en/1.10/intro/tutorial05/
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def is_future_blog(self):
        now = timezone.now()
        return self.pub_date > now


    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '最近(?天)發佈的?'

    is_future_blog.admin_order_field = 'pub_date'
    is_future_blog.boolean = True
    is_future_blog.short_description = '預約帖?'

    is_active.admin_order_field = 'is_active'
    is_future_blog.boolean = True
    is_future_blog.short_description = 'Is it active?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    remark = models.CharField("Remark",default="..",max_length=200)
    
    def __str__(self):
        return self.choice_text
class Feedback(models.Model):
    FEEDBACK_CHOICES = (
       ('可以','可以'),
       ('不行','不行'),
       ('不知道','不知道'),

    )
    question = models.ForeignKey(Question)
    feeback_text = models.CharField("回覆",default="不知道",choices =FEEDBACK_CHOICES, max_length=200)
    username = models.CharField("用戶名",default=".",max_length=200)
    created = models.DateTimeField( auto_now=True)
    # votes = models.IntegerField(default=0)
    def __str__(self):
        return self.username