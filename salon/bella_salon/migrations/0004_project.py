# Generated by Django 3.2.9 on 2021-12-29 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bella_salon', '0003_rename_service_service_service_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=1000)),
                ('service', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]
