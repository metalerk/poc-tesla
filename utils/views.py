from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated


class OpenView(APIView):
    permission_classes = (AllowAny,)


class PrivateView(APIView):
    permission_classes = (IsAuthenticated,)
