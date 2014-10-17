# coding: utf-8
from datetime import datetime
from django.test import TestCase
from website.sandwiches.models import Sandwich


class SandwichModelTest(TestCase):
    def setUp(self):
        self.obj = Sandwich(
            name='Big Tasty',
        )

    def test_create(self):
        """
        Sandwich should have a name
        """
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        """
        Sandwich must have automatic created_at
        """
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        """
        Unicode returns the Sandwich name
        """
        self.assertEqual(u'Big Tasty', unicode(self.obj))
