from django.http import HttpResponse
from django.shortcuts import render
from . import views
from django.contrib.auth.forms import UserCreationForm
from calendar import monthrange

from django.shortcuts import render, redirect
from datetime import date
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from datetime import timedelta as tdelta
from django.utils import timezone

import datetime
from datetime import date, timedelta, datetime

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
import _datetime

# Create your views here.
from .models import *
from .forms import CreateUserForm
from .forms import *
from .decorators import unauthenticated_user, allowed_users,admin_only
from django.contrib.auth.models import Group

@login_required(login_url='login')
#@allowed_users(allowed_roles=['libraryian'])
@admin_only

def home(request):
    return render(request,'user_account/dashboard.html')

# Create your views here.
@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'user_account/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    profile_form=StudentProfileForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profile_form = StudentProfileForm(request.POST)
        #profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            group = Group.objects.get(name='student')
            user.groups.add(group)

            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    return render(request, 'user_account/register.html',{'form':form,'profile_form':profile_form})





@unauthenticated_user
def teacher_register(request):
    form = CreateUserForm()
    profile_form=TeacherProfileForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profile_form = TeacherProfileForm(request.POST)
        #profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            group = Group.objects.get(name='teacher')
            user.groups.add(group)

            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    return render(request, 'user_account/teacher_register.html',{'form':form,'profile_form':profile_form})


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])

def student(request):
    return render(request,'user_account/student.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def teacher(request):
    return render(request, 'user_account/teacher.html')



