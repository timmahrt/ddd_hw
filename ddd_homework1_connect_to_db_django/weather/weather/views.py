import random

from django.shortcuts import render

from weather import domain


def index(request):
    return render(request, "index.html")


def new(request):
    weather = domain.recordWeather(random.uniform(-20, 40))
    return render(
        request, "new.html", {"temperature": weather.temperature, "date": weather.date}
    )


def list(request):
    weatherData = domain.getWeatherData()
    return render(request, "list.html", {"weather": weatherData})
