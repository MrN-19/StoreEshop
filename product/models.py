from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator

class ProductColor(models.Model):
    color_name = models.CharField(max_length=150,verbose_name="نام رنگ")
    color_code = models.CharField(max_length=100,verbose_name="کد رنگی")

    def __str__(self):
        return self.color_name
    class Meta:
        verbose_name = "رنگ محصول"
        verbose_name_plural = "رنگ محصولات"

class ProductSize(models.Model):
    size_name = models.CharField(max_length=200,verbose_name="نام سایز")

    def __str__(self):
        return self.size_name
    
    class Meta:
        verbose_name = "اندازه محصول"

class Product(models.Model):
    name = models.CharField(max_length=200,verbose_name="نام محصول")
    short_describtion = models.CharField(max_length=500,verbose_name="توضیح کوتاه")
    descrbtion = RichTextField(verbose_name = "متن توضیح")
    publish_date = models.DateTimeField(verbose_name="تاریخ انتشار",auto_now=True)
    price = models.FloatField(default=0,verbose_name="قیمت")
    is_discount = models.BooleanField(default=False,verbose_name="تخفیف دارد ؟")
    discount_percent = models.PositiveSmallIntegerField(default=0,verbose_name="درصد تخفیف",validators=[MaxValueValidator(100,message="درصد خفیف نمیتواند بیشتر از 100 باشد")])
    final_price = models.FloatField(default=0,verbose_name="قیمت نهایی")
    color = models.ManyToManyField(ProductColor,verbose_name="رنگ",null=True,blank=True)
    size = models.ManyToManyField(ProductSize,verbose_name="اندازه",null=True,blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

class ProductTags(models.Model):
    product = models.ForeignKey(Product,verbose_name="محصول",on_delete=models.CASCADE)
    tag_title = models.CharField(max_length=200,verbose_name="عنوان برچسب")

    def __str__(self):
        return self.tag_title + "----------" + " " + self.product.name

    class Meta:
        verbose_name = "برچسب محصول"
        verbose_name_plural = "بر چسب محصول"
    