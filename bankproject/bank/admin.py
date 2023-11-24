from django.contrib import admin
from .models import Place, District, Branch, Service

# Register your models here.

admin.site.register(Place)
admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Service)
# admin.site.register(District)
# admin.site.register(Branch)