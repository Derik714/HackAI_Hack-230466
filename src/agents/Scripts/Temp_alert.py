def verify_temp(Tmax, Tmin, Ctemp):
    if(Ctemp > Tmax):
        return "Current Temperature is, "+str(Ctemp)+"° Celsius which is greater than the maximum temperature"
    elif(Ctemp < Tmin):
        return "Current Temperature is, "+str(Ctemp)+"° Celsius which is lesser than the minimum temperature"
    else:
        return str(Ctemp)+"° Celsius is the current temperature, which is within the entered range" 