from django.db import models

# Create your models here.
class CheckIn(models.Model):

    appId = models.PositiveIntegerField(db_index=True)
    userId = models.CharField(max_length=50, db_index=True)
    datetime = models.DateTimeField()

    class Meta:
        ordering = ('appId', 'datetime')
