from django.contrib import admin
from .models import Question, Choice
# Register your models here.


# choice라는 선택목록을 question model 안에 넣어서 admin page 에서 보여주기 위해 작성한다.
class ChoiceInline(admin.TabularInline):
    model = Choice
    # 선택 목록의 기본 갯수
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)