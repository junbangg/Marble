from City import City
from Player import Player


# 주사위 돌리는 플레이어(player) / 상대플레이어(opponent) / 주사위 나온 수(dice)
def turn(player, opponent, dice):
    print('{} 도착 {}'.format(cityList[dice].name, cityList[dice].get_owner_print()))
    # 도시가 비어있는 경우
    if cityList[dice].get_owner() == 0:
        if player.buy_city(player.id, cityList[dice]):
            cityList[dice].set_owner(player.id)
        else:
            print('잔고가 부족하여 구입할 수 없다.')
    # 도시가 상대의 소유인 경우, 상대의 자금 500원추가
    elif cityList[dice].get_owner() == opponent.id:
        if player.pay_fee(player.id):
            opponent.balance += 500
        # 도시가 상대의 소유이지만 자금이 없는 경우
        else:
            print('잔고가 부족하여 통행료를 낼 수 없다.')
            print('player', opponent.id, '이(가) 승리하였습니다.')
            global player_win
            player_win = 1
    return player


# 지도 출력
def print_map(n, p1, p2):
    mapString = ""
    for c in cityList:
        temp = " => " + c.get_info()
        mapString += temp
        if p1.location == cityList.index(c):
            mapString += '[1]'
        if p2.location == cityList.index(c):
            mapString += '[2]'
    print("========================================================= TURN {} ==============================================================\n".format(n + 1))
    print("\t------------------------------------------------------------------------------------------------------------------------")
    print("\t" + mapString[4:])
    print("\t------------------------------------------------------------------------------------------------------------------------")
    #print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t(): 소유, []: 위치")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ( 소유), [ 위치]")


# 도시 배열
cityList = [City("Start"), City("Hawaii"), City("Seoul"), City("Tokyo"), City("Paris"), City("Seattle"),
            City("New York"), City("Alaska"), City("Madrid"), City("Hong Kong")]
# Start 에 도착하면 아무 동작도 하지 않기 위함
cityList[0].set_owner(-1)


# 플레이어 생성
player1 = Player(1)
player2 = Player(2)
cnt = 0
player_win = 0
for i in range(0, 30):
    input("턴을 진행하려면 Enter를 누르세요:")
    # 지도 출력
    print_map(i, player1, player2)
    print("DICE ROLL!")

    turn(player1, player2, player1.move())
    if player_win == 1:
        break

    turn(player2, player1, player2.move())
    if player_win == 1:
        break

    player1.print_current_state(cityList)
    player2.print_current_state(cityList)
    cnt += 1
    print("==============================================================================================================================\n")

if cnt == 30:
    print('30턴이 모두 진행되어 게임을 중지합니다.')
print("GAME END")
