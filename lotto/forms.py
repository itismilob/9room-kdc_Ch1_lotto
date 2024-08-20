from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):

    # 받아올 데이터가 명시되어 있는 메타 데이터
    class Meta:
        model = GuessNumbers
        fields = ('name', 'text',) # 입력 받을 데이터
