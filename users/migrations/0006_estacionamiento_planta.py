# Generated by Django 2.0.13 on 2019-07-12 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190712_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacionamiento',
            name='planta',
            field=models.CharField(default='2', max_length=2),
            preserve_default=False,
        ),
    ]
