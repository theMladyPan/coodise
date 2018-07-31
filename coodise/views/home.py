from django.http import HttpResponseRedirect  # if redirecting after successfull POST
from django.shortcuts import render
from django.views import View
from time import time, sleep

class Home(View):
    content = {'path': '/home/odroid',
               'content': 'Hello',
               'loadtime': 'fill_later'}
    template = 'home.html'

    def get(self, request, *args, **kwargs):
        stopwatch = time()
        self.content['path'] = kwargs['look_path']
        data = [str(i) for i in range(10000)]
        self.content['content'] = " ".join(data)
        self.content['loadtime'] = "%d"%((time()-stopwatch)*1000)
        return render(request, self.template, self.content)
