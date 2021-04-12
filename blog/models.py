from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) #this auth_user_model will point to the user model which is currently acitve i.e either User model which is defined by You or by django
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title