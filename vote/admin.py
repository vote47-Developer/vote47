from django.contrib import admin
from . import models
from .models import *
from .forms import UserForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['nickname']
    list_display_links = ["nickname"]
    form = UserForm


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ["num", 'name']
    list_display_links = ["num", "name"]


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question')


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'quiz', 'title', 'is_answer')

    def get_queryset(self, request):
        return self.model.objects.select_related('quiz').all()

    def quiz(self, obj):
        return obj.quiz.question


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ["num", "user", "example"]
    list_display_links = ["num", "user", "example"]
