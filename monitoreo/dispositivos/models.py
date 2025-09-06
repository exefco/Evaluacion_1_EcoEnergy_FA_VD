from django.db import models


class BaseModel(models.Model):
    STATES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
    ]

    state = models.CharField(max_length=10, choices=STATES, default="ACTIVE")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Zone(BaseModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Organization(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Company name: {self.name}"

class Device(BaseModel):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    max_usage = models.IntegerField()
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Measurement(BaseModel):
    device = models.ForeignKey(Device,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    usage = models.FloatField(default=0.0)

    def  __str__(self):
        return f"{self.device} - {self.usage} KWh"

class Alert(BaseModel):
    LEVELS = [
        ("CRITICAL", "critical"),
        ("MID", "mid"),
        ("HIGH", "high"),
    ]
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=10, choices=LEVELS, default="mid")

    def __str__(self):
        return f"Alert: ({self.level} - {self.device}: {self.message})"