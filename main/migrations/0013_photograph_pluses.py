# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20141027_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='photograph',
            name='pluses',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
