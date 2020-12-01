from City import City
from Player import Player
# 주사위 돌리는 플레이어(x) / 상대플레이어(y) / 주사위 나온 수(z)
def turn (x,y,z):
    print('{} 도착 {}'.format(cityList[z].name, cityList[z].get_owner_print()))    
    # 도시가 비어있는 경우
    if cityList[z].get_owner() == 0:
        if x.buy_city(x.get_id(), cityList[z]):
            cityList[z].set_owner(x.get_id())
        else:
            print('잔고가 부족하여 구입할 수 없다.')
    # 도시가 플레이어 y의 소유인 경우, 플레이어y의 자금 500원추가
    elif cityList[z].get_owner() == y.get_id():
        if x.pay_fee(x.get_id()):
            y.balance += 500
        # 도시가 플레이어 2의 소유이지만 자금이 없는 경우
        else:
            print('player',y.get_id(),'가 승리하였습니다.')
            global player_win
            player_win = 1
    return x


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
#플레이어 승리 플래그
player_win = 0
for i in range(0, 30):
    input("턴을 진행하려면 Enter를 누르세요:")
    # 지도 출력
    print_map(i)
    print("DICE ROLL!")

    # Player 1 주사위
    p1 = player1.move()
    # turn 함수
    turn(player1,player2,p1)
    #자금이 없어서 상대방이 이긴 경우
    if player_win == 1:
        break
    # 플레이어1의 위치와 남은 금액

    # Player 2 (코드는 동일)
    p2 = player2.move()
    #turn함수
    turn(player2,player1,player2.move())
    if player_win == 1:
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
