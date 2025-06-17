import datetime

from django.db import models
from django.utils import timezone
"""
Three-step process for changing models in Django:
    1) Change your models in models.py
    2) Run python manage.py makemigrations to create migrations for those changes
    3) Run python magage.py migrate to apply those changes to the database
"""

# Create your models here.
# Models = python representations of db tables
class Question(models.Model):
    def __str__(self):
        """
        Edits what is output when an instance is output to the terminal
        """
        return self.question_text

    def was_published_recently(self):
        """
        Checks whether or not a question was published within the last day

        Parameters:
            None
        Returns:
            bool - Whether or not the question was published in the last day
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    def __str__(self): #Important to add these to models
        return self.choice_text
    #Cascade = changes made to parent tables apply to child tables
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
