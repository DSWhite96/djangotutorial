from django.db import models
"""
Three-step process for changing models in Django:
    1) Change your models in models.py
    2) Run python manage.py makemigrations to create migrations for those changes
    3) Run python magage.py migrate to apply those changes to the database
"""

# Create your models here.
# Models = python representations of db tables
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    #Cascade = changes made to parent tables apply to child tables
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
