# Generated by Django 5.0.2 on 2024-02-26 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YourModelName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
            ],
        ),
    ]
