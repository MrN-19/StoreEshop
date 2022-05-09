from django.http import Http404
from django.shortcuts import render,get_object_or_404,get_list_or_404
from .models import KeyValue, ProductCategory,Product, ProductColor, ProductComment, ProductGallery, ProductSpecific, ProductTags
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

def single_product(request,slug,id):
    product = get_object_or_404(Product,slug = uri_to_iri(slug),id = id)
    product_galleries = ProductGallery.objects.filter(product = product)
    product_specifics = ProductSpecific.objects.filter(product = product)
    tags = ProductTags.objects.filter(product = product)
    comments = ProductComment.objects.filter(product = product)
    #specifics
    # end specifics
    context = {
        "product" : product,
        "galleries" : product_galleries,
        "specifics" : product_specifics,
        "tags" : tags,
        "comments" : comments
    }
    return render(request,"products/singleproduct.html",context)

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
