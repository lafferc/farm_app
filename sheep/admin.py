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
    list_display = ("__str__", "gender", "age", "is_alive")
    inlines = ( DoseGivenInLine, WeightInLine, LambingYearInline)
    list_filter = ( "gender", "age", "is_alive")


class DoseAdmin(admin.ModelAdmin):
    list_display = ("name", "days")


class WeightAdmin(admin.ModelAdmin):
    list_display = ("sheep", "date", "value")
    list_filter = (
        ('sheep', admin.RelatedOnlyFieldListFilter),
    )


class LambingYearAdmin(admin.ModelAdmin):
    list_display = ("sheep", "year", "scanned", "born", "yenned")
    list_filter = (
        "year",
        ('sheep', admin.RelatedOnlyFieldListFilter),
    )


admin.site.register(Dose, DoseAdmin)
admin.site.register(Sheep, SheepAdmin)
admin.site.register(Weight, WeightAdmin)
admin.site.register(LambingYear, LambingYearAdmin)
