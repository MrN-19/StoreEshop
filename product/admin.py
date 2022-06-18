from django.contrib import admin
from . import models

class ProductTagInline(admin.TabularInline):
    model = models.ProductTags
class ProductGalleryInline(admin.TabularInline):
    model = models.ProductGallery

class KeyValueInline(admin.TabularInline):
    model = models.KeyValue
class ProductCommentInline(admin.TabularInline):
    model = models.ProductComment

class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductTagInline,ProductGalleryInline,ProductCommentInline)
    prepopulated_fields = {"slug" : ("name",)}
class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}

class ProductSpecificAdmin(admin.ModelAdmin):
    inlines = (KeyValueInline,)

admin.site.register(models.ProductCategory,ProductCategoryAdmin)
admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.ProductGallery)
admin.site.register(models.ProductTags)
admin.site.register(models.ProductColor)
admin.site.register(models.ProductSize)
admin.site.register(models.Brand)
admin.site.register(models.BuyCount)
admin.site.register(models.KeyValue)
admin.site.register(models.ProductSpecific,ProductSpecificAdmin)
admin.site.register(models.ProductComment)