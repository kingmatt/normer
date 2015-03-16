from django.db import models

class Subject(models.Model):
  var = 1

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

