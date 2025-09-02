from django.db import models

# Create your models here.

class BaseModel(models.Model):
    STATES = [
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo"),
    ]

    state = models.CharField(max_length=10, choices=STATES, default="ACTIVO")
    created_at = models.DateTimeField(auto_now_add=True)   # se asigna al crear
    updated_at = models.DateTimeField(auto_now=True)       # se actualiza cada vez que se guarda
    deleted_at = models.DateTimeField(null=True, blank=True)  # opcional para borrado lógico

    class Meta:
        abstract = True   # no crea tabla, solo se hereda

class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Zone(BaseModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Device(BaseModel):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    max_usage = models.IntegerField()

    def __str__(self):
        return self.nombre

class Measurement(BaseModel):
    device = models.ForeignKey(Device,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    usage = models.FloatField(default=0.0)

    def  __str__(self):
        return f"{self.device} - {self.usage} KWh"

class Alert(BaseModel):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alerta {self.device} - {self.message}"

class Organization(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Nombre de la Empresa : {self.name}"




