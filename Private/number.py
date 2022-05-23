# Get User Mobile Number input by this function  
def GetNumber():
    import pyautogui as gui
    numbers = gui.prompt('Enter number with country code Ex: +91')
    return numbers