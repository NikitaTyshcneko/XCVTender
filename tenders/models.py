from django.db import models

class Tender(models.Model):
    '''A representation of imported tender.'''
    tender_id = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=255)
    euro_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    @property
    def btc(self):
        return float(self.euro_value) * 0.000022

    def __str__(self):
        return f'#{self.pk} {self.name}'