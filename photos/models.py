from django.db import models
import requests

# Create your models here.

class Photo(models.Model):
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=200, default='no_title')

    def __str__(self):
        return self.title+': '+self.url

def save_photo(url, title):
    p = Photo(url=url, title=title)
    p.save()


def populate():
    api_key = 'a0752bd84a6df8ca859a803cea5edf63'
    api_secret = 'eda5eab58b4c1e2a'
    user_id = '36587311@N08'

    params = {
        'api_key': api_key,
        'method': 'flickr.photos.search',
        'user_id': user_id,
        'format': 'json',
        'nojsoncallback': '1'
    }
    r = requests.get('https://api.flickr.com/services/rest/', params=params)
    photos = r.json()
    photo_list = photos["photos"]["photo"]

    for item in photo_list:
        photo_id = item["id"]
        secret = item["secret"]
        server_id = item["server"]
        farm_id = item["farm"]
        title = item["title"]

        photo_url = 'http://farm' + str(farm_id)\
                    + ".staticflickr.com/" + server_id\
                    + "/" + photo_id + "_" + secret + ".jpg"

        print(photo_url)

        save_photo(photo_url, title)