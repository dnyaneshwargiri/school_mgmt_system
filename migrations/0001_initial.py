# Generated by Django 2.1 on 2018-09-13 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rollno', models.CharField(max_length=20)),
                ('classname', models.CharField(max_length=20)),
                ('courseid', models.CharField(max_length=20)),
                ('dob', models.DateField(verbose_name='Date')),
                ('addres', models.CharField(max_length=20)),
                ('parentname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=20)),
            ],
        ),
    ]