from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('search/', search, name="search"),
    path('search/<int:player_id>/', search_results, name='search_results'),
]