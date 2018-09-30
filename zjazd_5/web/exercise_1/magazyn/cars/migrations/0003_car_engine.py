# Generated by Django 2.1.1 on 2018-09-30 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engines', '0001_initial'),
        ('cars', '0002_auto_20180930_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='engine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='engines.Engine'),
        ),
    ]
