# Generated by Django 3.1 on 2020-08-29 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200829_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='user_pw',
            field=models.CharField(default=False, max_length=20),
        ),
    ]
