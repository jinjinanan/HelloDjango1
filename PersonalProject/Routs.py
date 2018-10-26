from rest_framework import routers
from .ViewSets import HomeMenuViewSet

router = routers.DefaultRouter()
router.register(r'HomeMenu',HomeMenuViewSet)