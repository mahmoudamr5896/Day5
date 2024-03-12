"""
URL configuration for day4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from company import views


from company.views import DisplayEmp ,DisplayTeam, show_employees
from myapi.views import MyAPIView ,MyAPIView2,MyAPIView3

from rest_framework.routers import DefaultRouter

# view set url
router = DefaultRouter()
router.register(r'', MyAPIView3, basename='api-employee-3')



urlpatterns = [
    path("admin/", admin.site.urls),
    path('',DisplayEmp,name='DisplayEmp'), 
    path('api-employee-2/<int:pk>/', MyAPIView2.as_view(), name='api-employee-2'),

    path('team/',DisplayTeam,name='DisplayTeam'),
    path('employees/', show_employees, name='show_employees'),
    path('api-auth/', include('rest_framework.urls')),
    path('api-employee-2/',MyAPIView2.as_view(),name="api-employee-2"),
    path('api-employee-3/', include(router.urls)),
    path('MyAPIView/',MyAPIView,name='MyAPIView')
]
