from django.db import models
from uuid import uuid4


class BaseSP(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	name = models.CharField(max_length=150)
	mfal = models.CharField(max_length=5)
	take_rate = models.FloatField()

	def __str__(self):
		return f'{self.name} - {self.mfal}'


class Serie(BaseSP):
	ponderacion = models.PositiveSmallIntegerField()


class Package(BaseSP):
	pass