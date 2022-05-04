from django.shortcuts import render
from product.models import BuyCount, Product,ProductCategory
def home(request):
    all_product_recent = Product.objects.order_by("-publish_date").filter(is_active = True).all()[:6]
    categories_header = ProductCategory.objects.filter(is_header = True)
    categories = ProductCategory.objects.all()
    highest_products_bought = BuyCount.objects.order_by("-count").all()
    products_slider = Product.objects.filter(is_slider = True).all()
    context = {
        "products" : all_product_recent,
        "categories" : categories,
        "categories_header" : categories_header,
        "highest_products_bought" : highest_products_bought,
        "slider" : products_slider,
    }
    return render(request,"home.html",context)


