# -*- coding: utf-8 -*-

from __future__ import (print_function, division, absolute_import, unicode_literals)

from django.db import models

from django.utils.translation import ugettext_lazy as _


class CardType(models.Model):
    name = models.CharField(_("Type of Card"), max_length=250, unique=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(_("Card's Name"), max_length=250, unique=True)
    description = models.TextField(_("Description"))
    mana_cost = models.PositiveIntegerField(_("Mana Cost"), default=0)
    life = models.PositiveIntegerField(_("Life"), default=0)
    damage = models.PositiveIntegerField(_("Damage"), default=0)
    card_type = models.ForeignKey(CardType, verbose_name=_("Type of Card"))
    modified = models.PositiveIntegerField(_("Modified"), null=True)

    def __str__(self):
        return " %s, type : %s " % (self.name, self.card_type)
