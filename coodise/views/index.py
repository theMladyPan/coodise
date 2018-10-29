# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect  # if redirecting after successfull POST
from django.shortcuts import render
from django.views import View
from ..utils import parser
import os
from .. import settings
from ..forms.forms import CreateDirForm, CreateFileForm, UploadFileForm


class Index(View):
    """Index page view."""

    content = {'webpage_title': "Coodise index", 'path': ""}
    template = 'main.html'

    def get(self, request, *args, **kwargs):
        dir_content = parser.parse_directory(self.content['path'])
        self.content['directories'] = dir_content[0]
        self.content['files'] = dir_content[1]
        self.content["current_path"] = self.content['path']
        self.content['have_access_for_writing'] = os.access(
            str(settings.MEDIA_DIR), os.W_OK)
        dForms = {
            "create_dir_form": CreateDirForm,
            "create_file_form": CreateFileForm,
            "upload_file_form": UploadFileForm,
        }
        for form in dForms.keys():
            self.content[form] = dForms.get(form)
        return render(request, self.template, self.content)
