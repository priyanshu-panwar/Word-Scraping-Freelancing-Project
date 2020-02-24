"""Scraper urls."""

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', view=views.ScraperFormView.as_view(), name='index'),
]
