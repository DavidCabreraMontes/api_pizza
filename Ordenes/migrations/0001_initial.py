# Generated by Django 2.1.5 on 2019-07-10 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuarios', '0001_initial'),
        ('Carrito', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.TextField()),
                ('referencia', models.TextField()),
                ('total', models.FloatField()),
                ('tarjeta', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
                ('id_Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Usuarios')),
                ('pedido', models.ManyToManyField(related_name='Carrito', to='Carrito.Carrito')),
            ],
            options={
                'db_table': 'ORDENES',
            },
        ),
    ]
