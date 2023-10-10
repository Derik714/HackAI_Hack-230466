import requests #importing a python package for sending requests to the API server
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?" #Base URL is the URL that stays the same regardless of the variables that add up to it to make an API call
API_KEY ="ENTER_YOUR_API_KEY" #One such variable in this case is the API Key
def KtoCandF(temp): #Basic function to convert the Temperature obtained in Kelvin to Celsius and Farenheit(We have only used the celsius value in this project, you can use farenheit instead)
    Tc = temp-273.15
    Tf = Tc*(9/5)+32
    Tc=round(Tc,2)
    Tf=round(Tf,2)
    return Tc,Tf
def getTemp(City): #Function to make the API call
        url = BASE_URL + "appid="+API_KEY+"&q="+City #The other and final variable in this case is the City name
        response = requests.get(url).json() #Making a request to the API server and obtaining the response in JSON format
        TValue = str((KtoCandF(response['main']['temp']))[0]) #We have extracted the Celsius value by sending the response temperature value to KtoCanF(temp) function
        return TValue
