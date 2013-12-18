from django.db import models

from zinnia.models_bases.entry import AbstractEntry


class CustomEntry(AbstractEntry):
    public = models.BooleanField(
        default=False,
    )

    def __unicode__(self):
        return 'SomeEntry %s ' % self.title

    class Meta(AbstractEntry.Meta):
        abstract = True
