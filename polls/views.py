#View = function or class that takes a web request and returns a web response
#Basically a type of web page that serves a specific function
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# Create your views here.
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    #If we didn't specify this, it would automatically call it question_list instead of latest_questions_list
    context_object_name = "latest_questions_list"
    #Returns the set of questions to the as_view() method call in urls.py
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    #Details are provided automatically because django knows what a DetailView is and knows what model it's operating on (Question in this case)
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay question voting form
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice."
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        #ALWAYS return a redirect after successfully dealing with POST data, this prevents data from being posted twice
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
