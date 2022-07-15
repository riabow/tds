from django.contrib import admin


from .models import Dogovor
from .models import My_settings

admin.site.register(Dogovor)
admin.site.register(My_settings)
