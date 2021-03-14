import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from vote.models import *
from .forms import UserForm
from .models import User, Candidate
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
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
    if request.method == "POST":
        #todo JS 통신방법 ajax 밖에 없나? 프론트에서 보여줄 필요 없는데도? 
        req = json.loads(request.body)
        print(req)
        #todo 현재 로그인 중인 유저의 정보를 가져오기
        user = User.objects.all()
        print(user)
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