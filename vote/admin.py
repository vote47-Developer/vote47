from django.contrib import admin
from . import models
from .models import User, Result, Candidate, Question, Choice


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['nickname']


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['candidate']


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question']


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question']
