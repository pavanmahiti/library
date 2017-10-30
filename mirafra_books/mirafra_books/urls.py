"""mirafra_books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect
from books.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',dashboard),
    url(r'^borrow-book/$',BorrowBook.as_view()),
    url(r'^list-of-books/$',BookList.as_view()),
    url(r'^list-of-borrow_books/$',BorrowList.as_view()),
    url(r'^return-borrow-book/(?P<qid>.*)/$',return_book_date),
    url(r'.*css/bootstrap-cerulean.min.css$',
        lambda request: HttpResponseRedirect(
            '/static/charisma/css/bootstrap-cerulean.min.css')),
]
