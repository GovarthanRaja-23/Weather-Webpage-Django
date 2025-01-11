from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        try:
            res = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=e9cea3bf6832a69a1055df03421510de').read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
                "temp": str(round(json_data['main']['temp'] - 273.15, 2)) + ' °C',
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
            }
        except Exception:
            data = {"error": "City not found. Please try again."}

    else:
        city=''
        data={}
    return render(request,'index.html',{'city':city,'data':data})