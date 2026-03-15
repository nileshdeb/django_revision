from django.db import models

class YouTubeUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subscribers=models.PositiveBigIntegerField(default=0)
    

    def __str__(self):
        return self.name