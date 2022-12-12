from django.db import models  # Infra layer?


class Weather(models.Model):
    temperature = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)


def recordWeather(temperature):
    return Weather.objects.create(temperature=temperature)


def getWeatherData():
    return Weather.objects.all()
