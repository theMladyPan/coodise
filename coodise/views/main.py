# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect  # if redirecting after successfull POST
from django.shortcuts import render
from django.views import View
from time import time, sleep
from ..utils import parser
from django.views.static import serve
import os
from django.contrib.auth import authenticate
from django.shortcuts import redirect


class Serve(View):
    def get(self, request, *args, **kwargs):
        filepath = kwargs['file_name']
        user = request.user
        if user.is_anonymous:
            return redirect("/")
        else:
            with open(filepath, "rb") as wish_file:
                response = HttpResponse(wish_file.read(), content_type='application')
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(filepath.split("/")[-1])
            return response


class List(View):
    content = dict()
    template = 'main.html'

    def get(self, request, *args, **kwargs):
        stopwatch = time()
        user = request.user
        if user.is_anonymous:
            dir_content = parser.parse_directory(kwargs['look_path'])
            self.content['files'] = []  # dont show files to user
        else:
            dir_content = parser.parse_directory(kwargs['look_path'])
            self.content['files'] = dir_content[1]
        self.content['path'] = kwargs['look_path']
        self.content['directories'] = dir_content[0]
        self.content['loadtime'] = "%d"%((time()-stopwatch)*1000)
        self.content["current_path"] = self.content['path']

        return render(request, self.template, self.content)
