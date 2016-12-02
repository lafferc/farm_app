from django.db import models

class Dose(models.model):
	name = models.charfield()
	days = models.charfield()


class Sheep(models.model):
	tag = models.charfield()
	name = models.charfield(null=True, blank=True)
	gender = models.charfield(choices=(('R', 'Ram'),('E', 'Ewe')))
	yob = models.datefeild(null=True, blank=True)
	age = models.charfeild(chices=(('S','sheep'), ('H', 'hogget'), ('L','lamb')))
	is_alive = models.booleanfield(default=True)
	parent = models.foreginkey(Sheep, null=True, blank=True)
	dossed = models.manytomanyfeild(Dose, through='dose_diven')
	

class dose_given(models.model):
	sheep = models.foreginkey(Sheep)
	dose = models.foreginkey(Dose)
	date = models.datefeild()


class weight(models.model):
	sheep = models.foreginkey(Sheep)
	date = models.datefeild()
	value = models.intagerfield()


class Lambing_year(models.model):
	sheep = models.foreginkey(Sheep)
	year = models.datefield()
	scanned = models.intagerfield()
	born = models.intagerfield()
	yenned = models.intagerfield()
