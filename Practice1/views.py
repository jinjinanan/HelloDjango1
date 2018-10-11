from django.shortcuts import render
from django.shortcuts import redirect
from .models import User

def index(request):
    pass
    return render(request,'Practice1/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            username = username.strip()
            try:
               user = User.objects.get(name=username)
               if user.password == password:
                   return redirect('/Practice1/index/')
               else:
                   message = '密码不正确'
            except:
               message = '用户名不存在'
        return render(request,'Practice1/login.html',{'message':message})
    return render(request,'Practice1/login.html')

def register(request):
    pass
    return render(request,'Practice1/register.html')

def logout(request):
    pass
    return render(request,'/Practice1/index/')
