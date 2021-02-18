from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import home, send_order_enquiry, authors


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEqual(resolve(url).func, home)

    def test_send_order_enquiry_url_is_resolved(self):
        url = reverse('contact')
        print(resolve(url))
        self.assertEqual(resolve(url).func, send_order_enquiry)

    def test_authors_is_resolved(self):
        url = reverse('authors')
        print(resolve(url))
        self.assertEqual(resolve(url).func, authors)
