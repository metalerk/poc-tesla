from django.urls import re_path
from .views import (
    CreateMFAL,
    CreateSerie,
    CreatePackage,
    RetrieveMFAL,
    RetrieveSerie,
    RetrievePackage,
)

urlpatterns = [
    re_path(r'^create/mfal/', CreateMFAL.as_view()),
    re_path(r'^create/serie/', CreateSerie.as_view()),
    re_path(r'^create/package/', CreatePackage.as_view()),
    re_path(r'^retrieve/mfal/', RetrieveMFAL.as_view()),
    re_path(r'^retrieve/serie/', RetrieveSerie.as_view()),
    re_path(r'^retrieve/package/', RetrievePackage.as_view()),
]
