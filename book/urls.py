from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage),
    path('protein', views.protein_page),
    path('geiner', views.geiner_page),
    path('creatin', views.creatin_page),
    path('bcaa', views.bcaa_page),
    path('info', views.information_page),
]