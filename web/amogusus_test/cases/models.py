from django.db import models
from django.urls import reverse

from random import randint


class Case(models.Model):
    name = models.CharField(max_length=50)
    case_hash = models.DecimalField(
        default=randint(0, 100000), max_digits=10000, decimal_places=0
    )

    def get_absolute_url(self):
        return reverse("cases:case_detail", kwargs={"ref_id": self.id})
