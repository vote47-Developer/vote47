from django import forms
from .models import User
# from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ["nickname", "age", "job", "result", "gender"]

        def clean_nickname(self, *args, **kwargs):
            nickname = self.cleaned_data.get("nickname")
            print(nickname)
            if nickname == "hi":
                raise forms.ValidationError("닉네임을 입력하세요")
            return nickname
