# Generated by Django 3.2.4 on 2021-07-02 10:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Test_csv',
            field=models.FileField(upload_to='Home/excel', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv'])]),
        ),
        migrations.AlterField(
            model_name='project',
            name='Train_csv',
            field=models.FileField(upload_to='Home/excel', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv'])]),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together={('Name', 'U_id')},
        ),
    ]
