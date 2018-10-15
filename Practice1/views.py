from django.shortcuts import render
from django.shortcuts import redirect
from .models import User
from .forms import UserForm

def index(request):
    pass
    return render(request,'Practice1/index.html')

def login(request):
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
               user = User.objects.get(name=username)
               if user.password == password:
                   return redirect('/Practice1/index/')
               else:
                   message = '密码不正确'
            except:
               message = '用户名不存在'
        return render(request,'Practice1/login.html',locals())
    login_form = UserForm()
    return render(request,'Practice1/login.html',locals())

def register(request):
    pass
    return render(request,'Practice1/register.html')

def logout(request):
    pass
    return render(request,'/Practice1/index/')
