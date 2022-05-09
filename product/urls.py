from django.urls import path
from .views import get_product_by_category,single_product,get_product_by_tags
app_name = "product"

urlpatterns = [
    path("product-category/<slug>",get_product_by_category,name="getproductbycategory"),
    path("product/<slug>/<int:id>",single_product,name="singleproduct"),
    path("product/tags/<str:tag>",get_product_by_tags,name="getproductsbytag"),
    
]
