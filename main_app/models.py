from django.db import models
from django.urls import reverse

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})
    
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})
    
    def __str__(self):
        return f"{self.name}"
    
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)
class Feeding(models.Model):
    date = models.DateField('feeding date')
    # meal will be represented by a single letter (B)reakfast, (L)unch, (D)inner
    # # we set the default value for meal to 'B
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    # Create a cat_id FK
    # models.CASCADE, if we delete a cat, delete its feedings as well
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        # get_meal_display is automatically generated,
        # on inputs that have choices parameter, see meal
        return f"{self.get_meal_display()} on {self.date}"
