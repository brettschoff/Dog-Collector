from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from django.http import HttpResponse
from .models import Dog
from .forms import ToyForm

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', { 'dogs': dogs })

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id = dog_id)
    toy_form = ToyForm()
    return render(request, 'dogs/detail.html', {'dog': dog, 'toy_form': toy_form})

def add_toy(request, dog_id):
    form = ToyForm(request.POST)
    if form.is_valid():
        new_toy = form.save(commit=False)
        new_toy.dog_id = dog_id
        new_toy.save()
    return redirect('detail', dog_id=dog_id)