from rest_framework import viewsets
from .models import HomeMenu
from .serializes import HomeMenuSerialize

class HomeMenuViewSet(viewsets.ModelViewSet):
    queryset = HomeMenu.objects.all()
    serializer_class = HomeMenuSerialize