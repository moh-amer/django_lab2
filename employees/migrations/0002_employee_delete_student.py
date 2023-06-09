# Generated by Django 4.2 on 2023-05-04 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('age', models.IntegerField(default=18, max_length=60)),
                ('salary', models.FloatField(default=0.0, max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
