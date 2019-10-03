"""book2 URL Configuration

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
from app01 import views
from app01 import views2


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # url(r'^publish_list/', views.publish_list, name='publish_list'),
    # url(r'^publish_add/', views.publish_add, name='publish_add'),
    # url(r'^publish_edit/(\d+)', views.publish_edit, name='publish_edit'),
    # url(r'^publish_del/(\d+)', views.publish_del, name='publish_list'),
    #
    # url(r'^book_list/', views.book_list, name='book_list'),
    # url(r'^book_add/', views.book_add, name='book_add'),
    # url(r'^book_edit/(\d+)', views.book_edit, name='book_edit'),
    # url(r'^book_del/(\d+)', views.book_del, name='book_list'),
    #
    # url(r'^author_list/', views.author_list, name='author_list'),
    # url(r'^author_add/', views.author_add, name='author_add'),
    # url(r'^author_edit/(\d+)', views.author_edit, name='author_edit'),
    # url(r'^author_del/(\d+)', views.author_del, name='author_list'),




    # views2

    url(r'^publish_list/', views2.publish_list, name='publish_list'),
    url(r'^publish_add/', views2.publish_add, name='publish_add'),
    url(r'^publish_edit/(\d+)', views2.publish_edit, name='publish_edit'),
    url(r'^publish_del/(\d+)', views2.publish_del, name='publish_list'),

    url(r'^book_list/', views2.book_list, name='book_list'),
    url(r'^book_add/', views2.book_add, name='book_add'),
    url(r'^book_edit/(\d+)', views2.book_edit, name='book_edit'),
    url(r'^book_del/(\d+)', views2.book_del, name='book_list'),

    url(r'^author_list/', views2.author_list, name='author_list'),
    url(r'^author_add/', views2.author_add, name='author_add'),
    url(r'^author_edit/(\d+)', views2.author_edit, name='author_edit'),
    url(r'^author_del/(\d+)', views2.author_del, name='author_list'),
]
