class AppConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AppConfig, cls).__new__(cls, *args, **kwargs)
            cls._instance.articles_per_page = 10
            cls._instance.allowed_file_types = ['jpg', 'png', 'mp4', 'mp3']
            cls._instance.max_file_size = 10485760  # 10 MB
        return cls._instance