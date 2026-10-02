from django.contrib import admin
from stud.models import plant
from stud.models import fedback
from stud.models import address
from stud.models import PlantInfo
# Register your models here.
admin.site.register(plant)
admin.site.register(fedback)
admin.site.register(address)
admin.site.register(PlantInfo)
