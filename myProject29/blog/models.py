from django.db import models

class UserProfile(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    sub=models.IntegerField(default=0)

    def __str__(self):
        return self.name