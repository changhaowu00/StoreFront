# Generated by Django 4.0.6 on 2022-07-19 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customer_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='feature_product',
            new_name='featured_product',
        ),
    ]