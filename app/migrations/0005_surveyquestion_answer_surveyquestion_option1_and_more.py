# Generated by Django 4.0.5 on 2022-06-14 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_survey_user_delete_surveycompleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyquestion',
            name='answer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='surveyquestion',
            name='option1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='surveyquestion',
            name='option2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='surveyquestion',
            name='option3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='surveyquestion',
            name='option4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
