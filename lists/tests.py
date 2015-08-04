from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.
class SmokeTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_starts_with_html_tag(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))

    def test_home_contains_correct_title(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn(b'<title>To-Do lists</title>', response.content)

    def test_home_ends_with_html_tag(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.endswith(b'</html>'))

