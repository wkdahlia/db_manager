from django.conf.urls import url, include
from django.contrib import admin
from myweb import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^index/', views.index),
    url(r'^parts/', views.parts),
    url(r'^parts_add/', views.parts_add),
    url(r'^part_del/', views.part_del),
    url(r'^part_edit/', views.part_edit),
    url(r'^hosts/', views.hosts),
    url(r'^hosts_del/', views.hosts_del),
    url(r'^hosts_edit/', views.hosts_edit),
    url(r'^hosts_add/', views.hosts_add),
    url(r'^users/', views.users_list),
    url(r'^users_add/', views.users_add),
    url(r'^user_del/', views.users_del),
    url(r'^user_edit/', views.users_edit),
]
