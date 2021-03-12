# Generated by Django 3.1.7 on 2021-03-12 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveIntegerField(verbose_name='후보자번호')),
                ('name', models.CharField(max_length=100, verbose_name='후보자이름')),
                ('poster', models.ImageField(blank=True, upload_to='profile_image/%Y/%m/%d', verbose_name='프로필 이미지')),
                ('url', models.URLField(blank=True, verbose_name='온라인공약집링크')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveIntegerField(verbose_name='질문 번호')),
                ('question', models.TextField(verbose_name='질문')),
                ('background', models.TextField(verbose_name='질문에 대한 배경 설명')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100, verbose_name='닉네임')),
                ('age', models.PositiveIntegerField(verbose_name='나이')),
                ('job', models.CharField(max_length=100, verbose_name='직업')),
                ('gender', models.CharField(choices=[('male', '남성'), ('female', '여성'), ('none', '선택하지않음')], max_length=20)),
                ('result', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vote.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveIntegerField(verbose_name='선택지 번호')),
                ('title', models.TextField(verbose_name='선택지')),
                ('is_answer', models.BooleanField(default=False)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examples', to='vote.quiz', verbose_name='질문')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveIntegerField(verbose_name='질문 번호')),
                ('example', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='vote.example', verbose_name='선택한 선택지')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='vote.user', verbose_name='유저')),
            ],
        ),
    ]
