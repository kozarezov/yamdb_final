import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=20, unique=True,
                                          verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=20, unique=True,
                                          verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('year', models.IntegerField(verbose_name='Дата релиза')),
                ('description', models.TextField(blank=True, null=True,
                                                 verbose_name='Описание')),
                ('rating',
                 models.IntegerField(null=True, verbose_name='Рейтинг')),
                ('category', models.ForeignKey(null=True,
                                               on_delete=django.db.models.
                                               deletion.SET_NULL,
                                               related_name='titles',
                                               to='reviews.category',
                                               verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TitleGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('genre',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='reviews.genre', verbose_name='Жанр')),
                ('title',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='reviews.title',
                                   verbose_name='Произведение')),
            ],
            options={
                'verbose_name': 'Произведение и жанр',
                'verbose_name_plural': 'Произведения и жанры',
            },
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(through='reviews.TitleGenre',
                                         to='reviews.genre',
                                         verbose_name='Жанр'),
        ),
    ]
