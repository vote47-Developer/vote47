from django import forms
from .models import User
# from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ["nickname", "age", "job", "result", "gender"]

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = "__all__"