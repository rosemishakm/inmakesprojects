from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User




# Create your views here.
def demo(request):
    return render(request,"index.html")



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('about')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email, password=password)
                user.save();

                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')

        return redirect('/')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect ('/')


def form(request):
    return render(request, 'form.html')


def about(request):
    return render(request, 'about.html')
