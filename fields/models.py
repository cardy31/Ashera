from django.db import models
import requests


class Field(models.Model):
    # Playing with location data
    latitude = 44.357998
    longtitude = -78.290432
    api_key = 'd763818ba9e0ade7ba4fc7cc9addd027'
    weatherUrl = "https://api.darksky.net/forecast/" + api_key + "/" + latitude.__str__() + "," + longtitude.__str__()

    r = requests.get(url=weatherUrl)
    data = r.json()
    # Convert to Celcius
    tempEnv = (data['currently']['temperature'] - 32) / 1.8
    humidEnv = data['currently']['humidity']
    rainProb = data['daily']['data'][0]['precipProbability']

    phone = models.CharField(max_length=25)
    field = models.CharField(max_length=256)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    # Data choices based on Fig. 2: http://ijcta.com/documents/volumes/vol6issue3/ijcta2015060303.pdf
    # Soil
    temp = models.DecimalField(decimal_places=3, max_digits=10, null=True)
    humidity = models.DecimalField(decimal_places=3, max_digits=10, null=True)
    nitrate = models.DecimalField(decimal_places=3, max_digits=10, null=True)
    phosphorus = models.DecimalField(decimal_places=3, max_digits=10, null=True)
    potassium = models.DecimalField(decimal_places=3, max_digits=10, null=True)
    pH = models.DecimalField(decimal_places=3, max_digits=10, null=True)
    # Environment
    light = models.CharField(default="dark", max_length=20)
    envTemp = models.DecimalField(decimal_places=3, max_digits=10, null=False, default=tempEnv)
    envHumidity = models.DecimalField(decimal_places=3, max_digits=10, null=False, default=humidEnv)
    precipProb = models.DecimalField(decimal_places=3, max_digits=5, null=False, default=rainProb)
    lastUpdate = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='fields')

    class Meta:
        ordering = ('id',)
