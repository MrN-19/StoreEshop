from django.db import models
from django.contrib.auth.models import User
from product.models import Product
class Basket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="محصول")
    added_date = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ثبت")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبد خرید"
