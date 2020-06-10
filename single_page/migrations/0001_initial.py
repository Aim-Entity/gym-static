# Generated by Django 2.2.7 on 2020-05-30 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=300)),
                ('message', models.CharField(max_length=850)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='mentor_img')),
                ('role', models.CharField(max_length=200)),
                ('facebook', models.URLField(blank=True, max_length=1200, null=True)),
                ('twitter', models.URLField(blank=True, max_length=1200, null=True)),
                ('instagram', models.URLField(blank=True, max_length=1200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=1500)),
            ],
            options={
                'verbose_name_plural': "Package's",
            },
        ),
        migrations.CreateModel(
            name='Tick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='single_page.Package')),
            ],
        ),
        migrations.CreateModel(
            name='Cross',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='single_page.Package')),
            ],
            options={
                'verbose_name_plural': 'Cross',
            },
        ),
    ]