# Generated by Django 4.1.1 on 2022-09-10 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_todo_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='create',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]