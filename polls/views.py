from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
        return HttpResponse('투표 목록 화면입니다.')
