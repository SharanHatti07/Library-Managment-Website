from django.urls import path
from libapp import views

urlpatterns = [
    path('', views.index),
    path('v',views.view),
    path('delete/<rid>',views.delete),
]