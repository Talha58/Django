from django.shortcuts import render,redirect
from . forms import RegisterForm,LoginForm #giriş yapabilmek için dahil ettik

from django.contrib import messages   #message modülünü import ettik

from django.contrib.auth.models import User #user modeli aldık ki kullanıcı girişi yapabilelim
from django.contrib.auth import login,authenticate,logout #authenticate user ve password karşılaitıracak

# Create your views here.

def register(request):
    
    form = RegisterForm(request.POST or None) #Django kolaylığı ile aşağıdaki kodları bu şekilde kısaca yazarız
    if form.is_valid():   #bu durumda form.py içindeki clean metodu cagırılacaktır.
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username=username)   #yeni kullanıcıyı olusturduk
            newUser.set_password(password)   

            newUser.save()    #kullanıcı veritabanına kaydolmuş oldu
            login(request,newUser)   #hem kaydını yaptık hem de otomatik olarak sisteme giriş yaptırmış olduk
            
            messages.info(request,"Başarıyla Kayıt Oldunuz...")

            return redirect("index")

    context = {
        "form" : form
        }
    return render(request,"register.html",context)

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
            "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request,"Kullanıcı adı veya parola hatalı...")
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız...")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")