# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from ecomapp.models import Category, Product

def base_view(request):
    test="testing"
    categories=Category.objects.all()
    products=Product.objects.all()
    context={
        'categories': categories,
        'products':products
    }
    return render(request,'base.html',{})
