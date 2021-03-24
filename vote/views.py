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
from .calculate_util import *


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

            return render(request, "vote/home.html")
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
    enrollment = Enrollment.objects.create(
        num=quiz_id, user=request.user, example=example)
    print(enrollment)
    # todo 현재 로그인 중인 유저의 정보를 가져오기
    # user = User.objects.all()
    return render(request, "vote/user_info.html")


def candidate(request):
    user = User.objects.get(id=request.user.id)
    print(user)
    enrollment = Enrollment.objects.all()
    response_list = []
    print(enrollment)
    for i in enrollment:
        response_list.append(i)
    calculation = calculate(response_list=response_list)
    score_sum = calculation[-1]
    score_percentage = calculation[0]
    if score_sum[0] > score_sum[1]:
        winner = '기호 1번 박영선'
        win_rate = score_sum[0]
        win_cat = score_percentage[0]
    else:
        winner = '기호 2번 오세훈'
        win_rate = score_sum[1]
        win_cat = score_percentage[1]

    ctx = {
        'user': user,
        'winner': winner,  # 후보자
        'win_rate': round(win_rate*100, 1),  # 예측 종합 일치율
        'win_personal': win_cat[0],
        'win_real_estate': win_cat[1],
        'win_economy': win_cat[2],
        'win_welfare': win_cat[3],
        'win_youngs': win_cat[4],
        'win_social_value': win_cat[5],
    }
    return render(request, 'vote/result.html', ctx)
