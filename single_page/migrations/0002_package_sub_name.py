# Generated by Django 2.2.7 on 2020-05-30 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='sub_name',
            field=models.CharField(default='Subname', max_length=400),
        ),
    ]