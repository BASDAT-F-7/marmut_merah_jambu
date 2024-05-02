from django.urls import path
from Langganan_paket.views import show_serach_bar, show_search

app_name = 'Langganan_paket'

urlpatterns = [
    path('', show_search_bar, name='show_serach_bar'),
    path('', show_search, name= 'show_search'),
]