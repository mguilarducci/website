# coding: utf-8

from datetime import datetime
from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth.models import User
from model_mommy import mommy
from website.sandwiches.models import Sandwich
from website.ratings.models import Rating


class RatingModelTest(TestCase):
    def setUp(self):
        self.sandwich = mommy.make(Sandwich)
        self.user = mommy.make(User)
        self.obj = Rating(
            score=4.5,
            description=u'Descrição da avaliação',
            kind='PS',
            user=self.user,
            sandwich=self.sandwich
        )

    def test_create(self):
        """
        Rating should have score, description, kind and user
        """
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        """
        Rating must have automatic created_at
        """
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        """
        Unicode returns the Rating name
        """
        self.assertEqual('4.5', unicode(self.obj))

    def test_unique(self):
        """
        Rating should be unique (user, sandwich, kind)
        """
        self.obj.save()
        r = Rating(
            score=4.0,
            description=u'Descrição da avaliação',
            kind='PS',
            user=self.user,
            sandwich=self.sandwich
        )
        
        self.assertRaises(IntegrityError, r.save)
