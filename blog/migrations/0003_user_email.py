# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=datetime.datetime(2015, 6, 26, 2, 48, 37, 455682, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
