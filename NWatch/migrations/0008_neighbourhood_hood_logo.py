# Generated by Django 2.2.6 on 2019-10-27 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NWatch', '0007_auto_20191027_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='hood_logo',
            field=models.ImageField(default='hood.jpg', upload_to='hoods/'),
        ),
    ]