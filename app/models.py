from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Image(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True)
  name = models.CharField(max_length=256, null=True, blank=True)
  image = models.ImageField(_('image'))

  def delete(self, *args, **kwargs):
        print (self.image)
        storage, path = self.image.storage, self.image.name
        storage.delete(path)
        return super().delete(*args, **kwargs)

