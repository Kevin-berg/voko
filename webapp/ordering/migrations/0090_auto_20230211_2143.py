# Generated by Django 2.2.28 on 2023-02-11 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0089_merge_20230202_2211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='draftproduct',
            options={'get_latest_by': 'modified'},
        ),
    ]
