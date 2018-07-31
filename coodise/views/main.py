from django.http import HttpResponseRedirect  # if redirecting after successfull POST
from django.shortcuts import render
from django.views import View
from time import time, sleep
from ..utils import parser

class Main(View):
    content = {'path': '/home/odroid',
               'content': 'Hello',
               'loadtime': 'fill_later'}
    template = 'main.html'

    def get(self, request, *args, **kwargs):
        stopwatch = time()
        dir_content = parser.parse_directory(self.content['path'])
        self.content['directories'] = dir_content[0]
        self.content['files'] = dir_content[1]
        self.content['loadtime'] = "%d"%((time()-stopwatch)*1000)
        return render(request, self.template, self.content)
