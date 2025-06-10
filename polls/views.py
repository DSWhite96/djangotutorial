#View = function or class that takes a web request and returns a web response
#Basically a type of web page that serves a specific function
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
