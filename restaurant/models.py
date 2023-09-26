from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=127, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=127, unique=True)
    weight = models.DecimalField(max_digits=5, decimal_places=3)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}, {self.price}"


class Menu(models.Model):
    date = models.DateField(auto_now_add=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish)

    class Meta:
        unique_together = ("date", "restaurant")

    def __str__(self):
        return self.dishes
