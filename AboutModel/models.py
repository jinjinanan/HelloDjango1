from django.db import models
from django.utils import timezone

class Person(models.Model):
    first_name = models.CharField(max_length=30,verbose_name='名字')
    last_name = models.CharField(max_length=30,default='',verbose_name='曾用名')
    age = models.IntegerField(default=0,verbose_name='年龄')
    brithday = models.DateField('生日',default=timezone.now)
    photo = models.FileField('照片',upload_to='media/',default='')

    def __str__(self):
        return self.first_name


'''一对多'''
# 递归外健
class Comment(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(default='')
    parent_comment = models.ForeignKey('self',on_delete=models.CASCADE,null=True) # 递归外健


# 一对多
class Car(models.Model):
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
    )
    modelName = models.CharField(max_length=20,verbose_name='汽车类型')

    def __str__(self):
        return self.modelName

class Manufacturer(models.Model):
    name = models.CharField(max_length=20,verbose_name='工厂名字')
    def __str__(self):
        return self.name

'''多对多'''

class Student(models.Model):
    name = models.CharField(max_length=128)

    def class_list(self):
        return ','.join([i.name for i in self.class_set.all()])

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Student,blank=True)

    def student_list(self):
        return ','.join(i.name for i in self.members.all())

    def __str__(self):
        return self.name






'''一对一'''
