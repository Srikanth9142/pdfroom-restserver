# Generated by Django 3.0.2 on 2020-02-02 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='media/')),
                ('coverphoto', models.ImageField(upload_to='media/')),
                ('author', models.CharField(max_length=150)),
            ],
        ),
    ]
