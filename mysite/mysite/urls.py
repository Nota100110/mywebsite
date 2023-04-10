"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.conf.urls import include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings

from core import views

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('about/', views.about, name='about'),
    path('coming_soon_page/', views.coming_soon_page, name='coming_soon_page'),
    path('blog/', views.blog, name='blog'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_list/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post_list/<slug:slug>/edit', views.post_edit, name='post_edit'),
    path('post_list/<slug:slug>/new', views.post_new, name='post_new'),
    path('<slug:slug>/comment', views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.add_comment_to_post, name='comment_remove'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$', views.add_comment_to_post, name='comment_approve'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
