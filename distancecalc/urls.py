from django.urls import path 
from . import views 
from . import models

#url config
urlpatterns = [
    path('routes/', views.routes),
    path('asia/', views.search_intra_asia), 
    path('', views.search_global)
    ]
