from product.models import ProductCategory
from setting.models import AppSetting, MoneyCurrency
def site_logo(context):
    # this method will get site name and logo and contact info
    site_info = AppSetting.objects.last()
    return {
        "logo" : site_info.logo.url,
        "name" : site_info.name,
        "phone" : site_info.contact_info
    }

def get_currency(context):
    currency = MoneyCurrency.objects.last()
    if not currency:
        MoneyCurrency.objects.create(currency = "toman")
    return {
        "currency" : currency
    }
def get_all_categories(context):
    header_categories = ProductCategory.objects.filter(is_header = True)
    all_categories = ProductCategory.objects.all()
    return {
        "headers" : header_categories,
        "allcategories" : all_categories
    }
