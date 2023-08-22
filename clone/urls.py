"""
URL configuration for clone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from sitecode.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('signup/', Signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('dashboard/' , Dashboard , name= 'dashboard'),
    path('invoice/', invoice, name='invoice'),
    path('service/', service, name='service'),
    path('clientdetails/', addClient, name='clientdetail'),
    path('update_client/<int:item_id>/', update_client, name='update_client'),
    path('delete_client/<int:item_id>/', delete_client, name='delete_client'),

    
]
