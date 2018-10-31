# Generated by Django 2.1.1 on 2018-10-27 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expenses', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('members', models.CharField(max_length=150)),
                ('res', models.IntegerField(default=10)),
            ],
        ),
    ]
