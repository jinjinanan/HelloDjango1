from rest_framework import serializers
from .models import HomeMenu

class HomeMenuSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HomeMenu
        fields = ('title',)
