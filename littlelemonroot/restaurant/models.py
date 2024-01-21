from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField(default=2)
    booking_date = models.DateTimeField()

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __str__(self) -> str:
        return f'{self.name} for {self.no_of_guests} guests on {self.booking_date}'


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu Items"

    def __str__(self) -> str:
        return f"{self.title} : {str(self.price)}"
