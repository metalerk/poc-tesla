from django.conf.urls import url, include
from .views import SP

urlpatterns = [
    url(r'^$', SP.as_view()),
]
