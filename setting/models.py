from django.db import models

class AppSetting(models.Model):
    name = models.CharField(max_length=200,verbose_name="نام سایت")
    logo = models.ImageField(verbose_name="لوگو",upload_to = "Setting/Logo")
    contact_info = models.CharField(max_length=50,verbose_name="پل ارتباطی",null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "تنظیمات برنامه"
        verbose_name_plural = "تنظیمات برنامه"
    
class MoneyCurrency(models.Model):
    CURRENCY = (
        ("toman","تومان"),("rial","ریال"),("dolor","دلار"),("euro","یورو")
    )
    currency = models.CharField(max_length=200,verbose_name="واحد پول",choices=CURRENCY)

    def __str__(self):
        return self.currency
    class Meta:
        verbose_name = "واحد پول"
        verbose_name_plural = "واحد پول"
    
