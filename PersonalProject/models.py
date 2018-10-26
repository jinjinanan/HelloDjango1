from django.db import models


class HomeMenu(models.Model):
    title = models.CharField(max_length=6,verbose_name='列表名字')

    def __str__(self):
        return self.title