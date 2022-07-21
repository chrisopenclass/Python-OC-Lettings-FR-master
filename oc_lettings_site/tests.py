import pytest
from django.urls import reverse, resolve
from django.test import TestCase


@pytest.mark.django_db
def test_home_page_url():
    path = reverse('index')

    assert path == '/'
    assert resolve(path).view_name == 'index'


class ViewTests(TestCase):

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<title>Holiday Homes</title>", response.content)
