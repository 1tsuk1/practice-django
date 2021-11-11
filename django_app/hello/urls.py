from django.contrib import admin
from django.urls import path

import hello.views as hello

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('hello/', hello.index),
# ]
