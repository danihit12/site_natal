from django.db import models
from django.utils import timezone







class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # HTML
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(blank=True, null=True)  # hospedada fora

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"Comentário de {self.author}"

# Create your models here.
