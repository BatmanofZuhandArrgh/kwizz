# Generated by Django 3.2.2 on 2021-06-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputFirstNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num0', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='InputOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op', models.CharField(choices=[('ADD', '+'), ('SUB', '-'), ('MUL', 'x')], default='ADD', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='InputSecondNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num1', models.IntegerField(default=0)),
            ],
        ),
    ]
