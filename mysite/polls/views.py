from django.shortcuts import render
from .models import Company, User, Event, User_event, Build_User_Information
from .forms import UserInfoForm
from django.http import HttpResponseRedirect

def index(request):

    return render(request,'index.html')


def user_information_form(request):
    form = UserInfoForm()
    return render(request, 'form_edit.html', {'form': form})

def submit_user_information_form(request):
    form = UserInfoForm()

    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('WOO HOO')
        else:
            messages.error(request, "Error")
    return render(request, 'success.html')
