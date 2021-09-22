from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.contrib import messages
from django.views.decorators.cache import cache_control
# Create your views here.

# Home page and login page views


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin(request):
    if request.session.has_key('admin-logged'):
        return redirect(adminhome)
    else:
        return render(request, 'admin.html')


# home page views
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminhome(request):
    print('ijhkj')
    if request.session.has_key('admin-logged'):
        users = User.objects.all()
        print('hi')
        print(users)
        return render(request, 'admin home.html', {'users': users})
    else:
        return redirect(admin)


# admin checking
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def submit(request):
    user_name = request.POST['username']
    password = request.POST['password']

    user_name1 = 'mejo'
    password1 = '123'

    if user_name == user_name1 and password == password1:
        request.session['admin-logged'] = True
        return redirect(adminhome)
    else:
        messages.error(request, "Incorrect email or password!!!")
        return redirect(admin)


# logout
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_logut(request):
    if request.session.has_key('admin-logged'):
        del request.session['admin-logged']
    return redirect(admin)


# User creation
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def create_user(request):
    if request.session.has_key('admin-logged'):
        return render(request, 'register.html')
    else:
        return redirect(admin)


# user edit
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit(request, id):

    if request.session.has_key('admin-logged'):
        users = User.objects.get(id=id)
        print(users)
        print('hjbbjh')
        return render(request, 'index edit.html', {'user': users})
    else:
        return redirect(admin)


# edit user details
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def submitedit(request, id):
    print('sdgsdgsdgssdgsd')
    if request.method == 'POST':
        firstname1 = request.POST['firstname']
        lastname1 = request.POST['lastname']
        username1 = request.POST['username']
        email1 = request.POST['email']
        print(firstname1)
        user2 = User.objects.get(id=id)

        user2.first_name = firstname1
        user2.last_name = lastname1
        user2.username = username1
        user2.email = email1
        user2.save()
    return redirect(adminhome)

# delete user details


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete(request, id):
    user3 = User.objects.get(id=id)
    user3.delete()
    return redirect(adminhome)
