from django.shortcuts import render,get_object_or_404,get_list_or_404
from .models import ProductCategory,Product


def get_product_by_category(request,slug):
    category = get_object_or_404(ProductCategory,slug = slug)
    products = get_list_or_404(Product,category = category)
    context = {
        "products" : products,
        "filtered" : 1
    }
    return render(request,"products/products.html",context)

