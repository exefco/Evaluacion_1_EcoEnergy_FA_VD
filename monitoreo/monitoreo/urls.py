"""
URL configuration for monitoreo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from dispositivos.views import inicio,device,iniciarSesion,recoverPassword,devices_list,alerts_list,measurements_list,register

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",inicio,name="panel"),
    path("device/<int:device_id>/",device,name="device"),
    path("login/",iniciarSesion,name="iniciarSesion"),
    path("password-reset/",recoverPassword,name="recoverpassword"),
    path("devices/",devices_list,name="devices_list"),
    path("alerts/",alerts_list,name="alerts_list"),
    path("measurements/",measurements_list,name="measurements_list"),
    path("register/",register,name="register"),
]
