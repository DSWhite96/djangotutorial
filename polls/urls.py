#This file is used to map the views to URL configurations (URLconf)
from django.urls import path
from . import views

#This specifies a namespace for this application, which indicates it is separate from other apps that may be added
app_name = "polls"
urlpatterns = [
    #ex: /polls/
    #Outputs list of questions via the .as_view() method
    path("", views.IndexView.as_view(), name="index"),
    #ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    #ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
