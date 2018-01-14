# Generated by Django 2.0.1 on 2018-01-03 06:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0002_auto_20180103_0525'),
    ]

    operations = [
        migrations.CreateModel(
            name='MFAL',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('mfal_code', models.CharField(max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='basesp',
            name='mfal',
        ),
        migrations.AddField(
            model_name='basesp',
            name='mfal',
            field=models.ManyToManyField(to='sp.MFAL'),
        ),
    ]
