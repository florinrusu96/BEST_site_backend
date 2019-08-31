# Generated by Django 2.2.3 on 2019-07-28 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=50)),
                ('partner_image', models.ImageField(upload_to='events/partner_images')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='events/pictures')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('event_banner', models.ImageField(blank=True, upload_to='events/general_pictures')),
                ('event_background', models.ImageField(blank=True, upload_to='events/general_pictures')),
                ('event_description', models.TextField(max_length=500)),
                ('event_google_form', models.TextField(blank=True)),
                ('event_partners', models.ManyToManyField(blank=True, to='events.Partner')),
                ('event_pictures', models.ManyToManyField(blank=True, to='events.Picture')),
            ],
        ),
    ]