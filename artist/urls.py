from django.urls import path
from .views import ArtistWizard

urlpatterns = [
    path('register/artist/', ArtistWizard.as_view(FORMS), name='artist_registration'),
]
