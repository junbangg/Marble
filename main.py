from City import City
#from Player import Player


#도시 배열
cityList = [City("Start"), City("Hawai"), City("Seoul"), City("Tokyo"), City("Paris"), City("Seattle"), City("New York"), City("Alaska"), City("Madrid"), City("Hong Kong")]

#Test Code
cityList[1].set_id(1)
cityList[5].set_id(2)
#지도 출력
mapString = ""
for c in cityList:
    temp = " => " + c.get_info()
    mapString += temp
print(mapString[4:])
