from City import City
from Player import Player


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

#플레이어 설정
player1 = Player(1)
player2 = Player(2)

for i in range (0,30) :
    #플레이어1
    p1 = player1.move()
    #위치가 start인 경우
    if cityList[p1] == cityList[0] :
        cityList[0].set_id(1)
    #도시가 비어있고, 구매할 자금이 있는 경우
    elif cityList[p1].get_id() == 0 and player1.buy_city() == True :
        cityList[p1].set_id(1)
    #도시가 비었지만, 자금이 없는 경우
    elif cityList[p1].get_id() == 0 and player1.buy_city() == False :
        continue
    #도시가 플레이어1의 소유인 경우
    elif cityList[p1].get_id == 1 :
        continue
    #도시가 플레이어 2의 소유인 경우, 플레이어2의 자금 500원추가
    elif cityList[p1].get_id() == 2 and player1.pay_fee() == True :
        cityList[p1].set_id(1)
        player2.balance = player2.balance + 500
    #도시가 플레이어 2의 소유이지만 자금이 없는 경우
    elif cityList[p1].get_id() == 2 and player1.pay_fee() == False :
        print('플레이어2가 승리하였습니다.')
        break
    #자금이 다 떨어진 경우
    elif player1.balance < 1 :
        print('플레이어2가 승리하였습니다.')
        break
    #플레이어1의 위치와 남은 금액
    print('플레이어1의 현재위치 :', cityList[p1].get_info())
    print('플레이어1 남은금액 : ',player1.balance)
    #플레이어2 ( 코드는 동일)
    p2 = player2.move()
    if cityList[p1] == cityList[0] :
        cityList[0].set_id(1)
    elif cityList[p2].get_id() == 0 and player2.buy_city() == True :
        cityList[p2].set_id(2)
    elif cityList[p2].get_id() == 0 and player2.buy_city() == False :
        continue
    elif cityList[p2].get_id() == 2 :
        continue
    elif cityList[p2].get_id() == 1 and player2.pay_fee() == True :
        cityList[p2].set_id(2)
        player1.balance = player1.balance + 500
    elif cityList[p2].get_id() == 1 and player2.pay_fee() == False :
        print('플레이어1이 승리하였습니다.')
        break
    elif player2.balance < 1 :
        print('플레이어1이 승리하였습니다.')
        break
    print('플레이어2의 현재위치 :', cityList[p2].get_info())
    print('플레이어2 남은금액 : ',player2.balance)
    #도시 소유자 표시
    mapString = ""
    for c in cityList:
        temp = " => " + c.get_info()
        mapString += temp
    print(mapString[4:])
