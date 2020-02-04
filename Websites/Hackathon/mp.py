from urllib import request
import json
import requests
from bs4 import BeautifulSoup
import folium
from folium.plugins import MarkerCluster

cityCount = dict()
coordinateString = ""

def main(jt):
    print("main " + jt)

    latlon = webCrawler("https://www.indeed.com/jobs?q="+ jt +"&l=")
    print("https://www.indeed.com/jobs?q="+ jt +"&l=")
    
    # m = folium.Map(location=[43.2676254,-77.5311657], zoom_start=3)
    # mc = MarkerCluster()
    appendF = open("coordinates.txt", "w")
    for k in latlon:
        lat = float(latlon[k][0])
        lng = float(latlon[k][1])


        # print(str(lat)+" "+str(lng)+"\n")
        global coordinateString 
        coordinateString = coordinateString + str(lat)+" "+str(lng)+"\n"
        print("cstring = " + coordinateString)
        appendF.write(str(lat)+" "+str(lng)+"\n")

        # for x in range(cityCount.get(k)):
        #     #plot 
        #     mc.add_child(folium.Marker(location=[lat, lng], popup=""))
    # m.add_child(mc)    
    # m.save(r'C:\Users\Nico\OneDrive\Documents\SEMESTER 5\WEB DEV TA\Hackathon\templates\map.html')    
    coordinateString = coordinateString[:-1] 
    return

# def mapPlotting(city, state): correct
#     api_token = 'f5164adc5c1945b296d441bc9182d6e9'
#     api_base = 'http://api.opencagedata.com/geocode/v1/json?key='
#     api_location = '&q=' + city + '+' + state + '&pretty=1'

#     api_url = api_base + api_token + api_location

#     response = requests.get(api_url)

#     if response.status_code == 200:
#         return json.loads(response.content.decode('utf-8'))
#     else:
#         return None

def mapPlotting(location):
    # file = open("cityData.txt", "w+")
    # cities = open("cities.txt", "r")
    # cityList = cities.readlines()
    # for x in cityList:
        y = location.split(',')
        statePlusZip = y[1].split()
        city  = y[0]
        state = statePlusZip[0]
        if len(statePlusZip) > 1:
            zipCode = statePlusZip[1]
            data = open("data.txt", "r")
            dataList = data.readlines()
            for row in dataList:
                testZip = row.split(',')[0]
                if testZip == zipCode: 
                    lat = row.split(',')[3]
                    lng = row.split(',')[4]
                    L = [str(lat) + ' ', str(lng)]
                    return L
                    
        else:
            data = open("data.txt", "r")
            dataList = data.readlines()
            for row in dataList:
                if city == row.split(',')[1] and state == row.split(',')[2]:
                    lat = row.split(',')[3]
                    lng = row.split(',')[4]
                    L = [str(lat) + ' ', str(lng)]
                    return L
                

def webCrawler(url): #data scrapping
    page = 1
    maxPage = 2
    while page < maxPage:
        requestResponseText = requests.get(url).text
        soup = BeautifulSoup(requestResponseText, features="lxml")
        coords = []
        counter = 0
        for element in soup.find_all('div', {'class' : 'location accessible-contrast-color-location'}):
           coords[counter] = (mapPlotting(element.text))
           counter = counter + 1
           print(mapPlotting(element.text))
           
            # response = element.text.split(',') 

            # city  = response[0]
            # state = response[1].split()[0]
            # location = city+" "+state
            
            # if cityCount.get(location) == None:
            #     cityCount[location] = 1
            # else:
            #     cityCount[location] = cityCount.get(location)+1

        page +=1
    return coords

def appendFile(file, text):
    appendF = open(file, "a")
    appendF.write(text)
    appendF.close()