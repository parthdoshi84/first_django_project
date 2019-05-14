# Generated by Django 2.2.1 on 2019-05-14 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('age', models.CharField(max_length=3)),
                ('about', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('age', models.CharField(max_length=3)),
                ('about', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('age', models.CharField(max_length=3)),
                ('about', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('rating', models.FloatField(blank=True)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('actor', models.ManyToManyField(to='imdb.Actor')),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='imdb.Director')),
                ('producer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='imdb.Producer')),
            ],
        ),
    ]
