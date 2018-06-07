def dateValidation(checkIn, checkOut):
    if(checkOut>checkIn):
        return 1
    if(checkIn==checkOut):
        return 2
    return 3

def filterCity(city):
    if(city=="CO-MDE"):
        filterCity = 'Medellin'
    elif(city=="CO-BOG"):
        filterCity = 'Bogota'
    elif(city=="CO-CLO"):
        filterCity = 'Cali'
    elif(city=="CO-SMR"):
        filterCity = 'Santa Marta'
    elif(city=="CO-CTG"):
        filterCity = 'Cartagena'
    elif(city==""):
        filterCity = 'void'
    else:
        filterCity = 'invalid'
    return filterCity

def filterType(type):
    if(type=="1"):
        filterType = "Apartamento"
    elif(type=="2"):
        filterType = "Casa"
    elif(type=="3"):
        filterType = "Luxury"
    elif(type==""):
        filterType = "void"
    else:
        filterType = "invalid"
    return filterType
