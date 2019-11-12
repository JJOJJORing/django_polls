from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListAPIView
from .serializers import QuestionSerializer


class ApiQuestionList(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# 제네릭 뷰인 list view 로 바꿈
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultView(DetailView):
    model = Question
    template_name = 'polls/result.html'


# def detail_view(request, request_id):
#     # 페이지나 데이터가 있을때는 가져오고 없으면 404페이지를 띄운다
#     question = get_object_or_404(Question, pk=request_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def result_view(request, request_id):
#     question = get_object_or_404(Question, pk=request_id)
#     return render(request, 'polls/result.html', {'question': question})


def vote(request, request_id):
    question = get_object_or_404(Question, pk=request_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])

    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect('/polls/result/' + str(question.id))
