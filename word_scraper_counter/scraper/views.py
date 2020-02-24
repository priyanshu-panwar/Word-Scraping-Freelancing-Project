"""Scraper views."""

from django.views.generic import FormView


class ScraperFormView(FormView):
    """Scraper form view.

    Takes a query (URL), scrapes the URL, and extracts
    the complete vocabulary of the document.
    """

    # @TODO: Implement it
