from django.urls import path
from .views import get_product_by_category
app_name = "product"

urlpatterns = [
    path("product-category/<slug>",get_product_by_category,name="getproductbycategory"),
    
]
