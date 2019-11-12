from django.urls import path
from .views import IndexView, DetailView, ResultView, vote


# 뷰파일에 함수명은 바로 쓰지만 클래스를 사용한 제네릭뷰인 리스트뷰나 디테일뷰를 사용시 뒤에 as.view() 를사용한다
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:request_id>', DetailView.as_view()),
    path('result/<int:request_id>', ResultView.as_view()),
    path('vote/<int:request_id>', vote)
]

