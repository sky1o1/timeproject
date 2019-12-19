from django.contrib import admin
from django.urls import path
import timestamp

urlpatterns = [
    path('',index), #specifying path from view
    path('today',today),
    path('timestamp',timestamp)
]


