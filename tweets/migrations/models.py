from django.db import models

#Create your models here.

class Tweet(models.Model):
    creator =models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    location = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def__str__(self):
        return f"{self.creator.username}" - {self.construct}