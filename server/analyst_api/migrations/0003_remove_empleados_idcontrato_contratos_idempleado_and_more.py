# Generated by Django 4.2.1 on 2023-06-02 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analyst_api', '0002_empleados_resultadosentrevista'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleados',
            name='idContrato',
        ),
        migrations.AddField(
            model_name='contratos',
            name='idEmpleado',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='analyst_api.empleados'),
        ),
        migrations.AlterField(
            model_name='contratos',
            name='descripcionCargo',
            field=models.TextField(blank=True),
        ),
    ]
