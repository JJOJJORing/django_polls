from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
# Create your views here.


def index(request):
    output = ''
    for question in Question.objects.order_by('-pub_date'):
        output += '<a href="/polls/detail/' + str(question.id) + '">' + question.question_text + '</a><br>'

    return HttpResponse(output)


def detail_view(request, request_id):
    # 페이지나 데이터가 있을때는 가져오고 없으면 404페이지를 띄운다
    question = get_object_or_404(Question, pk=request_id)
    choice_list = get_list_or_404(question.choice_set)

    # form 태그를 쓸때는 csrf토큰을 사용해 보안을 막아야 한다.

    output = ''
    output += '<h1>' + question.question_text + '</h1>'
    output += '<form action="/polls/vote/' + str(question.id) + '" method="post">'

    for choice in choice_list:
        output += '<input type="radio" name="choice" value="' + str(choice.id) + '"/> ' + choice.choice_text + '<br>'

    output += '<input type="submit" value="Vote">'
    output += '</form>'
    return HttpResponse(output)


def result_view(request, request_id):
    question = get_object_or_404(Question, pk=request_id)
    choice_list = get_list_or_404(question.choice_set)

    output = '<h1>' + question.question_text + '</h1>'
    for choice in choice_list:
        output += choice.choice_text + ' : ' + str(choice.votes) + '<br>'

    return HttpResponse(output)


def vote(request, request_id):
    question = get_object_or_404(Question, pk=request_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])

    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect('/polls/result/' + str(question.id))
