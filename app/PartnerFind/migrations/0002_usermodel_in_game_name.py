# Generated by Django 4.2.6 on 2023-11-15 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PartnerFind', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='in_game_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]