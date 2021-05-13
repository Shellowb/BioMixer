
from django.urls import path

from . import views

app_name = 'grants_applications'
urlpatterns = [
    path(
        '',
        views.HomePage.as_view(),
        name='home',
    ),
    path(
        'library/',
        views.LibraryPage.as_view(),
        name='library',
    ),
    path(
        'mixing/',
        views.MixingPage.as_view(),
        name='mixing',
    ),
    path(
        'preparing/',
        views.PreparingPage.as_view(),
        name='preparing',
    ),
]