from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django import forms


class Candidate(models.Model):
    num = models.PositiveIntegerField(verbose_name="후보자번호")
    name = models.CharField(max_length=100, verbose_name='후보자이름')
    poster = models.ImageField(
        upload_to='profile_image/%Y/%m/%d', verbose_name='프로필 이미지', blank=True)
    url = models.URLField(verbose_name='온라인공약집링크', blank=True)


def is_nickname(value):
    if value == None:
        raise forms.ValidationError("no")


class User(AbstractUser):
    nickname = models.CharField(
        max_length=100, verbose_name="닉네임", blank=True, null=True, validators=[is_nickname])
    age = models.PositiveIntegerField(verbose_name='나이', blank=True, null=True)
    job = models.CharField(
        max_length=100, verbose_name='직업', blank=True, null=True)
    result = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, blank=True, null=True)
    TYPE_OF_GENDER = (
        ('male', '남성'),
        ('female', '여성'),
        ('none', '선택하지않음'),
    )
    gender = models.CharField(
        max_length=20, choices=TYPE_OF_GENDER, blank=True, null=True)
    username = models.CharField(
        max_length=150, verbose_name="이름", blank=True, null=True)

    USERNAME_FIELD = "id"
    REQUIRED_FIELDS = ["username", "nickname", "age", "job", "gender"]

    def __str__(self):
        if self.nickname:
            return self.nickname
        elif self.username:
            return self.username
        elif self.age:
            return str(self.age)

    # def clean(self, *args, ** kwargs):
    #     nickname = self.nickname
    #     if nickname == "":
    #         raise ValidationError("사용자의 닉네임을 입력하세요.")


class Quiz(models.Model):
    num = models.PositiveIntegerField(verbose_name="질문 번호")
    question = models.TextField(verbose_name="질문")
    background = models.TextField(verbose_name="질문에 대한 배경 설명")

    def __str__(self):
        return self.question


class Example(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="examples", verbose_name="질문")
    num = models.PositiveIntegerField(verbose_name="선택지 번호")
    title = models.TextField(verbose_name="선택지")
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    num = models.PositiveIntegerField(verbose_name="질문 번호")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="enrollments", verbose_name="유저")
    example = models.ForeignKey(
        Example, on_delete=models.CASCADE, related_name="enrollments", verbose_name="선택한 선택지")

    def __str__(self):
        return str(self.num)
