# Generated by Django 2.0.13 on 2019-07-12 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacionamiento',
            name='tipo',
            field=models.CharField(choices=[('PUBLICO', 'PUBLICO'), ('PRIVADO', 'PRIVADO')], default='PRIVADO', max_length=80),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='tipo',
            field=models.CharField(choices=[('ARRENDATARIO', 'ARRENDATARIO'), ('COMUN', 'COMUN')], default='COMUN', max_length=80),
        ),
    ]
