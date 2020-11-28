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
        self.id = 0

    def get_id(self):
        return self.id

    def set_id(self, playerID):
        self.id = playerID


    def get_info(self):
        if self.id == 0:
            return self.name
        else:
            temp = self.name + "(" + str(self.id) + ")"
            return temp
            #print("{}({})".format(self.name, self.id))


