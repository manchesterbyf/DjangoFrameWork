# Generated by Django 2.1.8 on 2019-10-05 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32)),
                ('username', models.CharField(blank=True, max_length=32, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=32, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=32, null=True)),
                ('adress', models.TextField(blank=True, null=True)),
                ('User_type', models.IntegerField(default=0)),
            ],
        ),
    ]
