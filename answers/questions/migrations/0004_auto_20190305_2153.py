# Generated by Django 2.1.7 on 2019-03-05 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_question_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
