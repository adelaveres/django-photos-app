from django.apps import AppConfig
import algoliasearch_django as algoliasearch
from algoliasearch_django import AlgoliaIndex


class PhotoIndex(AlgoliaIndex):
    fields = ('url', 'photo_id', 'title', 'colors')


class PhotosConfig(AppConfig):
    name = 'photos'

    def ready(self):
        # Color = self.get_model('Color')
        # algoliasearch.register(Color)
        Photo = self.get_model('Photo')
        algoliasearch.register(Photo, PhotoIndex)
