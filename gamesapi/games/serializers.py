"""
Book: Building RESTful Python Web Services
"""
from rest_framework import serializers
from games.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 
                  'title', 
                  'release_date',
                  'category_description', 
                  'played')