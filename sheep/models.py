from django.db import models

class Dose(models.Model):
	name = models.CharField()
	days = models.CharField()


class Sheep(models.Model):
	tag = models.CharField()
	name = models.CharField(null=True, blank=True)
	gender = models.CharField(choices=(('R', 'Ram'),('E', 'Ewe')))
	yob = models.DateField(null=True, blank=True)
	age = models.CharField(choices=(('S','sheep'), ('H', 'hogget'), ('L','lamb')))
	is_alive = models.BooleanField(default=True)
	parent = models.ForeignKey("Sheep", null=True, blank=True)
	dossed = models.ManyToManyField(Dose, through='dose_diven')
    comment = models.CharField(null=True, blank=True)
	

class dose_given(models.Model):
	sheep = models.ForeignKey(Sheep)
	dose = models.ForeignKey(Dose)
	date = models.DateField()


class weight(models.Model):
	sheep = models.ForeignKey(Sheep)
	date = models.DateField()
	value = models.IntegerField()


class Lambing_year(models.Model):
	sheep = models.ForeignKey(Sheep)
	year = models.DateField()
	scanned = models.IntegerField()
	born = models.IntegerField()
	yenned = models.IntegerField()
