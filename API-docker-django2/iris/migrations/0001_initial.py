# Generated by Django 3.1.2 on 2020-10-12 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iris',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('features', models.CharField(max_length=20)),
                ('label', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]