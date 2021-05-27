# from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
#from .models import UserProfile
from .models import *
from calendar import monthrange

from django.shortcuts import render, redirect
from datetime import date
from django.http import HttpResponse, request
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
# from .forms import CreateUserForm,UserProfileForm
# from .forms import *
#from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group, User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class StudentProfileForm(forms.ModelForm):
    unique_Id = forms.CharField(max_length=11)
    phone_number = forms.CharField(max_length=10, min_length=10)

    class Meta:
        model = StudentProfile
        fields = ("phone_number", "address", "unique_Id")

    def clean_unique_ID(self):
        unique_id = self.cleaned_data['unique_ID']
        id_base = ID.objects.filter(unique_Id=unique_id)
        id_user = StudentProfile.objects.filter(unique_Id=unique_id)

        if id_user:
            raise forms.ValidationError("An account with this MisId already exits")
        elif not id_base:
            raise forms.ValidationError("You have entered the wrong MisId")
        elif id_base:
            return unique_id
        elif not id_user:
            return unique_id

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        lent = len(phone)
        if lent > 10 and lent < 10:
            raise forms.ValidationError("You have not entered a valid phone number")
        else:
            return phone



class TeacherProfileForm(forms.ModelForm):
    # unique_Id = forms.CharField(max_length=11)
    phone_number = forms.CharField(max_length=10, min_length=10)

    class Meta:
        model = TeacherProfile
        fields = ("phone_number", "address", "joining")

    # def clean_unique_ID(self):
    #     unique_id = self.cleaned_data['unique_ID']
    #     id_base = ID.objects.filter(unique_Id=unique_id)
    #     id_user = StudentProfile.objects.filter(unique_Id=unique_id)
    #
    #     if id_user:
    #         raise forms.ValidationError("An account with this MisId already exits")
    #     elif not id_base:
    #         raise forms.ValidationError("You have entered the wrong MisId")
    #     elif id_base:
    #         return unique_id
    #     elif not id_user:
    #         return unique_id

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        lent = len(phone)
        if lent > 10 and lent < 10:
            raise forms.ValidationError("You have not entered a valid phone number")
        else:
            return phone

