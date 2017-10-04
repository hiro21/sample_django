# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publoshed_date',
            new_name='published_date',
        ),
    ]
