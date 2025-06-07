#View = function or class that takes a web request and returns a web response
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world. You're at the polls index.")