from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question,Choice
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect

def index(request):        
    latest_question_list = Question.objects.order_by('pub_date')
    context = {"latest_question":latest_question_list}
    template = loader.get_template("mangalib/index.html")
    return HttpResponse(template.render(context,request,),)

def detail(request,question_id):
 return render(request,'mangalib/details.html',{
     'question_id':question_id
 })

def vote(request,question_id):
 question = get_object_or_404(Question, pk=question_id)
 try:
   selected_choice  = question.choice_set.get(pk=request.POST["choice"])
 except(KeyError,Choice.DoesNotExist):
    #  if user didn't select any choice 
   return render(request,'mangalib/details.html',{
        "question": question,
        "error_message": "You didn't select a choice.",
        
   })
 else:
   selected_choice.votes = F("votes") + 1
   selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
   return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
