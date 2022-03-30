from django.contrib import admin
from django.urls import path

import app.views

urlpatterns = [
    path('', app.views.index, name='index'),
    path('rent', app.views.rent, name='rent'),
    path('register', app.views.register, name='register'),
    #path('post', app.views.post, name='post'),
    path('login', app.views.login, name='login'),
    path('admin/', admin.site.urls),
    path('view/<str:title>', app.views.view, name='view')
]