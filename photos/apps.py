from django.apps import AppConfig
import algoliasearch_django as algoliasearch


class PhotosConfig(AppConfig):
    name = 'photos'

    def ready(self):
        # Color = self.get_model('Color')
        # algoliasearch.register(Color)
        Photo = self.get_model('Photo')
        algoliasearch.register(Photo)
