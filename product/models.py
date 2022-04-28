from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator
from utilities.utility import Calculator

class ProductCategory(models.Model):
    title = models.CharField(max_length=200,verbose_name="عنوان دسته بندی")
    is_header = models.BooleanField(default=False,verbose_name="آیا سر گروه است ؟")
    header = models.ForeignKey("self",on_delete=models.CASCADE,verbose_name="سر گروه",null=True,blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "دسته بندی محصول"
        verbose_name_plural = "دسته بندی محصولات"


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
        verbose_name_plural = "ااندازه محصول"

class Product(models.Model):
    name = models.CharField(max_length=200,verbose_name="نام محصول")
    category = models.ManyToManyField(ProductCategory,verbose_name="دسته بندی")
    short_describtion = models.CharField(max_length=500,verbose_name="توضیح کوتاه")
    descrbtion = RichTextField(verbose_name = "متن توضیح")
    publish_date = models.DateTimeField(verbose_name="تاریخ انتشار",auto_now=True)
    price = models.FloatField(default=0,verbose_name="قیمت")
    is_discount = models.BooleanField(default=False,verbose_name="تخفیف دارد ؟")
    discount_percent = models.PositiveSmallIntegerField(default=0,verbose_name="درصد تخفیف",validators=[MaxValueValidator(100,message="درصد خفیف نمیتواند بیشتر از 100 باشد")])
    final_price = models.FloatField(default=0,verbose_name="قیمت نهایی")
    color = models.ManyToManyField(ProductColor,verbose_name="رنگ",null=True,blank=True)
    size = models.ManyToManyField(ProductSize,verbose_name="اندازه",null=True,blank=True)
    is_active = models.BooleanField(default=False,verbose_name="وضیعت فعال بودن")
    image = models.ImageField(verbose_name="تصویر محصول",upload_to = "Product/Product",null=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        if self.is_discount:
            if self.discount_percent > 0:
                self.final_price = Calculator.calculate_percent(self.discount_percent,self.price)
            else:
                self.discount_percent = 0
                self.final_price = self.price
        else:
            if self.discount_percent > 0:
                self.discount_percent = 0
            self.final_price = self.price
        super(Product,self).save(*args,**kwargs) 


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
    
class ProductGallery(models.Model):
    title = models.CharField(max_length=100,verbose_name="عنوان",help_text="این متن زمانی که تصویر بارگذاری نشود ظاهر خواهد شد",null=True,blank=True)
    image = models.ImageField(verbose_name="تصویر",upload_to = "Product/ProductGallery")
    product = models.ForeignKey(Product,verbose_name="محصول",on_delete=models.CASCADE)
    
    def __str__(self):
        if self.title:
            return self.title
        return self.product.name


class BuyCount(models.Model):
    product = models.ForeignKey(Product,verbose_name="محصول",on_delete=models.CASCADE)
    count = models.PositiveBigIntegerField(default=0,verbose_name="تعداد خرید")
    def __str__(self):
        return self.product.name
    class Meta:
        verbose_name = "تعداد خرید محصول"
        verbose_name_plural = "تعداد خرید محصول"
    
