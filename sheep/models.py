from django.db import models
import datetime


def current_year():
    return datetime.datetime.today().year


YEAR_CHOICES = [(r, r) for r in range(2000, current_year() + 1)]


class Dose(models.Model):
    name = models.CharField(max_length=50)
    days = models.IntegerField()
    def __str__(self):
        return self.name


class Sheep(models.Model):
    tag = models.CharField(max_length=50)
    name = models.CharField(null=True, blank=True, max_length=50)
    gender = models.CharField(choices=(('R', 'Ram'),('E', 'Ewe')), max_length=50)
    yob = models.IntegerField(null=True, blank=True, choices=YEAR_CHOICES)
    age = models.CharField(choices=(('S','sheep'), ('H', 'hogget'), ('L','lamb')), max_length=50)
    is_alive = models.BooleanField(default=True)
    parent = models.ForeignKey("Sheep", null=True, blank=True)
    dossed = models.ManyToManyField(Dose, through='DoseGiven')
    comment = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        if self.name:
            return "%s (%s)" % (self.tag, self.name)
        return str(self.tag)

    class Meta:
        verbose_name_plural = "Sheep"
    

class DoseGiven(models.Model):
    sheep = models.ForeignKey(Sheep)
    dose = models.ForeignKey(Dose)
    date = models.DateField(default=datetime.date.today)


class Weight(models.Model):
    sheep = models.ForeignKey(Sheep)
    date = models.DateField()
    value = models.IntegerField()
    def __str__(self):
        return "%sKg" % self.value


class LambingYear(models.Model):
    sheep = models.ForeignKey(Sheep)
    year = models.IntegerField(choices=YEAR_CHOICES, default=current_year)
    scanned = models.IntegerField()
    born = models.IntegerField()
    yenned = models.IntegerField()
    def __str__(self):
        return "%s (%s)" % (self.year, self.sheep) 
