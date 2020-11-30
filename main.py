from City import City
from Player import Player


#도시 배열
cityList = [City("Start"), City("Hawai"), City("Seoul"), City("Tokyo"), City("Paris"), City("Seattle"), City("New York"), City("Alaska"), City("Madrid"), City("Hong Kong")]

#지도 출력
def print_map(i):
    mapString = ""
    for c in cityList:
        temp = " => " + c.get_info()
        mapString += temp
    print("==========================================================TURN {}=========================================================\n".format(i))
    print("\t------------------------------------------------------------------------------------------------------------------------")
    print("\t" + mapString[4:])
    print("\t----------------------------------------------------------------------------------------------------------------------\n")

#플레이어 설정
player1 = Player(1)
player2 = Player(2)

for i in range(0, 30):
    input("Enter를 누르세요:")
    #지도 출력
    print_map(i)
    #플레이어1
    p1 = player1.move()
    #위치가 start인 경우
    if cityList[p1] == cityList[0]:
        cityList[0].set_id(1)
    #도시가 비어있고, 구매할 자금이 있는 경우
    elif cityList[p1].get_id() == 0 and player1.buy_city() == True:
        cityList[p1].set_id(1)
    #도시가 플레이어 2의 소유인 경우, 플레이어2의 자금 500원추가
    elif cityList[p1].get_id() == 2 and player1.pay_fee() == True:
        cityList[p1].set_id(1)
        player2.balance += 500
    #도시가 플레이어 2의 소유이지만 자금이 없는 경우
    elif cityList[p1].get_id() == 2 and player1.pay_fee() == False:
        print('Player 2가 승리하였습니다.')
        break
    #자금이 다 떨어진 경우
    elif player1.balance == 0: #<1
        print('Player 2 가 승리하였습니다.')
        break
    #플레이어1의 위치와 남은 금액

#value_if_true if condition else value_if_false
    print('Player 1 의 현재위치 :', cityList[p1].get_info() if cityList[p1].get_info() == "Start" else cityList[p1].get_info()[:-3])
    print('Player 1 남은 금액 : {}\n'.format(player1.balance))
    #플레이어2 ( 코드는 동일)
    p2 = player2.move()
    if cityList[p1] == cityList[0]:
        cityList[0].set_id(1)
    elif cityList[p2].get_id() == 0 and player2.buy_city() == True:
        cityList[p2].set_id(2)
    elif cityList[p2].get_id() == 1 and player2.pay_fee() == True:
        cityList[p2].set_id(2)
        player1.balance += 500
    elif cityList[p2].get_id() == 1 and player2.pay_fee() == False:
        print('Player 1 이 승리하였습니다.')
        break
    elif player2.balance == 0:
        print('Player 2이 승리하였습니다.')
        break

    print('Player 2 의 현재위치 :', cityList[p2].get_info() if cityList[p2].get_info() == "Start" else cityList[p2].get_info()[:-3])
    print('Player 2 남은 금액 : {}\n'.format(player2.balance))
    print("=======================================================================================================================\n")


print("GAME END")
