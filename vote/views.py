import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from vote.models import *
from .forms import UserForm, EnrollmentForm
from .models import User, Candidate, Enrollment
from django.views.decorators.csrf import csrf_exempt
import json

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
    

@csrf_exempt
def save_answer(request):
    if request.method == "POST":
        req = json.loads(request.body)
        print(req)
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save()
            # result = Result.objects.create()
            # user.result = result
            # user.save()
            # return render(request, "vote/test.html")
            return redirect("vote:home")
        else:
            ctx = {
                "form": form,
            }
            return render(request, "vote/user_info.html", ctx)
    if request.method == "GET":
        form = EnrollmentForm()
        ctx = {
            "form": form,
        }
        return render(request, "vote/user_info.html", ctx)
    
# user 정보
def user_info(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # result = Result.objects.create()
            # user.result = result
            # user.save()
            # return render(request, "vote/test.html")
            return redirect("vote:home")
        else:
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
