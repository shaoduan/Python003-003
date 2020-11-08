from io import RawIOBase
from django.http import response, HttpResponse
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as ori_login
from django.contrib.auth import logout as ori_logout
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm
# Create your views here.


def login(request):
    # 用户是否已经登录， 已经登录的用户跳转到欢迎页
    if request.user.get_username():
        return redirect('/login/welcome')

    if request.method == 'GET':
        loginform = UserLoginForm()
        return render(request, 'login/login.html', {'form': loginform})

    elif request.method == 'POST':
        print("CSRF: " + request.POST.get('csrfmiddlewaretoken'))
        #username, password = request.POST.get('username'), request.POST.get('password')
        loginform = UserLoginForm(request.POST)
        if loginform.is_valid():
            username = loginform.cleaned_data.get('username')
            password = loginform.cleaned_data.get('password')
        # 验证
        user = authenticate(username=username, password=password)
        
        if user:
            # 登录
            ori_login(request, user)
            return redirect('/login/welcome')
        else:
            return render(request, 'login/login.html', {'form': loginform, 'error_message': "Password Wrong Or User Not Exist."})
    else:
        print('login failed')
        return render(request, 'login/login.html')

@login_required(login_url='/login/')
def welcome(request):
    # request.user
    return render(request, 'login/welcome.html')

def user_logout(request):
    # ori_logout在最后会执行以下语句: request.user = Anonymous()
    ori_logout(request)
    return redirect('/login')