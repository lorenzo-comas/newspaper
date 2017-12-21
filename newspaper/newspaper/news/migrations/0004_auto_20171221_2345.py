# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_event_publish_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'event', 'verbose_name_plural': 'events'},
        ),
    ]
