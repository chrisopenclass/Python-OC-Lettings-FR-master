from django.urls import path

from . import views

# definition des différentes url
# this is a testing comment

urlpatterns = [
    path('', views.lettings_index, name='lettings_index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
