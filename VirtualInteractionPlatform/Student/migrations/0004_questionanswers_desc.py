# Generated by Django 3.2.4 on 2021-06-17 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_questionanswers'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionanswers',
            name='desc',
            field=models.CharField(default='', max_length=300),
        ),
    ]