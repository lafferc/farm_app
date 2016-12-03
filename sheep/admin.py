from django.contrib import admin
from sheep.models import Dose, Sheep, DoseGiven, Weight, LambingYear


class DoseGivenInLine(admin.TabularInline):
    model = DoseGiven
    extra = 0


class WeightInLine(admin.TabularInline):
    model = Weight
    extra = 0


class LambingYearInline(admin.TabularInline):
    model = LambingYear
    extra = 0

 
class SheepAdmin(admin.ModelAdmin):
    inlines = ( DoseGivenInLine, WeightInLine, LambingYearInline)


admin.site.register(Dose)
admin.site.register(Sheep, SheepAdmin)
admin.site.register(Weight)
admin.site.register(LambingYear)

