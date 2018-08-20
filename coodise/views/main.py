# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect  # if redirecting after successfull POST
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from time import time
from ..utils import parser
from django.views.static import serve
import os
from django.contrib.auth import authenticate


class Serve(View):
    """Basic fileserver."""

    def get(self, request, *args, **kwargs):
        filepath = kwargs['file_name']
        user = request.user
        if user.is_anonymous:
            return redirect("/")
        else:
            return serve(request, os.path.basename(filepath),
                         os.path.dirname(filepath))
            # with open(filepath, "rb") as wish_file:
            #    response = HttpResponse(wish_file.read(), content_type='application')
            # response['Content-Disposition'] = 'attachment; filename="{}"'.format(filepath.split("/")[-1])
            # return response


def generate_elements(path):
    """Accepts string, split it into subdirectories one at a time."""
    # Games/Battlefield 3
    elements = []
    for element in path.split("/"):
        elements.append([path.split(element)[0] + element, element])
    return elements


class List(View):
    """Render list of items for each directory and file in directory."""

    content = dict()
    template = 'main.html'

    def get(self, request, *args, **kwargs):
        stopwatch = time()
        user = request.user
        path = kwargs['look_path']
        dir_content = parser.parse_directory(kwargs['look_path'])
        if user.is_anonymous:
            self.content['files'] = []  # dont show files to user
        else:
            self.content['files'] = dir_content[1]
        self.content['path'] = path
        self.content['path_tail'] = "..." + str(path)[-16:]
        self.content['path_elements'] = generate_elements(str(path))
        self.content['last_path_element'] = self.content['path_elements'][-1][
            1]
        self.content['directories'] = dir_content[0]
        self.content['loadtime'] = "%d" % ((time() - stopwatch) * 1000)
        self.content["current_path"] = path

        return render(request, self.template, self.content)
