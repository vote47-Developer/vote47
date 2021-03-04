from django.db import models
from django.contrib.auth.models import AbstractUser


class Result(models.Model):
    candidate = models.CharField(max_length=100, verbose_name='후보자이름')
    q1 = models.PositiveIntegerField(verbose_name='1번 질문의 답')
    q2 = models.PositiveIntegerField(verbose_name='2번 질문의 답')
    q3 = models.PositiveIntegerField(verbose_name='3번 질문의 답')
    q4 = models.PositiveIntegerField(verbose_name='4번 질문의 답')
    q5 = models.PositiveIntegerField(verbose_name='5번 질문의 답')
    q6 = models.PositiveIntegerField(verbose_name='6번 질문의 답')
    q7 = models.PositiveIntegerField(verbose_name='7번 질문의 답')
    q8 = models.PositiveIntegerField(verbose_name='8번 질문의 답')
    q9 = models.PositiveIntegerField(verbose_name='9번 질문의 답')
    q10 = models.PositiveIntegerField(verbose_name='10번 질문의 답')
    q11 = models.PositiveIntegerField(verbose_name='11번 질문의 답')
    q12 = models.PositiveIntegerField(verbose_name='12번 질문의 답')
    q13 = models.PositiveIntegerField(verbose_name='13번 질문의 답')


class User(models.Model):
    nickname = models.CharField(max_length=100, verbose_name="닉네임")
    age = models.PositiveIntegerField(verbose_name='나이')
    job = models.CharField(max_length=100, verbose_name='직업')
    result = models.OneToOneField(Result, on_delete=models.CASCADE)
    TYPE_OF_GENDER = (
        ('male', '남성'),
        ('female', '여성'),
        ('none', '선택하지않음'),
    )
    gender = models.CharField(max_length=20, choices=TYPE_OF_GENDER)

    def __str__(self):
        return self.nickname


class Candidate(models.Model):
    name = models.CharField(max_length=100, verbose_name='후보자이름')
    poster = models.ImageField(
        upload_to='profile_image/%Y/%m/%d', verbose_name='프로필 이미지', blank=True)
    url = models.URLField(verbose_name='온라인공약집링크', blank=True)


class Question(models.Model):
    question = models.TextField(verbose_name='질문')
    background = models.TextField(verbose_name='질문에 대한 배경 설명')


class Choice(models.Model):
    question = models.ForeignKey(
        Question, related_name='choices', verbose_name='질문', on_delete=models.CASCADE)
    choice1 = models.CharField(max_length=100, verbose_name='선택지1번')
    choice2 = models.CharField(max_length=100, verbose_name='선택지2번')
    choice3 = models.CharField(max_length=100, verbose_name='선택지3번')
    choice4 = models.CharField(
        max_length=100, verbose_name='선택지4번', null=True)
    choice5 = models.CharField(
        max_length=100, verbose_name='선택지5번', null=True)

class Quiz(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question


class Example(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="examples")
    title = models.TextField()
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.title