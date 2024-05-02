from django.urls import path
from downloaded_songs.views import download_list
app_name = 'downloaded_songs'

urlpatterns = [
    path('', download_list, name='download_list'),
]