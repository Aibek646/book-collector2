# Generated by Django 3.0.5 on 2020-04-12 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20200412_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.ManyToManyField(to='main_app.AuthorName'),
        ),
    ]
