from django.shortcuts import render, HttpResponse
from .models import Question, Choice
# Create your views here.


def index(req):
    question_list = Question.objects.all()
    return render(req, 'index/index.html', {"question_list": question_list})


def detail(req, question_id):
    return HttpResponse('detail')


def results(req, question_id):
    return HttpResponse('results')


def vote(req, question_id):
    return HttpResponse('vote')

