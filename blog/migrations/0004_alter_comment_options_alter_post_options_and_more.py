# Generated by Django 4.2.16 on 2024-10-29 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_on']},
        ),
        migrations.AddField(
            model_name='comment',
            name='challenge',
            field=models.SlugField(default='a_slug'),
        ),
    ]
