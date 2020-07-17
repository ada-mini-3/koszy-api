# Generated by Django 3.0.8 on 2020-07-17 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('lat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('long', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
    ]