# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sandwiches', '0002_auto_20141017_0147'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.DecimalField(verbose_name='score', max_digits=2, decimal_places=1)),
                ('description', models.TextField(max_length=255, verbose_name='descri\xe7\xe3o')),
                ('kind', models.CharField(max_length=2, verbose_name='\xe1rea', choices=[(b'PS', 'Poder de Sedu\xe7\xe3o'), (b'SI', 'Segunda Impress\xe3o'), (b'AP', 'Apetitosidade'), (b'CB', 'Custo x Benef\xedcio')])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('sandwich', models.ForeignKey(verbose_name='Sandu\xedche', to='sandwiches.Sandwich')),
                ('user', models.ForeignKey(verbose_name='avaliador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', 'sandwich', 'kind', 'score'],
                'verbose_name': 'avalia\xe7\xe3o',
                'verbose_name_plural': 'avalia\xe7\xf5es',
            },
            bases=(models.Model,),
        ),
    ]
