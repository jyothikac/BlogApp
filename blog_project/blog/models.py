from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#class based models
class Post(models.Model):                           #post method will save the each post to database
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #if useraccount is deleted then all posts  gets deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # this will route the blog post creation page to the page where blog is posted
        return reverse('post-detail', kwargs={'pk': self.pk})
