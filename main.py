from City import City
from Player import Player


# 지도 출력
def print_map(i):
    mapString = ""
    for c in cityList:
        temp = " => " + c.get_info()
        mapString += temp
    print("==========================================================TURN {}=========================================================\n".format(i+1))
    print("\t------------------------------------------------------------------------------------------------------------------------")
    print("\t" + mapString[4:])
    print("\t----------------------------------------------------------------------------------------------------------------------\n")


# 도시 배열
cityList = [City("Start"), City("Hawai"), City("Seoul"), City("Tokyo"), City("Paris"), City("Seattle"),
            City("New York"), City("Alaska"), City("Madrid"), City("Hong Kong")]
# Start에 도착하면 아무 동작도 하지 않기 위함
cityList[0].set_owner(-1)


# 플레이어 생성
player1 = Player(1)
player2 = Player(2)
cnt = 0

for i in range(0, 30):
    input("턴을 진행하려면 Enter를 누르세요:")
    # 지도 출력
    print_map(i)
    print("DICE ROLL!")

    # Player 1 주사위
    p1 = player1.move()
    print('{} 도착 {}'.format(cityList[p1].name, cityList[p1].get_owner_print()))
    # 도시가 비어있는 경우
    if cityList[p1].get_owner() == 0:
        if player1.buy_city(1, cityList[p1]):
            cityList[p1].set_owner(1)
        else:
            print('잔고가 부족하여 구입할 수 없다.')
    # 도시가 플레이어 2의 소유인 경우, 플레이어2의 자금 500원추가
    elif cityList[p1].get_owner() == 2:
        if player1.pay_fee(1):
            player2.balance += 500
        # 도시가 플레이어 2의 소유이지만 자금이 없는 경우
        else:
            print('Player 2가 승리하였습니다.')
            break
    # 플레이어1의 위치와 남은 금액

    # Player 2 (코드는 동일)
    p2 = player2.move()
    print('{} 도착 {}'.format(cityList[p2].name, cityList[p2].get_owner_print()))
    if cityList[p2].get_owner() == 0:
        if player2.buy_city(2, cityList[p2]):
            cityList[p2].set_owner(2)
        else:
            print('잔고가 부족하여 구입할 수 없다.')
    elif cityList[p2].get_owner() == 1:
        if player2.pay_fee(2):
            player1.balance += 500
        else:
            print('Player 1이 승리하였습니다.')
            break

    print('\nPlayer 1 의 현재위치 :', cityList[p1].name)
    print('Player 1 남은 금액 : {}'.format(player1.balance))
    print('\nPlayer 2 의 현재위치 :', cityList[p2].name)
    print('Player 2 남은 금액 : {}\n'.format(player2.balance))
    cnt += 1
    print("=======================================================================================================================\n")

if cnt == 30:
    print('30턴이 모두 진행되어 게임을 중지합니다.')
print("GAME END")
