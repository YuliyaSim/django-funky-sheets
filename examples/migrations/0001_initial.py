# Generated by Django 2.1.7 on 2019-02-17 12:59

from django.db import migrations, models
import django.db.models.deletion

from examples.models import Movie, Genre, Director, Country


def add_genres(apps, schema_editor):
    Genre.objects.create(name='Action')
    Genre.objects.create(name='Drama')
    Genre.objects.create(name='Horror')
    Genre.objects.create(name='Sci-Fi')
    Genre.objects.create(name='Thriller')


def add_directors(apps, schema_editor):
    Director.objects.create(name='Christopher Nolan')
    Director.objects.create(name='Paul W.S. Anderson')


def add_countries(apps, schema_editor):
    Country.objects.create(name='Slovenia')
    Country.objects.create(name='USA')
    Country.objects.create(name='France')
    Country.objects.create(name='Greece')
    Country.objects.create(name='Canada')


def add_movies(apps, schema_editor):
    movie_one = Movie.objects.create(
        title='Inception',
        imdb_link='https://www.imdb.com/title/tt1375666/',
        parents_guide=True,
        release_date='2010-07-16',
        director_id=1,
        country_id=2,
        imdb_rating=8.8
    )
    movie_one.genre.add(1, 4)
    movie_two = Movie.objects.create(
        title='Interstellar',
        imdb_link='https://www.imdb.com/title/tt0816692/',
        parents_guide=True,
        release_date='2014-11-06',
        director_id=1,
        country_id=2,
        imdb_rating=8.6
    )
    movie_two.genre.add(2, 4)
    movie_three = Movie.objects.create(
        title='Event horizon',
        imdb_link='https://www.imdb.com/title/tt0119081/',
        parents_guide=True,
        release_date='1997-12-04',
        director_id=2,
        country_id=2,
        imdb_rating=6.7)
    movie_three.genre.add(3, 4, 5)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, null=True)),
                ('imdb_link', models.URLField(null=True)),
                ('imdb_rating', models.DecimalField(decimal_places=1, max_digits=2, null=True)),
                ('parents_guide', models.BooleanField(default=False, null=True)),
                ('release_date', models.DateField(null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='examples.Country')),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='examples.Director')),
                ('genre', models.ManyToManyField(to='examples.Genre')),
            ],
        ),
        migrations.RunPython(add_genres, lambda apps, schema_editor: None),
        migrations.RunPython(add_directors, lambda apps, schema_editor: None),
        migrations.RunPython(add_countries, lambda apps, schema_editor: None),
        migrations.RunPython(add_movies, lambda apps, schema_editor: None),
    ]