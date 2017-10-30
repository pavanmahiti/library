# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import CreateView,ListView
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta
from books.models import *
from customer.models import *




def dashboard(request):
    categorys = [i for i in Category.objects.all() if i.get_no_of_stockout()]
    total_out_of_stock  = len([i for i in Book.objects.all()
                               if not i.has_stock()])
    due_users = [i for i in Customer.objects.all() if i.get_dues() ]
    user_due_books = Borrow.get_due_borrows().count()
    borrowed_users = [i for i in Customer.objects.all() if i.get_borrowed() ]
    borrowed_users_books = Borrow.get_borrowed_books().count()
    from_date = datetime.now() - timedelta(days=7)
    new_customers = Customer.objects.filter(created__range=[from_date, datetime.now()])
    return render(request,'dashboard.html',locals())


class Manage(object):

    model = Borrow
    fields = ['customer', 'book', 'borrowed_date', 'due_date']
    success_url = '/'
    template_name = 'borrow-book.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Manage, self).form_valid(form)


class BorrowBook(Manage,  CreateView):
    success_url = "/list-of-borrow_books/"


class BorrowList(Manage,ListView):
    template_name = 'borrow-book-listing.html'
    def get_queryset(self):
        qs = super(Manage, self).get_queryset()
        return qs.filter(return_date=None)


class BookList(Manage, ListView):
    model = Book
    template_name = 'book-listing.html'

def return_book_date(request,qid=None):
    bo_obj = Borrow.objects.get(id=qid)
    bo_obj.return_date = datetime.now()
    bo_obj.save()
    return HttpResponseRedirect('/list-of-borrow_books/')
