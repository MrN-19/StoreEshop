from django.shortcuts import render,get_object_or_404,get_list_or_404
from .models import ProductCategory,Product
from django.utils.encoding import uri_to_iri

def get_product_by_category(request,slug):
    category = get_object_or_404(ProductCategory,slug = uri_to_iri(slug))
    products = Product.objects.filter(category = category).all()
    context = {
        "products" : products,
        "filtered" : 1,
        "category" : category.title
    }
    return render(request,"products/products.html",context)

