# Generated by Django 4.0 on 2021-12-15 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_fb_login_id_alter_upload_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fb_login',
            name='imgid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.upload'),
        ),
    ]
