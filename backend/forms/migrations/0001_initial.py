# Generated by Django 2.2.3 on 2019-09-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=150)),
                ('content', models.TextField(max_length=1000)),
            ],
        ),
    ]
