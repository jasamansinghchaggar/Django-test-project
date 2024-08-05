from django.shortcuts import render
from django.views.generic import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from cbvApp.models import Company, Employee
from django.urls import reverse, reverse_lazy


# Create your views here.

# def index(request):
#     return HttpResponse('<h1>Function Based View</h1>')

class IndexView(TemplateView):
    template_name = 'index.html'
    
class CompanyListView(ListView):
    model = Company
    template_name = 'cbvApp/companyList.html'
    context_object_name = 'companylist'

class CompanyDetailView(DetailView):
    model = Company
    template_name = 'cbvApp/companyDetail.html'
    context_object_name = 'companydetail'

class CompanyCreateView(CreateView):
    model = Company
    fields = '__all__'

class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('cbvApp:companylist')
    template_name = 'cbvApp/companyDelete.html'

class CompanyUpdateView(UpdateView):
    model = Company
    fields = '__all__'
    template_name = 'cbvApp/companyUpdate.html'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'