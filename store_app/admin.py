from django.contrib import admin 
from .models import *

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Products)
admin.site.register(ContactInfo)
admin.site.register(ContactForm)
admin.site.register(AskedQuestions)
