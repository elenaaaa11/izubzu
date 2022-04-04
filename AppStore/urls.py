from django.contrib import admin
from django.urls import path

import app.views

urlpatterns = [
    path('', app.views.index, name='index'),
    path('rent', app.views.rent, name='rent'),
    path('area/<str:area_name>', app.views.area, name='area'),
    path('register', app.views.register, name='register'),
    path('post', app.views.post, name='post'),
    path('login', app.views.user_login, name='login'),
    path('admin/', admin.site.urls),
    path('view/<str:title>', app.views.view, name='view'),
    path('rent_1/<str:title>', app.views.rent_1, name='rent_1'),
    path('view/rent_1/<str:title>', app.views.rent_1, name='rent_2')
    path('area/view/<str:title>', app.views.view, name='rent_area')
]
