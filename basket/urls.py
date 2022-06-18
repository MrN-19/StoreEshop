from django.urls import path
from . import views

app_name = "basket"

urlpatterns = [
    path("basket",views.add_into_basket,name="addintobasket"),

]