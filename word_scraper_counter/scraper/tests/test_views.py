"""Scraper views test module."""

import io
import os.path
from unittest import mock

from django.test import TestCase

from word_scraper_counter.scraper.forms import ScraperForm


class TestScraper(TestCase):

    def setUp(self):
        test_page = os.path.join(
            'word_scraper_counter', 'scraper', 'tests',
            'test_data', 'lorem_ipsum.html')
        with open(test_page) as f:
            self.test_page = io.BytesIO(f.read().encode('utf-8'))

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post('/')
        self.assertEqual(resp.status_code, 200)

    def test_form_valid(self):
        form = ScraperForm(data={'url': 'http://www.lorem.ipsum/'})
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = ScraperForm(data={'url': 'http://www/'})
        self.assertFalse(form.is_valid())

    def test_post_field_required(self):
        resp = self.client.post('/')
        self.assertFormError(resp, 'form', 'url', 'This field is required.')

        resp = self.client.post('/', {'url': ''})
        self.assertFormError(resp, 'form', 'url', 'This field is required.')

    @mock.patch('urllib.request.urlopen')
    def test_contains_table(self, mock_urlopen):
        mock_urlopen.return_value = self.test_page

        resp = self.client.post(
            '/', {'url': 'http://www.lorem.ipsum/'}, follow=True)
        mock_urlopen.assert_called_once_with('http://www.lorem.ipsum/')
        self.assertContains(resp, 'Word Frequency')
        self.assertContains(resp, 'Word Type')

    @mock.patch('urllib.request.urlopen')
    def test_contains_chart(self, mock_urlopen):
        mock_urlopen.return_value = self.test_page

        resp = self.client.post(
            '/', {'url': 'http://www.lorem.ipsum/'}, follow=True)
        self.assertIsNotNone(resp.context['chart'])
        self.assertContains(resp, '100 most common words')

    @mock.patch('urllib.request.urlopen')
    def test_words_counter_and_type(self, mock_urlopen):
        mock_urlopen.return_value = self.test_page

        resp = self.client.post(
            '/', {'url': 'http://www.lorem.ipsum/'}, follow=True)
        stats = resp.context['stats']
        words = {word: (count, wtype) for word, count, wtype in stats}
        test_stats = [('the', 47, 'Determiner'), ('there', 6, 'Adverb'),
                      ('will', 5, 'Modal'), ('here', 4, 'Adverb'),
                      ('frequently', 1, 'Adverb')]
        for word, count, wtype in test_stats:
            self.assertEqual(words[word], (count, wtype))

    @mock.patch('matplotlib.pyplot.savefig')
    @mock.patch('urllib.request.urlopen')
    def test_save_chart(self, mock_urlopen, mock_savefig):
        mock_urlopen.return_value = self.test_page

        self.client.post(
            '/', {'url': 'http://www.lorem.ipsum/'}, follow=True)
        mock_savefig.assert_called_once()
