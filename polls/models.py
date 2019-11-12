from django.db import models


class Question(models.Model):
    # 어떤색상을 좋아하세요? 라는 질문들이 들어갈 필드
    question_text = models.CharField(max_length=200)
    # 2019년 11월 12일날 등록 이라는 데이터
    pub_date = models.DateTimeField('등록날짜')

    # question object(1)로 어드민에 나오는 문제를 직접질문한 내용을 볼수 있도록 바꿈
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # Question 클래스 에 연결된 데이터가 삭제되면 같이 삭제해준다
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 선택 목록 들 색상 초록색
    choice_text = models.CharField(max_length=200)
    # 투표수
    votes = models.IntegerField(default=0)
