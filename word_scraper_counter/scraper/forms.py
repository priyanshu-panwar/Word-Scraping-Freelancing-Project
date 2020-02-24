"""Scraper forms module."""

from django import forms
from django.utils.translation import ugettext_lazy as _


class ScraperForm(forms.Form):
    """Scraper form.

    Takes a query (URL) and validate it.
    """

    # @TODO: Implement it
