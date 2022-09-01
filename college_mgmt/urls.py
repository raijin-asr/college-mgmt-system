"""college_mgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import views
from college_mgmt.views import AdminHomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('',include('registration.urls')),
    path('',include('user_mgmt.urls')),
    path('about_home',views.about_home,name='about_home'),
    path('about_admin',views.about_admin,name='about_admin'),
    path('contact',views.contact,name='contact'),
    path('admin_home', AdminHomeView.as_view(), name="Admin_home"),


]
