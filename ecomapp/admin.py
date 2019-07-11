# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ecomapp.models import Category,Brand,Product,TitlePrepopulated
# admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Category,TitlePrepopulated)
