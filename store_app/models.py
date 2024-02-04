from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100, blank=True, null=True)
    img = models.ImageField(upload_to='CategoryImg', blank=True, null=True)

    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    categoris = models.ForeignKey( ProductCategory, verbose_name='Product Cetegory', on_delete=models.CASCADE )
    image = models.ImageField(upload_to='ProductImg/')
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    product_purchase_price = models.CharField(max_length=100, blank=True, null=True)
    sort_description = models.CharField(max_length=300,blank=True, null=True)
    description = models.CharField(max_length=300)
    aditional_discription = models.CharField(max_length=300, blank=True, null=True)
    stok_quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'New Arrivals Products'

    def __str__(self):
        return self.product_name
    
# class CardProduct(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     ordered = models.BooleanField(default=False)
#     product = models.ForeignKey(Products, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
    
#     class Meta:
#         verbose_name_plural =("CardProducts")

#     def __str__(self):
#         return self.product.product_name
    
# class OdderProduct(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE) 
#     card_product = models.ManyToManyField(CardProduct)
#     satrt_date = models.DateTimeField(auto_now_add=True)
#     order_date = models.DateTimeField()
#     ordered = models.BooleanField(default=False)
    
#     class Meta:
#         verbose_name_plural =("OdderProduct")

#     def __str__(self):
#         return self.card_product.product.product_name
    
# class CartItem(models.Model):
#     cart = models.ForeignKey(CardProduct, on_delete=models.CASCADE)
#     product = models.ForeignKey(Products, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)    


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    

    
    



class ContactInfo(models.Model):
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    working_days = models.CharField(max_length=500)
    info = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = 'Contact Info'

    def __str__(self):
        return self.address


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'Contact Form'

    def __str__(self):
        return self.name


class AskedQuestions(models.Model):
    questions = models.CharField(max_length=150)
    answer = models.CharField(max_length=600)

    class Meta:
        verbose_name_plural = 'Asked Questions'

    def __str__(self):
        return self.questions
