# Generated by Django 2.0 on 2018-01-03 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basesp',
            old_name='preference',
            new_name='take_rate',
        ),
        migrations.AlterField(
            model_name='basesp',
            name='mfal',
            field=models.CharField(max_length=5),
        ),
    ]