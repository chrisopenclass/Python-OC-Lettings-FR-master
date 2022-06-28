import pytest

from django.urls import reverse, resolve
from lettings.models import Address, Letting


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
