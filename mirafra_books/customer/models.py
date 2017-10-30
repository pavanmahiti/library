# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from books.models import BaseContent, OPTIONAL
from datetime import datetime
# Create your models here.

class Customer(BaseContent):
    # for customer information who use library
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=250, **OPTIONAL)
    customer_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    def get_dues(self):
        return self.borrow_set.filter(
                    due_date__lte=datetime.now(), return_date=None)

    def get_borrowed(self):
        return self.borrow_set.filter(
                    due_date__gte=datetime.now(), return_date=None)


class Borrow(BaseContent):
    # information stored when customer is borrowing book
    # due_date is expected date to return book and return date
    # is actuall date given by customer
    customer = models.ForeignKey('Customer')
    book = models.ForeignKey('books.Book')
    borrowed_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(**OPTIONAL)

    def __str__(self):
        return str(self.customer)

    @staticmethod
    def get_due_borrows():
        return Borrow.objects.filter(
        due_date__lte=datetime.now(), return_date=None)

    @staticmethod
    def get_borrowed_books():
        return Borrow.objects.filter(
        due_date__gte=datetime.now(), return_date=None)


