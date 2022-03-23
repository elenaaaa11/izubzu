from django.contrib import admin
from django.urls import path

import app.views

urlpatterns = [
    path('', app.views.index, name='index'),
    path('rent', app.views.rent, name='rent'),
    path('register', app.views.register, name='register'),
    #path('post', app.views.register, name='post'),
    #path('sign_in', app.views.sign_in, name='sign_in'),
    path('admin/', admin.site.urls)
]