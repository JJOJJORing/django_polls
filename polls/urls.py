from django.urls import path
from .views import IndexView, DetailView, ResultView, vote, ApiQuestionList


# 뷰파일에 함수명은 바로 쓰지만 클래스를 사용한 제네릭뷰인 리스트뷰나 디테일뷰를 사용시 뒤에 as.view() 를사용한다
# 제네릭뷰를 사용시 <int:pk> 에서 무조건 pk를 사용해야한다
# vote 는 제네릭뷰를 사용하지 않으므로 request_id를 사용할수 있다.
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:pk>', DetailView.as_view()),
    path('result/<int:pk>', ResultView.as_view()),
    path('vote/<int:request_id>', vote),
    path('api/', ApiQuestionList.as_view())
]

