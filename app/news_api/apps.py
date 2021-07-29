from django.apps import AppConfig


class UploadConfig(AppConfig):
    name = "news_api"

    def ready(self):
        print("Starting Scheduler ...")
        from .jobs import start

        start()
