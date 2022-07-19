import pytest
from django.urls import reverse, resolve
from lettings.models import Address, Letting
from django.test import TestCase


@pytest.mark.django_db
def test_Address_list_url():
    path = reverse('lettings_index')
    assert path == '/lettings/'
    assert resolve(path).view_name == 'lettings_index'


@pytest.mark.django_db
def test_Address_retrive_url():
    address = Address.objects.create(
        number=1,
        street='rues des citrons',
        city='citronville',
        state='ci',
        zip_code='8080',
        country_iso_code='CIT'
    )
    letting = Letting.objects.create(title='citron', address=address)
    path = reverse('letting', kwargs={'letting_id': letting.id})
    assert path == '/lettings/1/'
    assert resolve(path).view_name == 'letting'


def create_address(number, street, city, state, zip_code, country_iso_code):
    """Creating a test address"""
    return Address.objects.create(
        number=number,
        street=street,
        city=city,
        state=state,
        zip_code=zip_code,
        country_iso_code=country_iso_code
    )


def create_letting(title, address):
    """Creating a test letting"""
    return Letting.objects.create(title=title, address=address)


class ViewTests(TestCase):

    def test_index_view(self):
        url = reverse('lettings:lettings_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<title>Lettings</title>", response.content)

    def test_letting_view(self):
        address = create_address(
            number=1,
            street='test street',
            city='test city',
            state='test state',
            zip_code=11111,
            country_iso_code=111
        )
        letting = create_letting(title='test', address=address)
        url = reverse('lettings:letting', args=(letting.id,))
        response = self.client.get(url)
        title = "<title>{}</title>".format(letting.title)
        self.assertEqual(response.status_code, 200)
        self.assertIn(title.encode('utf-8'), response.content)
