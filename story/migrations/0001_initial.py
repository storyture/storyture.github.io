# Generated by Django 3.1.7 on 2021-02-28 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_name', models.CharField(max_length=60)),
                ('happy_count', models.IntegerField(default=0)),
                ('sad_count', models.IntegerField(default=0)),
                ('interested', models.IntegerField(default=0)),
            ],
        ),
    ]
