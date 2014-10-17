# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Sandwich(models.Model):
    name = models.CharField(_('nome'), max_length=100)
    created_at = models.DateTimeField(_('criado em'), auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = _(u'sanduíche')
        verbose_name_plural = _(u'sanduíches')

    def __unicode__(self):
        return u'%s' % self.name
