from django.contrib import admin
from .models.models import Person,Comment,Car,Manufacturer,Student,Class
from .models.ModelForOperation import Blog,Author,Entry

class ClassAdmin(admin.ModelAdmin):
    list_display = ['id','name','student_list']

admin.site.register(Class,ClassAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','class_list']

admin.site.register(Student,StudentAdmin)

admin.site.register([Person,Comment,Car,Manufacturer,Blog,Author,Entry])

