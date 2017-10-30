# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
OPTIONAL = {'blank': True, 'null': True}


class BaseContent(models.Model):
    # This is base content table where i inherting for all tables
    ACTIVE_CHOICES = ((0, 'Inactive'), (2, 'Active'),)
    active = models.PositiveIntegerField(choices=ACTIVE_CHOICES,
                                         default=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def switch(self):
        self.active = {2: 0, 0: 2}[self.active]
        self.save()


class Category(BaseContent):
    # it defines what type of category that book belongs to
    name = models.CharField(max_length=200)

    admin_method = ['num_of_books']

    class Admin:
        inlines = ['Book']

    def __str__(self):
        return self.name

    def num_of_books(self):
        return self.book_set.count()

    def get_no_of_stockout(self):
        return len([i for i in Book.objects.filter(category=self)
                    if not i.has_stock()])


class Shelf(BaseContent):
    # Shelf is for find the place where book was stored
    serial_number = models.CharField(max_length=20)

    def __str__(self):
        return self.serial_number


class Book(BaseContent):
    title = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    author = models.CharField(max_length=100)
    category = models.ForeignKey('Category')
    shelf = models.ForeignKey('Shelf')

    def __str__(self):
        return self.title

    def has_stock(self):
        return bool(self.available_stock())

    def available_stock(self):
        from customer.models import Borrow
        return self.stock - Borrow.objects.filter(return_date=None,
                book=self).count()


