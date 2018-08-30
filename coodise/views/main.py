# -*- coding: utf-8 -*-

from django.http import HttpResponse  # if redirecting after successfull POST
from django.shortcuts import render
from django.views import View
from time import time
from ..utils import parser
from .. import settings
from django.shortcuts import redirect
from ..forms.forms import CreateDirForm
from django.urls import reverse
from django.contrib import messages
import os


class Serve(View):
    """Basic fileserver."""

    def get(self, request, *args, **kwargs):
        filepath = kwargs['file_name']
        user = request.user
        if user.is_anonymous:
            return redirect("/")
        else:
            # return serve(request, os.path.basename(filepath),
            #              os.path.dirname(filepath))
            with open(filepath, "rb") as wish_file:
                response = HttpResponse(
                    wish_file.read(), content_type='application')
            response[
                'Content-Disposition'] = 'attachment; filename="{}"'.format(
                    filepath.split("/")[-1])
            return response


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

        path = kwargs['look_path']
        dir_content = parser.parse_directory(path)
        self.content['have_access_for_writing'] = os.access(
            os.path.join(settings.MEDIA_DIR, path), os.W_OK)
        self.content["create_dir_form"] = CreateDirForm
        self.content['files'] = dir_content[1]
        self.content['user'] = request.user
        self.content['path'] = path
        self.content['path_tail'] = "..." + str(path)[-16:]
        self.content['path_elements'] = generate_elements(str(path))
        self.content['last_path_element'] = self.content['path_elements'][-1][
            1]
        self.content['directories'] = dir_content[0]
        self.content['loadtime'] = "%d" % ((time() - stopwatch) * 1000)
        self.content["current_path"] = path

        if not self.content['have_access_for_writing']:
            messages.warning(request, "Directory is not available for writing")

        return render(request, self.template, self.content)

    def post(self, request, *args, **kwargs):
        new_dir_name = request.POST["dir_name"]
        path = kwargs['look_path']
        current_dir = os.path.join(
            os.path.join(settings.BASE_DIR, settings.MEDIA_DIR), path)
        try:
            os.makedirs(os.path.join(current_dir, new_dir_name))
            messages.success(request,
                             "Directory {} created.".format(new_dir_name))
        except OSError:
            messages.error(
                request,
                "Directory {} not created. Perhaps there is already existing directory or read only filesystem.".
                format(new_dir_name))
        return redirect(reverse("path", args=(path, )))
