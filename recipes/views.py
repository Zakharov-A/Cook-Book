from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': recipes})