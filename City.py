'''
    멤버변수
        -name : 도시 이름
        -id : 차지하고 있는 플레이어의 숫자. 0 => 차지x , 1=> 플레이어 1, 2=> 플레이어 2
    메소드
        -get_id():
            => 도시를 차지하고있는 플레이어 id 반환(int)
        -set_id():
            @Params:
                -playerID (도시를 차지하는 플레이어의 id)
        -get_info():
            => 정보 출력
'''


class City:

    def __init__(self, name):
        self.name = name
        self.owner = 0

    def get_owner(self):
        return self.owner

    def get_owner_print(self):
        if self.owner == -1:
            return '(출발지)'
        elif self.owner == 0:
            return '(주인 없음)'
        else:
            return '(Player{} 소유지)'.format(self.owner)

    def set_owner(self, playerID):
        self.owner = playerID

    def get_info(self):
        if self.owner <= 0:
            return self.name
        else:
            return self.name + '(' + str(self.owner) + ')'


