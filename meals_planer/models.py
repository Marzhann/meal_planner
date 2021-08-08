from django.db import models

# Create your models here.
class Weekday(models.Model):
    """A weekday the user plan meal for"""
    name = models.CharField(max_length=50)

    def __str__(self):
        """Return a string representation of the model"""
        return self.name

class Meal(models.Model):
    """Meals planned by the user for the day"""
    weekday = models.ForeignKey(Weekday, on_delete=models.CASCADE)
    menu = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        if len(self.menu) > 50:
            return f'{self.menu[:50]}...'
        else:
            return self.menu            


