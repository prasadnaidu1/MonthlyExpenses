# Generated by Django 2.1.1 on 2018-10-27 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='showdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp', models.CharField(max_length=50)),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
    ]
