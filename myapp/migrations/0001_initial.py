# Generated by Django 4.0 on 2021-12-15 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('img', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fb_login',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('mob_email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('con_pass', models.CharField(max_length=50)),
                ('date_ofbi', models.DateField(max_length=20)),
                ('gen_der', models.CharField(max_length=20, null=True)),
                ('imgid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.upload')),
            ],
        ),
    ]