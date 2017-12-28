from django.conf.urls import url, include
from .views import Home

urlpatterns = [
    url(r'^$', Home.as_view()),
    url(r'sp', include('sp.urls'))
]