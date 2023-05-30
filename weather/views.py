from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid = '52c9a5cf220ba183b3cbcdd7326de176'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    cities = City.objects.all()
    allcities = []
    
    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
        
    form = CityForm()
    
    for city in cities:
            res = requests.get(url.format(city.name)).json()
            city_info = {
                'city': city.name,
                'temp': res["main"]["temp"],
                'icon': res["weather"][0]["icon"]
            }
            allcities.append(city_info)
    
    context = {
        'allinfo': allcities,
        'form': form
    }
    
    return render(request, 'weather/index.html', context) 
