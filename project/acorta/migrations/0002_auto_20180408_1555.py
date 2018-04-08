# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urls',
            old_name='short',
            new_name='url_acortada',
        ),
        migrations.RenameField(
            model_name='urls',
            old_name='longer',
            new_name='url_original',
        ),
    ]
