"""Scraper urls test module."""

from django.core.urlresolvers import resolve, reverse
from django.test import TestCase


class TestScraperURLs(TestCase):
    """Test URL patterns for scraper app."""

    def test_index_reverse(self):
        self.assertEqual(reverse('scraper:index'), '/')

    def test_index_resolve(self):
        self.assertEqual(resolve('/').view_name, 'scraper:index')
