# Generated by Django 2.2.3 on 2019-07-28 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0002_auto_20190529_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partener',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('logo', models.ImageField(upload_to='')),
                ('group', models.CharField(max_length=64)),
            ],
        ),
    ]