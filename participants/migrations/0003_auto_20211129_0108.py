# Generated by Django 3.0 on 2021-11-28 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0002_profile_mobile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]