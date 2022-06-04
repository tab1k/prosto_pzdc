from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('market', views.market, name = 'market'),
    path('stock', views.stock, name = 'stock'),
    path('help', views.help, name = 'help')
]