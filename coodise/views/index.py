# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect  # if redirecting after successfull POST
from django.shortcuts import render
from django.views import View
from ..utils import parser

class Index(View):
    content = {'webpage_title': "Coodise index",
               'path': ""}
    template = 'main.html'

    def get(self, request, *args, **kwargs):
        dir_content = parser.parse_directory(self.content['path'])
        self.content['directories'] = dir_content[0]
        self.content['files'] = dir_content[1]
        self.content["current_path"] = self.content['path']
        return render(request, self.template, self.content)
