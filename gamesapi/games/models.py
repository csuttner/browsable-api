from django.db import models

# Create your models here.
class Game(models.Model):
    # integer identifier automatically added

    # time created
    created = models.DateTimeField(auto_now_add=True)

    # name or title
    title = models.CharField(max_length=200, blank=True, default='')

    # release date
    release_date = models.DateTimeField()

    # category description
    category_description = models.CharField(max_length=200, blank=True, default='')

    # bool value game played y/n
    played = models.BooleanField()

    class Meta:
        ordering = ('title',)
