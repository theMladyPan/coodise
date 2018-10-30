# -*- coding: utf-8 -*-

from django.http import HttpResponse  # if redirecting after successfull POST
from django.shortcuts import render
from django.views import View
from time import time
from ..utils import parser
from .. import settings
from django.shortcuts import redirect
from ..forms.forms import CreateDirForm, CreateFileForm, UploadFileForm, RenameForm
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
    error = '404.html'

    def get(self, request, *args, **kwargs):
        stopwatch = time()

        dForms = {
            "create_dir_form": CreateDirForm,
            "create_file_form": CreateFileForm,
            "upload_file_form": UploadFileForm,
            "rename_form": RenameForm,
        }
        for form in dForms.keys():
            self.content[form] = dForms.get(form)

        path = kwargs['look_path']
        self.content['path'] = path
        self.content["media_dir"] = settings.MEDIA_DIR
        if not os.path.isdir(os.path.join(settings.MEDIA_DIR, path)):
            return render(request, self.error, self.content)

        dir_content = parser.parse_directory(path)
        self.content['directories'] = dir_content[0]
        self.content['files'] = dir_content[1]

        self.content['have_access_for_writing'] = os.access(
            os.path.join(settings.MEDIA_DIR, path), os.W_OK)
        self.content['user'] = request.user
        self.content['path_tail'] = "..." + str(path)[-16:]
        if path:
            self.content['path_elements'] = generate_elements(str(path))
            self.content['last_path_element'] = self.content['path_elements'][
                -1][1]
        else:
            self.content["path_elements"] = ""
            self.content["last_path_element"] = ""

        self.content['loadtime'] = "%d" % ((time() - stopwatch) * 1000)
        self.content["current_path"] = path

        if not self.content['have_access_for_writing']:
            messages.warning(request, "Directory is not available for writing")

        return render(request, self.template, self.content)

    def post(self, request, *args, **kwargs):
        dActions = {
            "create_dir": self.create_dir,
            "create_file": self.create_file,
            "upload_file": self.upload_file,
            "rename_file": self.rename_file,
        }
        return dActions.get(request.POST.get("tool"))(request, kwargs)

    def rename_file(self, request, kwargs):
        new_name = request.POST.get("new_name")
        path = kwargs['look_path']
        full_old_name = os.path.join(settings.MEDIA_DIR, path,
                                     request.POST.get("old_name").lstrip("/"))
        directory = ("/".join(full_old_name.split("/")[:-1])).lstrip("/")
        full_new_name = os.path.join(directory, new_name)

        print(
            f"path {path} new_name {new_name} fulloldname {full_old_name} director {directory} fullnewname {full_new_name}"
        )
        if os.path.isfile(full_new_name) or os.path.isdir(full_new_name):
            messages.warning(
                request,
                f"File or directory with name '{new_name}' already exists")
        else:
            os.rename(full_old_name, full_new_name)
            messages.success(request, f"File '{new_name}' renamed.")

        return redirect(reverse("path", args=(path, )))

    def create_file(self, request, kwargs):
        path = kwargs['look_path']
        file_name = request.POST.get("file_name")
        full_path = os.path.join(
            os.path.join(settings.MEDIA_DIR, path), file_name)
        if os.path.isfile(full_path):
            messages.warning(
                request,
                f"File or directory with name '{file_name}' already exists")
        else:
            open(full_path, 'a').close()
            messages.success(request, f"File '{file_name}' created.")

        return redirect(reverse("path", args=(path, )))

    def upload_file(self, request, kwargs):
        path = kwargs['look_path']
        file_name = request.POST.get("file_name")
        if not file_name:
            file_name = str(request.FILES["file"])
        full_path = os.path.join(
            os.path.join(settings.MEDIA_DIR, path), file_name)

        if os.path.isfile(full_path):
            messages.warning(
                request,
                f"File or directory with name '{file_name}' already exists")
        else:
            with open(full_path, "wb") as out_file:
                out_file.write(request.FILES["file"].read())
            messages.success(request, f"File '{file_name}' uploaded.")

        return redirect(reverse("path", args=(path, )))

    def create_dir(self, request, kwargs):
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
