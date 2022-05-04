from django.contrib import admin
from . import models

class ProductTagInline(admin.TabularInline):
    model = models.ProductTags

class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductTagInline,)
    prepopulate_fields = ({"slug" : "name"},)

    
admin.site.register(models.ProductCategory)
admin.site.register(models.Product,ProductAdmin)

admin.site.register(models.ProductTags)
admin.site.register(models.ProductColor)
admin.site.register(models.ProductSize)
admin.site.register(models.BuyCount)