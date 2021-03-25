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
from django.http import JsonResponse

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
    enrollment = Enrollment.objects.filter(user=user)
    response_list = []
    for i in enrollment:
        print('i : ' , i)
        response_list.append(i.example)
        
    
    print('user', user)
    print('enrollment', enrollment)
    print('response_list', response_list)
    
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
        
    win_list = [win_cat[0], win_cat[1], win_cat[2],
                win_cat[3], win_cat[4], win_cat[5]]
    
    win_dic = {"win_personal": win_cat[0], "win_real_estate": win_cat[1], "win_economy": win_cat[2],
               "win_welfare": win_cat[3], "win_youngs": win_cat[4], "win_social_value": win_cat[5]}

    return JsonResponse({"user": user, "winner": winner, "win_rate": round(win_rate*100, 1), "win_dic": win_dic, "win_list": win_list})
    # ctx = {
    #     'user': user,
    #     'winner': winner,  # 후보자
    #     'win_rate': round(win_rate*100, 1),  # 예측 종합 일치율
    #     'win_personal': win_cat[0],
    #     'win_real_estate': win_cat[1],
    #     'win_economy': win_cat[2],
    #     'win_welfare': win_cat[3],
    #     'win_youngs': win_cat[4],
    #     'win_social_value': win_cat[5],
    # }
    # return render(request, 'vote/result.html', ctx)


def detail(request):
    user = User.objects.get(id=request.user.id)
    enrollment = Enrollment.objects.all()

    response_list = []
    for i in enrollment:
        response_list.append(i.example)
         
    calculation = calculate(response_list=response_list)
    score_sum = calculation[-1]
    score_percentage = calculation[0]
    if score_sum[0] > score_sum[1]:
        winner = '기호 1번 박영선'
        answer_list = [[1], [3, 4], [2], [1, 3], [1],
                       [2], [1], [2], [2], [1], [2], [1], [0], [2]]
        win_rate = score_sum[0]
        win_cat = score_percentage[0]
    else:
        winner = '기호 2번 오세훈'
        answer_list = [[2], [1, 2, 3, 4], [1], [1, 2], [2],
                       [1], [3], [1], [1], [2], [1], [2], [2], [1]]
        win_rate = score_sum[1]
        win_cat = score_percentage[1]
    ox = []
    for i in range(2, 14):
        if response_list[i] in answer_list[i]:
            ox.append('o')
        else:
            ox.append('x')
    print(ox)
    
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
        'ox3': ox[0],
        'ox4': ox[1],
        'ox5': ox[2],
        'ox6': ox[3],
        'ox7': ox[4],
        'ox8': ox[5],
        'ox9': ox[6],
        'ox10': ox[7],
        'ox11': ox[8],
        'ox12': ox[9],
        'ox13': ox[10],
        'ox14': ox[11],
    }
    return render(request, 'vote/detail.html', ctx)
