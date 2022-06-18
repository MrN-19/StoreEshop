from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render,get_object_or_404,get_list_or_404
from .models import KeyValue, ProductCategory,Product, ProductColor, ProductComment, ProductGallery, ProductSpecific, ProductTags
from django.utils.encoding import uri_to_iri
from django.views.decorators.http import require_POST,require_GET,require_http_methods
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from utilities.utility import Calculator, StringModifier
@require_GET
def get_product_by_category(request,slug):
    category = get_object_or_404(ProductCategory,slug = uri_to_iri(slug))
    products = Product.objects.filter(category = category).all()
    context = {
        "products" : products,
        "filtered" : 1,
        "category" : category.title
    }
    return render(request,"products/products.html",context)

@require_GET
def single_product(request,slug,id):
    product = get_object_or_404(Product,slug = uri_to_iri(slug),id = id)
    product_galleries = ProductGallery.objects.filter(product = product)
    product_specifics = ProductSpecific.objects.filter(product = product)
    tags = ProductTags.objects.filter(product = product)
    comments_header = ProductComment.objects.filter(product = product,is_header = True,is_active = True)
    comments = ProductComment.objects.filter(product = product,is_active = True).all()
    print(comments)
    context = {
        "product" : product,
        "galleries" : product_galleries,
        "specifics" : product_specifics,
        "tags" : tags,
        "comments_header" : comments_header,
        "comments" : comments
    }
    return render(request,"products/singleproduct.html",context)
@require_GET
def get_product_by_tags(request,tag):
    if tag:
        tags = ProductTags.objects.filter(tag_title = tag)
        products = []
        for i in tags:
            products.append(i.product)
        context = {
            "products" : products
        }
        return render(request,"products/products.html",context)
    raise Http404()

@login_required(login_url = "account:login")
def set_comment(request):
    product_id = request.POST.get("id")
    comment = request.POST.get("comment")
    header = request.POST.get("header")
    http_referer = request.META.get("HTTP_REFERER")
    if product_id and comment:
        product = Product.objects.filter(id = product_id).first()
        if header and int(header) > 0:
            if product:
                ProductComment.objects.create(
                    product = product,user = request.user,
                    is_active = True,is_header = False,header_id = header
                )
            else:
                Product.objects.create(
                    product = product,user = request.user,is_header = True,
                    is_active = True
                )
            return redirect("/product/{0}/{1}?success=yes".format(product.slug,product.id))
    return redirect(http_referer)

