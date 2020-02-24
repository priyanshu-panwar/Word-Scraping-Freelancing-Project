from django.apps import AppConfig


class ScraperConfig(AppConfig):
    name = 'word_scraper_counter.scraper'
    verbose_name = 'Scraper'

    def ready(self):
        pass
