#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from django.test import TestCase
from zinnia.models import Entry

class ZinniaTests(TestCase):
    """Test zinnia pathological explode database."""

    def test_break_database_destroy(self):
        """This test will cause the database to have open transactions most
        of the time. It seems to be more consistent on better hardware..."""
        entry = Entry.objects.create(
            title='view this',
            slug='view-this',
            content='post',
            status=2,
        )
