# Generated by Django 3.1.4 on 2021-01-03 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('victims', '0003_victim_id_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='victim',
            name='is_complete',
            field=models.IntegerField(choices=[(1, 'Complete'), (0, 'Not complete')], default=1),
        ),
    ]
