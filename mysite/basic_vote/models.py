# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Vote(models.Model):
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    qb1 = models.BooleanField(default=False)
    qb2 = models.BooleanField(default=False)
    qb3 = models.BooleanField(default=False)
    qb4 = models.BooleanField(default=False)
    more_info = models.CharField(max_length=1000, default='')
