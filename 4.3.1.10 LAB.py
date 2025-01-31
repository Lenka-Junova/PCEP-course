# 4.3.1.10 LAB tasks - converting fuel consumption
mile_to_km = (1609.344)/1000
gallon_to_litre = 3.785411784

#x miles per 1 galon
#100 km per x litre

def liters_100km_to_miles_gallon(liters):
    result =(100/mile_to_km)/(liters/gallon_to_litre)
    return result

def miles_gallon_to_liters_100km(miles):
    result = ((gallon_to_litre)/(miles*mile_to_km))*100
    return result


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
