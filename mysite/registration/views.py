from django.shortcuts import render
from .models import Company, User, Event, UserEvent, BuildUserInformation
from .forms import UserInfoForm
from django.http import HttpResponse
from django.contrib import messages

def index(request):

    return render(request,'index.html')

def user_form(request):
    form = UserInfoForm()

    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            print "********************************************"
            print form
            return render(request, 'success.html', {'form': form})
        else:
            messages.error(request, "Error")

    return render(request, 'form_edit.html', {'form': form})


