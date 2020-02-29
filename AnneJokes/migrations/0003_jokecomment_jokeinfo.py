# Generated by Django 2.2.7 on 2020-02-25 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AnneJokes', '0002_auto_20200218_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='JokeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joke_type', models.IntegerField(choices=[(1, '点赞'), (2, '点踩')])),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('joke', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AnneJokes.UserJokes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AnneJokes.User')),
            ],
        ),
        migrations.CreateModel(
            name='JokeComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=128)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('comment_self', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AnneJokes.JokeComment')),
                ('joke', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AnneJokes.UserJokes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AnneJokes.User')),
            ],
        ),
    ]
