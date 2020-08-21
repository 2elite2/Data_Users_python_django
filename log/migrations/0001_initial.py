# Generated by Django 3.1 on 2020-08-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=12)),
                ('date', models.DateField()),
                ('school', models.TextField()),
                ('year', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'Member',
            },
        ),
    ]