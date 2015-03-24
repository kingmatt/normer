# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ratings.models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_auto_20150316_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='created_at',
            field=models.DateTimeField(default=ratings.models.default_create_time),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subject',
            name='ip_address',
            field=models.GenericIPAddressField(null=True),
            preserve_default=True,
        ),
    ]
