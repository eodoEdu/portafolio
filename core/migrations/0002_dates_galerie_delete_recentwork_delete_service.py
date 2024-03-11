# Generated by Django 5.0.3 on 2024-03-10 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Date name')),
                ('description', models.TextField(verbose_name='About date')),
            ],
        ),
        migrations.CreateModel(
            name='Galerie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Picture description')),
                ('image', models.ImageField(upload_to='picture')),
            ],
        ),
        migrations.DeleteModel(
            name='RecentWork',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
