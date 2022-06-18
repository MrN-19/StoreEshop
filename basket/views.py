from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from product.models import Product
from django.http import JsonResponse
from .models import Basket

@require_POST
@login_required(login_url="account:login")
def add_into_basket(request):
    print("Hello World")
    product_id = request.POST.get("id")

    if str(product_id).isdigit():

        product = get_object_or_404(Product,id = product_id)
        
        if not Basket.objects.filter(product = product,user = request.user).exists():
            Basket.objects.create(
                user = request.user,
                product = product,
            )
            return JsonResponse({
                "message" : "محصول مورد نظر به سبد خرید افزوده شد"
            },safe=False,status = 200)
        return JsonResponse({"message" : "این محصول قبلا افزوده شده"},status = 400,safe = False)
    return JsonResponse({
        "message" : "خطا در انجام عملیات"
    },status = 400)
