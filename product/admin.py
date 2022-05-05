from django.contrib import admin
from . import models

class ProductTagInline(admin.TabularInline):
    model = models.ProductTags

class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductTagInline,)
    prepopulated_fields = {"slug" : ("name",)}
class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    
admin.site.register(models.ProductCategory,ProductCategoryAdmin)
admin.site.register(models.Product,ProductAdmin)

admin.site.register(models.ProductTags)
admin.site.register(models.ProductColor)
admin.site.register(models.ProductSize)
admin.site.register(models.BuyCount)