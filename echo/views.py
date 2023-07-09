from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello(request):
    """
    hello world 을 출력합니다.
    :param request:
    :return:
    """
    return HttpResponse('hello world')
