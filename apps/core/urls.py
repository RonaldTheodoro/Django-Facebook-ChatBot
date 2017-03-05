from django.conf.urls import url
from .views import SpotifyBotView

urlpatterns = [
    url(r'^$', SpotifyBotView.as_view(), name='spotify'),
]
