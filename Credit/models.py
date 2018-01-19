from django.db import models

# Create your models here.
class Credit(models.Model):

    appId = models.PositiveIntegerField(db_index=True)
    userId = models.CharField(max_length=50, db_index=True)
    credit = models.IntegerField()

    class Meta:
        ordering = ('appId', 'credit')
        unique_together = ('appId', 'userId')
