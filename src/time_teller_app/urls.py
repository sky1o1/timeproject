from django.contrib import admin
from django.urls import path
from .views import timestamp,index,today

urlpatterns = [
    path('',index), #specifying path from view
    path('today',today),
    path('timestamp',timestamp)
]


