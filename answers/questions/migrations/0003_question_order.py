# Generated by Django 2.1.7 on 2019-03-05 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_question_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='order',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
