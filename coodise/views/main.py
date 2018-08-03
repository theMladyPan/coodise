from django.http import HttpResponse, HttpResponseRedirect  # if redirecting after successfull POST
from django.shortcuts import render
from django.views import View
from time import time, sleep
from ..utils import parser
from django.views.static import serve
import os


class Serve(View):
    def get(self, request, *args, **kwargs):
        filepath = kwargs['file_name']
        with open(filepath, "rb") as wish_file:
            response = HttpResponse(wish_file.read(), content_type='application')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filepath.split("/")[-1])
        return response


class List(View):
    content = dict()
    template = 'main.html'

    def get(self, request, *args, **kwargs):
        stopwatch = time()
        dir_content = parser.parse_directory(kwargs['look_path'])
        self.content['path'] = kwargs['look_path']
        self.content['directories'] = dir_content[0]
        self.content['files'] = dir_content[1]
        self.content['loadtime'] = "%d"%((time()-stopwatch)*1000)
        return render(request, self.template, self.content)
