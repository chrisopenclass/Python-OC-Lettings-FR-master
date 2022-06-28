import pytest

from django.urls import reverse, resolve
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_Address_list_url():
    path = reverse('profile_index')

    assert path == '/profiles/'
    assert resolve(path).view_name == 'profiles_index'


@pytest.mark.django_db
def test_profile_retrieve_url():
    user = User.objects.create(username='test', password='securedpassword')

    profile = Profile.objects.create(user=user, favorite_city='citronville')

    path = reverse('profile', kwargs={'username': profile.user.username})

    assert path == '/profiles/test/'
    assert resolve(path).view_name == 'profile'
