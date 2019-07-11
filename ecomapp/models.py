# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('category_detail',kwargs={'category_slug':self.slug})

class TitlePrepopulated(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)


class ProductManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(ProductManager, self).get_queryset().filter(available=True)


class Product(models.Model):
    category = models.ForeignKey(Category)
    brand = models.ForeignKey(Brand)
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    available = models.BooleanField(default=True)
    objects=ProductManager()

    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('product_detail',kwargs={'product_slug':self.slug})