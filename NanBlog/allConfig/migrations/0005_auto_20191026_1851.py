# Generated by Django 2.2.6 on 2019-10-26 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allConfig', '0004_auto_20191026_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='allinfo',
            name='contactText',
            field=models.TextField(default='Send us your query anytime!'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='allinfo',
            name='description',
            field=models.TextField(null=True),
        ),
    ]