from django.contrib import admin
from .models import Brand, CarModel, Car

admin.site.register(Brand)
admin.site.register(CarModel)
admin.site.register(Car)

admin.site.site_title = 'Transport'
admin.site.site_header = 'Transport'
