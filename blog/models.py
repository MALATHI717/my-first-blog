# import json
# from django.db import models

# # Create a simple Post model class without database interaction
# class Post:
#     def __init__(self, author, title, content):
#         self.author = author
#         self.title = title
#         self.content = content

#     def to_dict(self):
#         # Return a dictionary representation of the Post object
#         return {
#             'author':1, #self.author,
#             'title': self.title,
#             'content': self.content,
#         }

#     @staticmethod
#     def save_to_file(posts, filename='posts.json'):
#         # Save the posts to a JSON file
#         with open(filename, 'w') as f:
#             json.dump([post.to_dict() for post in posts], f)

#     @staticmethod
#     def load_from_file(filename='posts.json'):
#         # Load posts from a JSON file
#         try:
#             with open(filename, 'r') as f:
#                 data = json.load(f)
#                 return [Post(**item) for item in data]
#         except FileNotFoundError:
#             return []

from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title