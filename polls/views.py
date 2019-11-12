from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('투표 목록 화면입니다.')


def detail_view(request, request_id):
    return HttpResponse('투표 선택 화면입니다.' + str(request_id))


def result_view(request, request_id):
    return HttpResponse('투표 결과 화면입니다.' + str(request_id))
