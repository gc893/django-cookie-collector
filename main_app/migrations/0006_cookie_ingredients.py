# Generated by Django 3.1.2 on 2020-10-09 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20201009_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookie',
            name='ingredients',
            field=models.ManyToManyField(to='main_app.Ingredient'),
        ),
    ]