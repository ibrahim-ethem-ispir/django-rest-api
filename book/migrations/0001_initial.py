# Generated by Django 5.1.1 on 2024-09-23 19:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('published', models.BooleanField()),
                ('published_date', models.DateField()),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
