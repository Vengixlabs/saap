# Generated by Django 3.1.6 on 2021-02-27 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210227_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]