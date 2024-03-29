# Generated by Django 2.0.13 on 2019-07-12 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_hora', models.CharField(max_length=4)),
                ('direccion', models.CharField(max_length=30)),
                ('numero', models.CharField(max_length=3)),
                ('letra', models.CharField(max_length=2)),
                ('hora_min', models.CharField(max_length=5)),
                ('hora_max', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='cod',
            field=models.CharField(default='x', max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='mes_año',
            field=models.CharField(default='x', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='nombre_completo',
            field=models.CharField(default='x', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='numero_tarjeta',
            field=models.CharField(default='x', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='rut',
            field=models.CharField(default='x', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='dueno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
