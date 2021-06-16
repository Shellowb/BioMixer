
from django.urls import path

from . import views

app_name = 'back_end'
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
    path(
        'connect/',
        views.QRConnect.as_view(),
        name='connect'
    ),
    path(
        'dzone/',
        views.DropZone.as_view(),
        name='dzone'
    ),
    path(
        'file-upload',
        views.DropZone.as_view(),
        name='file_upload'
    ),
    path(
        'dzone_success',
        views.DropZone.success,
        name='dzone_succes'
    ),
    path(
        'api_materiom',
        views.DropZone.success,
        name='api_materiom'
    ),
    path(
        'api_materiom_query',
        views.DropZone.success,
        name='api_materiom_query'
    ),
    path(
        'dzone_success',
        views.DropZone.success,
        name='dzone_succes'
    ),

]
