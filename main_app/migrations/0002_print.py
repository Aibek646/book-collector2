# Generated by Django 3.0.5 on 2020-04-11 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Print',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('cover', models.CharField(choices=[('P', 'Paperback'), ('C', 'Case Wrap'), ('D', 'Dust Jacket')], default='P', max_length=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Book')),
            ],
        ),
    ]
