# Generated by Django 2.2.5 on 2019-10-08 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('passw', models.CharField(max_length=15)),
                ('name', models.CharField(default='黑户口', max_length=20)),
                ('email', models.CharField(max_length=80, null=True)),
                ('priv', models.CharField(default='1', max_length=1)),
                ('state', models.CharField(default='1', max_length=1)),
                ('reg_time', models.DateField()),
            ],
        ),
    ]
