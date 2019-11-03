from abc import ABCMeta, abstractmethod, abstractproperty
from django.db import models
from mdeditor.fields import MDTextField

# Create your models here.
from django.utils.timezone import now

from drf_blog.utils import get_current_site


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('修改时间', default=now)

    def get_full_url(self):
        site = get_current_site().domain
        url = "https://{site}{path}".format(site=site, path=self.get_absolute_url())
        return url

    class Meta:
        abstract = True

    @abstractmethod
    def get_absolute_url(self):
        pass


class ExampleModel(models.Model):
    name = models.CharField(max_length=10)
    content = MDTextField()

    def __str__(self):
        return self.name
