import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_add_reviews_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('text', models.TextField(max_length=800,
                                          verbose_name='Текст отзыва')),
                ('score',
                 models.IntegerField(null=True, verbose_name='Оценка')),
                ('pub_date', models.DateTimeField(auto_now_add=True,
                                                  verbose_name='Дата публикации')),
                ('author',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL,
                                   verbose_name='Автор отзыва')),
                ('title',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='reviews.title',
                                   verbose_name='Произведение')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('text', models.TextField(max_length=200,
                                          verbose_name='Комментарий к отзыву')),
                ('pub_date', models.DateTimeField(auto_now_add=True,
                                                  verbose_name='Дата публикации')),
                ('author',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL,
                                   verbose_name='Автор комментария')),
                ('review',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='reviews.review')),
            ],
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('title', 'author'),
                                               name='unique_review'),
        ),
    ]
