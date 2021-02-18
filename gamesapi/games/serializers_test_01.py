"""
Book: Building RESTful Python Web Services
"""
from datetime import datetime
from django.utils import timezone
from io import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from games.models import Game
from games.serializers import GameSerializer


gamedatetime = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
game1 = Game(title='Smurfs Jungle', release_date=gamedatetime, category_description='2D mobile arcade', played=False)
game1.save()
game2 = Game(title='Angry Birds RPG', release_date=gamedatetime, category_description='3D RPG', played=False)
game2.save()

print(game1.pk)
print(game1.title)
print(game1.created)
print(game2.pk)
print(game2.title)
print(game2.created)

game_serializer1 = GameSerializer(game1)
print(game_serializer1.data)

game_serializer2 = GameSerializer(game2)
print(game_serializer2.data)

renderer = JSONRenderer()
rendered_game1 = renderer.render(game_serializer1.data)
rendered_game2 = renderer.render(game_serializer2.data)
print(rendered_game1)
print(rendered_game2)

json_string_for_new_game = '{"title":"Tomb Raider Extreme Edition","release_date":"2016-05-18T03:02:00.776594Z","category_description":"3D RPG","played":false}'
json_bytes_for_new_game = bytes(json_string_for_new_game, encoding="UTF-8")
stream_for_new_game = BytesIO(json_bytes_for_new_game)
parser = JSONParser()
parsed_new_game = parser.parse(stream_for_new_game)
print(parsed_new_game)

new_game_serializer = GameSerializer(data=parsed_new_game)
if new_game_serializer.is_valid():
    new_game = new_game_serializer.save()
    print(new_game.title)
