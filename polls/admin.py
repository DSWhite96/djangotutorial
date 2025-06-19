from django.contrib import admin
#You need to import your models in order for them to be viewable by the admin
from .models import Choice, Question

# Register your models here.
#InLine classes allow you to add additional models directly into the form for a different model (best for foreignkey relationships)
class ChoiceInLine(admin.TabularInline):
    model = Choice
    #This specifies how many fields are added by default (they don't need to all be used)
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #The fields appear in the order specified by the <fields> or <fieldsets> lists
    #Ex: fields = ["pub_date", "question_text"]
    fieldsets = [
        #The first value in the tuple indicates the field set's title, the second value is a dict with the actual fields
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]})
    ]
    #Use this to indicate which models you are adding to your <Question> form
    inlines = [ChoiceInLine]
    #This specifies what information about the model is displayed in the admin page
    list_display = ["question_text", "pub_date", "was_published_recently"]
    #Use pub_date as a filter in the admin page
    list_filter = ["pub_date"]
    #Adds a search box and specifies what can be searched within the questions
    search_fields = ["question_text"]

#Need to register your models for them to appear in the admin form
admin.site.register(Question, QuestionAdmin)
