# Generated by Django 2.2 on 2019-04-19 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20190418_1630'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='show',
            order_with_respect_to='theatre',
        ),
    ]