import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from vote.models import *
from .forms import UserForm
from .models import User, Candidate
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import UserForm
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
    
# user 정보
def user_info(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.username = user.id
            user.save()

            is_user = authenticate(request, username=user.username)
            if is_user is not None:
                auth_login(request, is_user)

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

@csrf_exempt
def save_answer(request):
    req = json.loads(request.body)
    quiz_id = req["quizId"]
    example_id = req["exampleId"]
    example = Example.objects.get(id=example_id)
    enrollment = Enrollment.objects.create(num=quiz_id, user=request.user, example=example)
    print(enrollment)
    #todo 현재 로그인 중인 유저의 정보를 가져오기
    # user = User.objects.all()
    return render(request, "vote/user_info.html")