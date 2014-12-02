import datetime

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.test import TestCase

from food_mood.models import Entry, UserProfile

class EntryMethodTests(TestCase):

    def test_1(self):
        """
        comments on the test
        """
        self.assertEqual(False, False)
