#View = function or class that takes a web request and returns a web response
#Basically a type of web page that serves a specific function
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #Pass in variables as context for the template
    context = {"latest_question_list": latest_question_list}
    #Render the template and send it in the HTTP response
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    #Searches for an object, returns 404 if it doesn't exist
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
