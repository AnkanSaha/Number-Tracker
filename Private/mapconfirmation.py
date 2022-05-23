def mapconfirmation(latitude, longitude):
    import pyautogui as GUI
    import sys
    confirmed = 'rejected'
    confirmation = GUI.confirm("Your latitude is : "+str(latitude)+"  &  Longitude is : "+str(longitude), buttons=['Save HTML Map', 'Exit Now'])
    if confirmation == 'Save HTML Map':
        confirmed = 'validated'
    elif confirmation == 'Exit Now':
        pass
    return confirmed