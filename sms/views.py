from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import StdModelForm
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