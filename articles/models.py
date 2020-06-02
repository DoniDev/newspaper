from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse






class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('article-detail', args=[self.id])


    def get_update_url(self):
        return reverse('article-update', args=[self.id])

    def get_delete_url(self):
        return reverse('article-delete', args=[self.id])



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.body[:10]


    def get_absolute_url(self):
        return reverse('article-list')