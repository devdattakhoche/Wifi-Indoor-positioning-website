# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [
    ##Template
    re_path(r'^.*\.html', views.pages, name='pages'),
    path('', views.index, name='home'),

    ## Geofencing
    path('geo', views.dashboard, name='dashboard'),
    path('geo/all-user-tracking',views.all_user_tracking,name='all-user-tracking'),
    path('geo/all-user-list',views.all_user_list,name='all-user-list'),
    path('geo/individual-user/<int:id>',views.individual_user,name='individual-user'),
    path('geo/blacklist',views.blacklist,name='blacklist'),
    path('geo/admin-profile',views.admin_profile,name='admin-profile'),
]
