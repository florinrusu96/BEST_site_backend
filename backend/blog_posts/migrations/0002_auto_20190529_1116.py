# Generated by Django 2.2.1 on 2019-05-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("blog_posts", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="english_content",
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name="blogpost", name="content", field=models.TextField(default=None)
        ),
    ]
