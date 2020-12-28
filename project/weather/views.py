import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1b41d3b4c7d3f941b1978fd084362505'
    
    err_msg = ''
    message = ''
    message_class = ''

    if request.method == 'POST':
        
        form = CityForm(request.POST)
        
        if form.is_valid():
            new_city = form.cleaned_data['name']
            r = requests.get(url.format(new_city)).json()
            
            if r['cod'] == 200:
                form.save()
            else:
                err_msg = ('Invalid city name')
            
        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'Weather list updated'
            message_class = 'is-primary'
        
       
    form = CityForm()
    
    cities = City.objects.all()
    
    weather_data = []
    
    for city in cities:
        
        r = requests.get(url.format(city)).json()
        
        city_weather = {
            'city': r['name'],
            'temperature': r['main']['temp'] ,
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        
        weather_data.append(city_weather)

    context = {
        'weather_data': weather_data, 
        'form': form,
        'message': message,
        'message_class': message_class,
    }
    
    return render(request,'weather\index.html', context)


def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    
    return redirect('index')
    
 
    