from .models import Article, MultimediaContent


class ArticleFactory:
    @staticmethod
    def create_article(article_type, **kwargs):
        if article_type not in dict(Article.ARTICLE_TYPES):
            raise ValueError(f"Invalid article type: {article_type}")
        return Article.objects.create(article_type=article_type, **kwargs)


class MultimediaFactory:
    @staticmethod
    def create_content(content_type, **kwargs):
        if content_type not in dict(MultimediaContent.CONTENT_TYPES):
            raise ValueError(f"Invalid content type: {content_type}")
        return MultimediaContent.objects.create(content_type=content_type, **kwargs)
