# Generated by Django 4.0.5 on 2022-06-17 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='usertype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.usertype'),
        ),
    ]