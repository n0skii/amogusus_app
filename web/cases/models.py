from django.db import models
from django.urls import reverse

from random import randint


class Case(models.Model):
    name = models.CharField(max_length=10)
    case_hash = models.DecimalField(
        default=randint(0, 10000),
        max_digits=100,
        decimal_places=0,
    )

    def get_absolute_url(self):
        return reverse("cases:case_detail", kwargs={"ref_id": self.id})
