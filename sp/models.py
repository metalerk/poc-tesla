from django.db import models
from uuid import uuid4


class MFAL(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	name = models.CharField(max_length=150, unique=True)
	mfal_code = models.CharField(max_length=5, unique=True)


	def __str__(self):
		return f'{self.name} - {self.mfal_code}'


class BaseSP(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	name = models.CharField(max_length=150, unique=True)
	mfal = models.ManyToManyField(MFAL)
	take_rate = models.FloatField()

	def __str__(self):
		return f'{self.name} - {self.mfal}'


class Serie(BaseSP):
	ponderacion = models.PositiveSmallIntegerField()


class Package(BaseSP):
	pass
