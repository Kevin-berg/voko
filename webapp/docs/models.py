from django.db import models
from django.utils.text import slugify
from django_extensions.db.models import TimeStampedModel


class Document(TimeStampedModel):
    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documenten'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='docs/%Y/%m/%d')
    slug = models.SlugField(unique=True, editable=False, max_length=100)

    def save(self, **kwargs):
        self.slug = slugify(self.name)
        return super(Document, self).save(**kwargs)

    def __str__(self):
        return self.name


class Link(TimeStampedModel):
    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name
