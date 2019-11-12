from .models import Question
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        # 나중엔 내려줄 것만 따로정의 예를들면 유저의 패스워드는 내려주면 안되기때문에