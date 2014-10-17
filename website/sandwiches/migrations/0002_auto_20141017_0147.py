# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sandwiches', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sandwich',
            options={'ordering': ['name'], 'verbose_name': 'sandu\xedche', 'verbose_name_plural': 'sandu\xedches'},
        ),
        migrations.AddField(
            model_name='sandwich',
            name='created_at',
            field=models.DateTimeField(default=datetime.date(2014, 10, 17), verbose_name='criado em', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sandwich',
            name='name',
            field=models.CharField(default='nome', max_length=100, verbose_name='nome'),
            preserve_default=False,
        ),
    ]
