# Generated by Django 4.0.2 on 2022-03-23 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendmail', '0002_city_area_alter_city_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='City123',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('populations', models.IntegerField()),
                ('area', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'sity',
            },
        ),
    ]
