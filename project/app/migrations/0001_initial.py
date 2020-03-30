# Generated by Django 3.0.4 on 2020-03-30 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SomeObjectType',
            fields=[
                ('sot_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SomeObject',
            fields=[
                ('so_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.SomeObjectType')),
            ],
        ),
    ]
