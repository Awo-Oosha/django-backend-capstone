from django.db import models

# Create your models here.
class Booking(models.Model):
  """Model definition for Booking."""

  # TODO: Define fields here
  name = models.CharField(max_length=255, db_index=True)
  no_of_guest = models.IntegerField()
  bookingDate = models.DateTimeField()

  class Meta:
    verbose_name = 'Booking'
    verbose_name_plural = 'Bookings'

  def __str__(self):
    """Unicode representation of Booking."""
    return self.name


class Menu(models.Model):
  """Model definition for Booking."""

  # TODO: Define fields here
  title = models.CharField(max_length=255, db_index=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  inventory = models.IntegerField()

  class Meta:
    verbose_name = 'Menu'
    verbose_name_plural = 'Menus'

  def __str__(self):
    """Unicode representation of Booking."""
    return f'{self.title} : {str(self.price)}'
  