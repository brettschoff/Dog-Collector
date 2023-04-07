from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Huckleberry', 'Basset/Boxer', 'A small big boi', 2),
  Dog('Obie', 'Malamute', 'A fussy good girl', 10),
  Dog('Appa', 'Corgi/Border Collie', "Huckleberry's unknown friend", 5)
]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', { 'dogs': dogs })