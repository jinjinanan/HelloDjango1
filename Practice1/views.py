from django.shortcuts import render
from django.shortcuts import redirect
from .models import User
from .forms import UserForm,RegisterForm

def index(request):
    pass
    return render(request,'Practice1/index.html')

def login(request):
    if request.session.get('is_login',None):
        return redirect('/index/')
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
               user = User.objects.get(name=username)
               if user.password == password:
                   request.session['is_login'] = True
                   request.session['user_id'] = user.id
                   request.session['user_name'] = user.name
                   return redirect('/Practice1/index/')
               else:
                   message = '密码不正确'
            except:
               message = '用户名不存在'
        return render(request,'Practice1/login.html',locals())
    login_form = UserForm()
    return render(request,'Practice1/login.html',locals())

def register(request):
    if request.session.get('is_login',None):
        return redirect('/Practice1/index/')
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = '请检查填写的内容！'
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = '两次输入的密码不同'
                return render(request,'Practice1/register.html',locals())
            else:
                same_name_user = User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/Practice1/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request,'Practice1/register.html',locals())

def logout(request):
    if not request.session.get('is_login',None):
        return redirect('/Practice1/index/')
    request.session.flush()
    return render(request,'Practice1/index.html')
