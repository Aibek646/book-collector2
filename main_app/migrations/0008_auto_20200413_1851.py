# Generated by Django 3.0.5 on 2020-04-13 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200413_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='translator',
            old_name='language',
            new_name='country',
        ),
    ]
