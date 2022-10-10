# Generated by Django 3.2.12 on 2022-10-08 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='shirt_size',
            field=models.CharField(choices=[('xs', 'Xs'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'Xl')], max_length=255, null=True),
        ),
    ]
