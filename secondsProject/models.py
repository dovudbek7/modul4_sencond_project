from django.db import models


class Article(models.Model):
    ARTICLE_TYPES = [
        ('general', 'General Article'),
        ('technical', 'Technical Article'),
        ('news', 'News Article'),
    ]
    title = models.CharField(max_length=255)
    content = models.TextField()
    article_type = models.CharField(max_length=20, choices=ARTICLE_TYPES)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class MultimediaContent(models.Model):
    CONTENT_TYPES = [
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('image', 'Image'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    file_url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.content[:30]
