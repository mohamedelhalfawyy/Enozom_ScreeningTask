# Generated by Django 4.1.4 on 2022-12-23 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_code', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'country',
            },
        ),
    ]