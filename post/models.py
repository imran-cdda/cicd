from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)

    def length(self):
        return len(self.title)

    def __str__(self):
        return self.title
