from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone

# Create your models here.

@python_2_unicode_compatible # 当你想支持python2版本的时候才需要这个装饰器
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):  # 在python2版本中使用的是__unique__
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200);
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
