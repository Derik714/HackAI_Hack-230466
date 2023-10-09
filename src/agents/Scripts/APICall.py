import requests
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY ="d5d110b46dc686de57c9168f304a894d"
def KtoCandF(temp):
    Tc = temp-273.15
    Tf = Tc*(9/5)+32
    Tc=round(Tc,2)
    Tf=round(Tf,2)
    return Tc,Tf
def getTemp(City):
        url = BASE_URL + "appid="+API_KEY+"&q="+City
        response = requests.get(url).json()
        TValue = str((KtoCandF(response['main']['temp']))[0])
        return TValue