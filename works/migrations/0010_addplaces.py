# Generated by Django 4.0.2 on 2022-02-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0009_delete_places'),
    ]

    operations = [
        migrations.CreateModel(
            name='addplaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=30)),
            ],
        ),
    ]
