from django.http import HttpResponse
from django.views import View

class MainView(View):
    def get(self, request):
        # <view logic>
	name = "Hello!"
	result = name
        return HttpResponse(result)
