from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    number_of_guests = models.IntegerField(db_index=True)
    booking_date = models.DateField(db_index=True)


class MenuItem(models.Model):
    title = models.CharField(max_length=255,db_index=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    inventory = models.IntegerField(db_index=True)

    def get_item(self):
        return f'{self.title} : {str(self.price)}'



