from django.urls import path
from Langganan_paket.views import show_list_paket, show_pembayaran, show_riwayat

app_name = 'Langganan_paket'

urlpatterns = [
    path('', show_list_paket, name='show_list_paket'),
    path('', show_pembayaran, name= 'show_pembayaran'),
    path('', show_riwayat, name= 'show_riwayat'),
]