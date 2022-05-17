from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    # data = {'Kolkata_Cost': 1200, 'Mumbai_Cost': 1100, 'Dhaka_Cost': 1000}

    puneLocation = models.destination()
    puneLocation.name = 'Pune'
    puneLocation.description = 'IT Hub'
    puneLocation.price = '700'
    puneLocation.img = 'pune.png'
    puneLocation.offer = True

    hydrabadLocation = models.destination()
    hydrabadLocation.name = 'Hyderabad'
    hydrabadLocation.description = 'Sunrisers Hyderabad'
    hydrabadLocation.price = '900'
    hydrabadLocation.img = 'hyderabad.avif'
    hydrabadLocation.offer = False

    indoreLocation = models.destination()
    indoreLocation.name = 'Indore'
    indoreLocation.description = 'Middle Area'
    indoreLocation.price = '500'
    indoreLocation.img = 'indore.webp'
    indoreLocation.offer = False

    allDestinations = [puneLocation, hydrabadLocation, indoreLocation]

    # return render(request, 'index.html', data)
    return render(request, 'index.html', {'allDestinations': allDestinations})