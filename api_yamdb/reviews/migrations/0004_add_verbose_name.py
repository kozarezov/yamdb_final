from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('reviews', '0003_related_names_added'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий',
                     'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Отзыв',
                     'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True,
                                   serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True,
                                   serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True,
                                   serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True,
                                   serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='title',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True,
                                   serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='titlegenre',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True,
                                   serialize=False, verbose_name='ID'),
        ),
    ]
