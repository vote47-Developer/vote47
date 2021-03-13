from django import forms
from .models import User, Enrollment


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = "__all__"