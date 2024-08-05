from django.urls import path, include
from cbvApp import views

app_name = 'cbvApp'

urlpatterns = [
    path('', views.CompanyListView.as_view(), name='companylist'),
    path('<int:pk>/', views.CompanyDetailView.as_view(), name='companydetail'),
    path('create/', views.CompanyCreateView.as_view(), name='company_create'),
    path('create_employee/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('delete/<int:pk>/', views.CompanyDeleteView.as_view(), name='company_delete'),
    path('update/<int:pk>/', views.CompanyUpdateView.as_view(), name='company_update'),
]