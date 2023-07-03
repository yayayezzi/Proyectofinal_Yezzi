# Generated by Django 4.2.2 on 2023-07-02 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('escudo', models.ImageField(upload_to='escudos/')),
            ],
        ),
        migrations.CreateModel(
            name='Liga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('equipos', models.ManyToManyField(to='Basquet2023_DatosApp.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('altura', models.DecimalField(decimal_places=2, max_digits=4)),
                ('posicion', models.CharField(max_length=50)),
                ('valor_mercado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('foto', models.ImageField(upload_to='fotos_jugadores/')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Basquet2023_DatosApp.equipo')),
            ],
        ),
    ]
