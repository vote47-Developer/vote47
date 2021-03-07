from django.shortcuts import render
from django.http import JsonResponse
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


def test(request):
    i = 1
    ctx = {
        'i': i
    }
    return render(request, 'vote/ajax-test.html', ctx)


@ method_decorator(csrf_exempt)
def test_plus(request):
    if request.method == 'GET':
        return render(request, 'vote/ajax-test.html')
    elif request.method == 'POST':
        req = json.loads(request.body)
        print(req)
        print(req)
        print(req)
        print(req)
        print(req)
        num = req['numdiv']
        return JsonResponse({'num': num})
