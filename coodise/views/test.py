from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View


class jQuery(View):
    """Test class for jQuerry."""

    template = 'test.html'
    content = dict()

    def get(self, request, *args, **kwargs):
        return render(request, self.template, self.content)
