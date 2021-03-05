import json

from django.http import HttpResponse
from django.shortcuts import render
from vote.models import *
from .forms import UserForm


def home(request):
    return render(request, 'vote/home.html')


def get_quiz_list(request):
    quizs = Quiz.objects.prefetch_related('examples').all()

    context = {
        "quiz_list": [{
            "id": q.id,
            "question": q.question,
            "examples": [
                {
                    "title": e.title,
                    "is_answer": e.is_answer
                } for e in q.examples.all()]
        } for q in quizs]
    }

    return HttpResponse(json.dumps(context), content_type="application/json")


# user 정보
def user_info(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "vote/test.html")
        else:
            print(request.POST)
            print(form.errors)  # model에서 result 필드가 null 가능해야함
            ctx = {
                "form": form,
            }
            return render(request, "vote/user_info.html", ctx)
    if request.method == "GET":
        form = UserForm()
        ctx = {
            "form": form,
        }
        return render(request, "vote/user_info.html", ctx)
