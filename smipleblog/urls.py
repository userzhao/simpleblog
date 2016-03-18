from django.conf.urls import patterns,url,include
from django.contrib import admin
import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^post/(\d+)/$',views.post_detial),
	url(r'^post/new/$',views.post_new),
	url(r'^post/draft/$',views.post_draft),
	url(r'^post/publish/(\d+)/$',views.post_publish),
	url(r'^post/login/$',views.post_login),
	url(r'^post/register/$',views.post_register),
	
]
