from django.db import models
from datetime import datetime, timedelta

# Probably unnecessary, but I don't want to look this up and
# might need to change this in a minute
def default_create_time():
  return datetime.now()

class Subject(models.Model):
  created_at = models.DateTimeField(default=default_create_time)
  ip_address = models.GenericIPAddressField(null=True)

class Question(models.Model):
  # Images are now static files because fuck django
  image = models.IntegerField()
  subject = models.ForeignKey(Subject)

  # Actual question fields
  # Should rank 1 to 5

  name = models.CharField(max_length=50)
       
  recognizability = models.IntegerField()

  familiarity = models.IntegerField()

  pleasantness = models.IntegerField()

  complexity = models.IntegerField()

  memorability = models.IntegerField()

