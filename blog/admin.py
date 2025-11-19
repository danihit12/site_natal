from django.contrib import admin
from .models import Post, Comment  # se você tiver a classe Comment também

admin.site.register(Post)
admin.site.register(Comment)