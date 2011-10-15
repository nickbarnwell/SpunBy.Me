from django.db import models
from common.models import *
import datetime
# Create your models here.

class Party(models.Model):
  name = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True, blank=False)
  queue = models.OneToOneField(SongQueue, blank=False, on_delete=models.CASCADE)
  @property
  def expired(self):
    return datetime.datetime.now() >= self.created_at+datetime.timedelta(24)
 
 # def __init__(self, *args, **kwargs):
 #   super(Party, self).__init__(*args, **kwargs)
 #   self.queue = Queue(party=self)
