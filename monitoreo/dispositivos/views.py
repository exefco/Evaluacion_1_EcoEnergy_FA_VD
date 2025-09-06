from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Device,Zone,Category,Measurement,Alert,Organization

def inicio(request):
    empresa = request.session.get("empresa")
    if not empresa:
        return redirect("login")
    devices = Device.objects.filter(organization__name=empresa)
    categoria_id = request.GET.get("categoria")
    if categoria_id:
        devices = devices.filter(category_id=categoria_id)
    zones = Zone.objects.filter(device__in=devices).annotate(num_devices=Count("device", distinct=True))
    categories = Category.objects.filter(device__in=devices).distinct()
    measurements = Measurement.objects.filter(device__in=devices)
    alerts = Alert.objects.filter(device__in=devices)
    

    return render(request, 'devices/panel.html',{'devices':devices,'zones':zones,'categories':categories,'measurements':measurements,'alerts':alerts,'empresa':empresa})

def devices_list(request):
    empresa = request.session.get("empresa")
    devices = Device.objects.filter(organization__name=empresa)
    categoria_id = request.GET.get("categoria")
    if categoria_id:
        devices = devices.filter(category_id=categoria_id)
    categories = Category.objects.filter(device__in=devices).distinct()
    return render(request, 'devices/devices_list.html', {'devices': devices, 'empresa': empresa, 'categories': categories})

def alerts_list(request):
    empresa = request.session.get("empresa")
    devices = Device.objects.filter(organization__name=empresa)
    alerts = Alert.objects.filter(device__in=devices)
    return render(request, 'devices/alerts_list.html', {'alerts': alerts, 'empresa': empresa})

def measurements_list(request):
    empresa = request.session.get("empresa")
    devices = Device.objects.filter(organization__name=empresa)
    measurements = Measurement.objects.filter(device__in=devices)
    return render(request, 'devices/measurements_list.html', {'measurements': measurements, 'empresa': empresa})
def device(request,device_id):
    empresa = request.session.get("empresa")
    device = Device.objects.get(id=device_id)
    measurements = Measurement.objects.filter(device=device)
    alerts = Alert.objects.filter(device=device)
    return render(request,"devices/device.html",{"device":device,'empresa':empresa,"measurements":measurements,"alerts":alerts})


def iniciarSesion(request): 
    if request.method == "POST":
        empresa_nombre = request.POST.get("empresa")
        if not empresa_nombre:
            return render(request, "devices/login.html", {"error": "Por favor ingrese el nombre de la empresa."})
        
        empresa = Organization.objects.filter(name=empresa_nombre).first()
        if not empresa:
            return render(request, "devices/login.html", {"error": "Empresa no encontrada."})
        
        request.session['empresa'] = empresa.name
        return redirect("panel")
    
    return render(request, "devices/login.html")

def register(request):
    if request.method == "POST":
        empresa = request.POST.get("empresa")
        correo = request.POST.get("correo")
        password = request.POST.get("password")
        mensaje = f"La empresa '{empresa}' fue registrada con el correo {correo}."
        return render(request, "devices/register_done.html", {"mensaje": mensaje})
    return render(request, "devices/register.html")

def recoverPassword(request):
    if request.method == "POST":
        empresa = request.POST.get("empresa")
        mensaje = f"Si la empresa '{empresa}' está registrada, recibirás un correo con instrucciones."
        return render(request, "devices/recoverpassword_done.html", {"mensaje": mensaje})
    return render(request, "devices/recoverpassword.html")
