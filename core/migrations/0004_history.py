# Generated by Django 4.2.4 on 2023-08-06 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_post_id_alter_post_post_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post')),
            ],
        ),
    ]
