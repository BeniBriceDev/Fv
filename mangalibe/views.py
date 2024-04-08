from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):        
    latest_question_list = Question.objects.order_by('pub_date')
    context = {"latest_question":latest_question_list}
    template = loader.get_template("mangalib/index.html")
    return HttpResponse(template.render(context,request,),)

def detail(request,question_id):
 return HttpResponse("You're looking at question %s." % question_id)
