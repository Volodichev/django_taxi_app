from django.db import models
from datetime import date


class Brand(models.Model):
    """Brands"""
    name = models.CharField("Марка", max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class CarModel(models.Model):
    """Models"""
    brand = models.ForeignKey(to='Brand', verbose_name="Марка", on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField("Модель", max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"



class Car(models.Model):
    """Cars"""
    brand = models.ForeignKey(to='Brand', verbose_name="Марка", on_delete=models.SET_NULL, null=True, blank=False,
                              related_name="cars")
    model = models.ForeignKey(to='CarModel', verbose_name="Модель", on_delete=models.SET_NULL, null=True, blank=False,
                              related_name="cars")
    color = models.CharField(verbose_name="Цвет", max_length=50)
    registration_number = models.CharField(verbose_name="Регистрационный номер", db_index=True, max_length=15,
                                           unique=True)
    production_year = models.IntegerField(verbose_name="Год выпуска", default=1970)
    vin = models.CharField(verbose_name="Vin номер", unique=True, max_length=17)
    sts_number = models.CharField(verbose_name="Номер СТС (свидетельство о регистрации)", max_length=10)
    sts_date = models.DateField(verbose_name="Дата СТС", )

    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = "Транспорт"
        verbose_name_plural = "Транспорт"
