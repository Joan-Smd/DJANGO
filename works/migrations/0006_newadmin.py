# Generated by Django 4.0.2 on 2022-02-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0005_userbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='newadmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('uname', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
