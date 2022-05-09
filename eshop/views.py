from django.shortcuts import render
from product.models import BuyCount, Product,ProductCategory
from django.db.models import Q
from django.contrib import messages
def home(request):
    all_product_recent = Product.objects.order_by("-publish_date").filter(is_active = True).all()[:6]
    highest_products_bought = BuyCount.objects.order_by("-count").all()
    products_slider = Product.objects.filter(is_slider = True).all()
    context = {
        "products" : all_product_recent,
        "highest_products_bought" : highest_products_bought,
        "slider" : products_slider,
    }
    return render(request,"home.html",context)

def search(request):
    q = request.GET.get("q")
    context = {}
    if q:
        producst_found = Product.objects.filter(Q(name__icontains = q) | Q(short_describtion = q) | 
        Q(descrbtion = q)).all()
        if not producst_found:
            messages.error(request,"نتیجه ای یافت نشد",extra_tags="error")
        context["products"] = producst_found
        context["count"] = producst_found.count()
    return render(request,"products/products.html",context)


