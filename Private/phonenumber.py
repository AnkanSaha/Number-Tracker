import phonenumbers
# get phonenumbers exact location with map by this function 
def main():
    # importing all modules and functions from another file in this section 
    from Private.number import GetNumber
    import phonenumbers
    from phonenumbers import geocoder
    numbers = GetNumber()
    # for getting country name
    pepnumber = phonenumbers.parse(numbers)
    location = geocoder.description_for_number(pepnumber,'en')
    print(pepnumber)
    print(location)
    # for getting carrier name
    from phonenumbers import carrier
    service_pro = phonenumbers.parse(numbers)
    carrierName = carrier.name_for_number(service_pro, 'en')
    print(carrierName)
    # for getting exact location  by latitiude and longtitude
    import opencage
    import pyautogui as GUI
    import sys
    from Private.generatemap import generatemap
    from opencage.geocoder import OpenCageGeocode
    tempkey = open('Private/opencageapi.txt', 'r')
    key = tempkey.read()
    geocoder = OpenCageGeocode(key)
    query = str(location)
    results = geocoder.geocode(query)
    print(results)
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    from Private.mapconfirmation import mapconfirmation
    confirmed = mapconfirmation(lat, lng)
    if confirmed == 'validated':
        generatemap(lat, lng, location)
    elif confirmed == 'rejected':
        GUI.alert('Thank You For Using Our Service')
        sys.exit()

