# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from website.sandwiches.models import Sandwich


class Rating(models.Model):
    KINDS = (
        ('PS', _(u'Poder de Sedução')),
        ('SI', _(u'Segunda Impressão')),
        ('AP', _(u'Apetitosidade')),
        ('CB', _(u'Custo x Benefício')),
    )

    score = models.DecimalField(_('score'), max_digits=2, decimal_places=1)
    description = models.TextField(_(u'descrição'), max_length=255)
    kind = models.CharField(_(u'área'), max_length=2, choices=KINDS)
    user = models.ForeignKey(User, verbose_name=_('avaliador'))
    sandwich = models.ForeignKey(Sandwich, verbose_name=_(u'Sanduíche'))
    created_at = models.DateTimeField(_('criado em'), auto_now_add=True)

    class Meta:
        ordering = ['-created_at', 'sandwich', 'kind', 'score']
        verbose_name = _(u'avaliação')
        verbose_name_plural = _(u'avaliações')
        unique_together = ('kind', 'user', 'sandwich')

    def __unicode__(self):
        return u'%.1f' % self.score
