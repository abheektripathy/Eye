# Generated by Django 3.2.12 on 2022-10-08 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirts', '0002_alter_shirts_shirt_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirts',
            name='size',
            field=models.CharField(choices=[('XS', 'Xs'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'Xl')], max_length=10),
        ),
    ]
