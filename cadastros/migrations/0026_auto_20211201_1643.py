# Generated by Django 3.1.7 on 2021-12-01 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0025_auto_20211201_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doadores',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
