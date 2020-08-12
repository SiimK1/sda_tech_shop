# Generated by Django 2.2.14 on 2020-08-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0005_auto_20200805_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('AD', 'At Delivery'), ('D', 'Delivered')], max_length=15, null=True),
        ),
    ]
