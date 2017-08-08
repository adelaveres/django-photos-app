from django.db import models
import requests
import xml.etree.ElementTree as xmlET
from django.contrib.auth.models import AbstractBaseUser, UserManager


# Create your models here.

api_key = 'a0752bd84a6df8ca859a803cea5edf63'
api_secret = 'eda5eab58b4c1e2a'
accepted_colors = ['red', 'green', 'blue', 'yellow', 'orange', 'brown', 'black', 'white', 'gray', 'purple', 'pink']


# class User(models.Model):
#     username = models.CharField(max_length=30, default='no_username')
#     email = models.CharField(max_length=30, default='no_email')
#     password = models.CharField(max_length=30, default='no_password')
#     is_authenticated = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#
#     objects = UserManager()

class Photo(models.Model):
    photo_id = models.CharField(max_length=20, default='')
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=200, default='no_title')
    color1 = models.CharField(max_length=20, default='')
    color2 = models.CharField(max_length=20, default='')
    color3 = models.CharField(max_length=20, default='')

    @property
    def colors(self):
        result = []
        if self.color1:
            result.append(self.color1)
        if self.color2:
            result.append(self.color2)
        if self.color3:
            result.append(self.color3)
        return result

# class Color(models.Model):
#     color = models.CharField(max_length=20)
#     photos = models.ManyToManyField(Photo, related_name="color", related_query_name="color")


# def save_photo(photo_id, url, title, colors):
#     p = Photo(photo_id=photo_id, url=url, title=title)
#     p.save()
#     for color in colors:
#         c = Color(color=color)
#         c.save()
#         p.color.add(c)
#     p.save()


def save_photo(photo_id, url, title, colors):
    l = len(colors)

    # def color_at_index(index):
    #     try:
    #         return colors[index]
    #     except IndexError:
    #         return None

    # REFACTORED:
    # p = Photo(
    #     photo_id=photo_id,
    #     color1=color_at_index(0),
    #     color2=color_at_index(1),
    #     color3=color_at_index(2),
    #     url=url,
    #     title=title
    # )
    # p.save()

    if l == 1:
        color1 = colors[0]
        p = Photo(photo_id=photo_id, url=url, title=title, color1=color1)
        p.save()
    else:
        if l == 2:
            color1 = colors[0]
            color2 = colors[1]
            p = Photo(photo_id=photo_id, url=url, title=title, color1=color1, color2=color2)
            p.save()
        else:
            if l == 3:
                color1 = colors[0]
                color2 = colors[1]
                color3 = colors[2]
                p = Photo(photo_id=photo_id, url=url, title=title, color1=color1, color2=color2, color3=color3)
                p.save()
            else:
                p = Photo(photo_id=photo_id, url=url, title=title)
                p.save()


def get_photos(params):
    r = requests.get('https://api.flickr.com/services/rest/', params=params)
    photos = r.json()
    photo_list = photos["photos"]["photo"]
    return photo_list


def get_photos_by_user():
    params = {
        'api_key': api_key,
        'method': 'flickr.photos.search',
        'user_id': '36587311@N08',
        'format': 'json',
        'nojsoncallback': '1'
    }
    return get_photos(params)


def get_photos_by_tag():
    params = {
        'api_key': api_key,
        'method': 'flickr.photos.search',
        'format': 'json',
        'nojsoncallback': '1',
        'tags': 'abstract'
    }
    return get_photos(params)


def get_colors(url):
    params = {
        'url': url,
        'precision': 'medium',
        'xml': 1
    }
    r = requests.get('http://mkweb.bcgsc.ca/color-summarizer/', params=params)
    root = xmlET.fromstring(r.content)
    color_tags = root[0][0][9].text
    colors_list = color_tags.split(':')

    max_el = 3
    final_list = []
    for color in colors_list:
        for accepted_color in accepted_colors:
            if color == accepted_color:
                if max_el > 0:
                    final_list.append(color)
                    max_el -= 1

    return final_list


def loop_save_photos(photos_list):

    for item in photos_list:
        photo_id = item["id"]
        secret = item["secret"]
        server_id = item["server"]
        farm_id = item["farm"]
        title = item["title"]

        photo_url = 'http://farm' + str(farm_id)\
                    + ".staticflickr.com/" + server_id\
                    + "/" + photo_id + "_" + secret + ".jpg"

        print(photo_url)
        colors = get_colors(photo_url)
        save_photo(photo_id, photo_url, title, colors)


def populate():
    photos_list = get_photos_by_user()
    loop_save_photos(photos_list)
    photos_list = get_photos_by_tag()
    loop_save_photos(photos_list)



