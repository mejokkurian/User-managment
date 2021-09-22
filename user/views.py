import user
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from .models import Mobiles
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views.decorators.cache import cache_control


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.session.has_key('user-logged'):
        return redirect(home)
    print('login')
    if request.method == 'POST':
        print('logged')
        email = request.POST['email']
        password = request.POST['pass']
        print(email)
        print(password)
        user = auth.authenticate(username=email, password=password)
        print(user)

        if user is not None:
            print("dfgg")
            auth.login(request, user)
            request.session['user-logged'] = True
            return redirect(home)
        else:
            print('fdsfdfdgf')
            messages.info(request, 'invalid credentials')
            return redirect(login)

    else:
        print('logout')
        return render(request, 'index.html')


# register view
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    print('register request....')

    if request.method == 'POST':
        print(request.method)
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['your_email']
        password1 = request.POST['password']
        password2 = request.POST['comfirm_password']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'mail already taken!!!')
                return redirect(register)
            else:
                user = User.objects.create_user(
                    first_name=firstname, last_name=lastname, username=username, email=email, password=password1)
                user.save()

        else:
            messages.info(request, 'password is not matching')
            return redirect(register)
        return redirect(login)

    else:
        return render(request, 'register.html')


# home views
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    mobile1 = Mobiles()
    mobile1.name = 'Iphone'
    mobile1.price = 52000
    mobile1.descr = 'The iPhone is a line of smartphones designed and marketed by Apple Inc. that use Apples iOS mobile operating system'

    mobile2 = Mobiles()
    mobile2.name = 'Iphone 11'
    mobile2.price = 55000
    mobile2.descr = 'The iPhone is a smartphone made by Apple that combines a computer, iPod, digital camera and cellular phone into one device with a touchscreen interface'

    mobile3 = Mobiles()
    mobile3.name = 'Iphone 10'
    mobile3.price = 42000
    mobile3.descr = 'IPhone, a multipurpose handheld computing device combining mobile telephone, digital camera, music player, and personal computing technologies'

    mobes = [mobile1, mobile2, mobile3]
    if request.session.has_key('user-logged'):
        return render(request, 'home.html', {'mobes': mobes})
    else:
        return redirect(signin)


# signin views
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signin(request):
    return redirect(login)

# logout views


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    if request.session.has_key('user-logged'):
        del request.session['user-logged']
    return redirect(login)
