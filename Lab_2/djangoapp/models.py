from django.db import models

class Measurement(models.Model):
    value = models.CharField(max_length=50)
    description = models.CharField( max_length=250, blank=True, null=True)
    time = models.DateTimeField("date and time")

    def __str__(self):
        return self.value

