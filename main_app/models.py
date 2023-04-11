from django.db import models
from django.urls import reverse


class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})
    
    def __str__(self):
        return f"{self.name}"
    
TOYS = (
    ('B', 'Bone'),
    ('S', 'Stuffed Animal'),
    ('T', 'Tennis Ball'),
)
class Toy(models.Model):
    date = models.DateField()
    toy_name = models.CharField(
        'Toy',
        max_length=1,
        choices=TOYS,
        default=TOYS[0][0]
    )

    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_toy_name_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']