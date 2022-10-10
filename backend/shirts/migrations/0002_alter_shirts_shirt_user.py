# Generated by Django 3.2.12 on 2022-10-08 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shirts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirts',
            name='shirt_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
