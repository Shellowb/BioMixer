import logging
import os.path
from  biomixer_interface.settings import STATIC_PATH
from biomixer_interface.net_functions.ip import IP
from django.views import View
from django.shortcuts import render, redirect
import socket
import qrcode
from django.http import HttpResponse
from .models import Doc
import PIL


class HomePage(View):
    """
        Home page view
        manages the request for the home page
    """

    def get(self, request):
        """

        :param request:
        :return:
        """
        return render(request, 'home.html', context={})

    def post(self, request):
        """

        :param request:
        :return:
        """
        pass


class LibraryPage(View):
    """
        Home page view
        manages the request for the home page
    """

    def get(self, request):
        """

        :param request:
        :return:
        """
        return render(request, 'library.html', context={})

    def post(self, request):
        """

        :param request:
        :return:
        """
        pass


class MixingPage(View):
    """
        Home page view
        manages the request for the home page
    """

    def get(self, request):
        """

        :param request:
        :return:
        """
        return render(request, 'mixing.html', context={})

    def post(self, request):
        """

        :param request:
        :return:
        """
        pass


class PreparingPage(View):
    """
        Home page view
        manages the request for the home page
    """

    def get(self, request):
        """

        :param request:
        :return:
        """
        return render(request, 'preparing.html', context={})

    def post(self, request):
        """

        :param request:
        :return:
        """
        pass


class QRConnect(View):
    already_visited = True

    def get(self, request):
        if self.already_visited:
            path = os.path.join(STATIC_PATH, 'img')
            print(path)
            host = IP.get_ip()
            ip = socket.gethostbyname(host)
            ip = 'http://' + ip + ':8000'
            img = qrcode.make(ip)
            img.save(path + '/qrip.png', )
            print(img)

        return render(request, 'qrip.html')


class DropZone(View):
    def get(self, request):
        return render(request, 'dzone.html')

    def post(self, request):
        my_file = request.FILES.get('file')
        Doc.objects.create(upload=my_file)
        return HttpResponse('upload')

    @staticmethod
    def success(request):
        return render(request, 'dzone_success.html')

