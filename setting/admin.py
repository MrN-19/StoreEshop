from django.contrib import admin
from .models import AppSetting,MoneyCurrency

admin.site.register(AppSetting)
admin.site.register(MoneyCurrency)
