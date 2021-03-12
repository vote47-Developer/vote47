from django.db import models
from django.contrib.auth.models import AbstractUser


class Candidate(models.Model):
    num = models.PositiveIntegerField(verbose_name="후보자번호")
    name = models.CharField(max_length=100, verbose_name='후보자이름')
    poster = models.ImageField(
        upload_to='profile_image/%Y/%m/%d', verbose_name='프로필 이미지', blank=True)
    url = models.URLField(verbose_name='온라인공약집링크', blank=True)


class User(models.Model):
    nickname = models.CharField(max_length=100, verbose_name="닉네임")
    age = models.PositiveIntegerField(verbose_name='나이')
    job = models.CharField(max_length=100, verbose_name='직업')
    result = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, blank=True, null=True)
    TYPE_OF_GENDER = (
        ('male', '남성'),
        ('female', '여성'),
        ('none', '선택하지않음'),
    )
    gender = models.CharField(max_length=20, choices=TYPE_OF_GENDER)

    def __str__(self):
        return self.nickname


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
        return self.num
