    # making html file for exact location 
def generatemap(lat, lng, location):
    import folium
    import pyautogui as graphicaluserinterface
    mymap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(mymap)
    saved_map_html_File_Name = graphicaluserinterface.prompt('Enter File Name To Save Location Map :: Without .html extension')+'.html'
    mymap.save(saved_map_html_File_Name)