# Generated by Django 4.0.5 on 2022-06-03 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_title', models.CharField(max_length=255, verbose_name='Имя: ')),
                ('q_text', models.TextField(verbose_name='Вопрос: ')),
                ('q_date', models.DateTimeField(verbose_name='Дата публикации: ')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=55, verbose_name='Имя автора: ')),
                ('comment_text', models.TextField(max_length=200, verbose_name='Текст комментария: ')),
                ('aricle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.question')),
            ],
        ),
    ]
