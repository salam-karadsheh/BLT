from django.urls import path 
from . import views 
from . import models

#url config
urlpatterns = [
    path('distance/', views.search_two),
    path('routes/', views.routes),
    path('', views.search_intra_asia), 
    path('test/', views.test)
    ]
