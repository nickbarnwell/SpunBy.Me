"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from common.models import *

class PartyTest(TestCase):
    def test_create(self):
        Party(name='testing123', use)
