from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import StdModelForm, SingUpForm
from .models import StudentModel

# Create your views here.

class StdRegisterView(View):
    def get(self, request):
        std_form = StdModelForm(label_suffix=' ')
        std_data = StudentModel.objects.all()
        return render(request, 'sms/std_registration.html', {'form': std_form, 'std_data': std_data})
        
    def post(self, request):
        if request.method == 'POST':
            std_form = StdModelForm(request.POST)
            if std_form.is_valid():
                std_reg = StudentModel()
                first_name = std_form.cleaned_data.get('first_name')
                last_name = std_form.cleaned_data.get('last_name')
                email = std_form.cleaned_data.get('email')
                password = std_form.cleaned_data.get('password')
                std_reg = StudentModel(first_name=first_name, last_name=last_name, email=email, password=password)
                std_reg.save()
                std_form = StdModelForm(label_suffix=' ')
            else:
                std_form = StdModelForm(label_suffix=' ')
            std_data = StudentModel.objects.all()
            return render(request, 'sms/std_registration.html', {'form': std_form, 'std_data': std_data})
        

class StRegistrationUpdateView(View):
    def get(self, request, pk):
        std_data = StudentModel.objects.get(id=pk)
        std_form = StdModelForm(instance=std_data, label_suffix=' ')
        return render(request, 'sms/std_registration_update.html', {'form': std_form, 'std_data': std_data})

    def post(self, request, pk):
        if request.method == 'POST':
            std_data = StudentModel.objects.get(id=pk)
            std_form = StdModelForm(request.POST, instance=std_data)
            if std_form.is_valid():
                std_form.save()
                # id = std_form.cleaned_data.get('id')
                # first_name = std_form.cleaned_data.get('first_name')
                # last_name = std_form.cleaned_data.get('last_name')
                # email = std_form.cleaned_data.get('email')
                # password = std_form.cleaned_data.get('password')
                # std_data = StudentModel(id=id, first_name=first_name, last_name=last_name, email=email, 
                #                         password=password)
                # std_data.save()
                return HttpResponseRedirect('/students/register/')
            else:
                return render(request, 'sms/std_registration_update.html', {'form': std_form})

class StRegistrationDeleteView(View):
    def get(self, request, pk):
        std_data = StudentModel.objects.get(id=pk)
        std_data.delete()
        return HttpResponseRedirect('/students/register/')
    

class SingUpView(View):
    def get(self, request):
        form = SingUpForm(label_suffix=' ')
        return render(request, 'sms/singup.html', {'signup_form': form})
    
    def post(self, request):
        if request.method == 'POST':
            users = User.objects.all()
            fm = SingUpForm(request.POST)
            if fm.is_valid():
                # for user in users:
                #     if user.username == fm.cleaned_data.get('username'):
                #         messages.error(request, 'Username already exisits!!!')
                #         return render(request, 'sms/singup.html', {'singup_form': fm})
                fm.save()
                messages.success(request, 'Account created successfully!!!')
                fm = SingUpForm(label_suffix=' ')
        return render(request, 'sms/singup.html', {'signup_form': fm})


class UserLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/students/profile/')
        else:
            fm = AuthenticationForm()
            return render(request, 'sms/login.html', {'login_form': fm})
    
    def post(self, request):
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data.get('username')
                upass = fm.cleaned_data.get('password')
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/students/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'sms/login.html', {'login_form': fm})
    

def profile_view(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'sms/profile.html', {'user': user})
    else:
        return HttpResponseRedirect('/students/user-login/')
    

def user_logout_view(request):
    logout(request)
    return HttpResponseRedirect('/students/user-login/')