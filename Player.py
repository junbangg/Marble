from random import randint


class Player:
    def __init__(self, id, balance=4000):
        self.id = id
        self.balance = balance
        self.location = 0

    # 일단 만들어놓은 정보 조회용 함수
    def get_id(self):
        return self.id

    def get_balance(self):
        return self.balance

    def get_location(self):
        return self.location

    # 주사위 던져서 몇 나왔는지 프린트, 이동, 위치 반환
    def move(self):
        ri = randint(1, 6)
        print("{}번 플레이어의 주사위가 {}이 나왔다.".format(self.id, ri))
        self.location = (self.location + ri) % 10
        return self.location

    # 도시를 살 잔고가 있는지 확인, 있다면 사고 True, 없다면 False 리턴
    def buy_city(self):
        if self.balance >= 300:
            self.balance -= 300
            return True
        else:
            return False

    # 통행료를 낼 잔고가 있는지 확인, 있다면 사고 True, 없다면 False 리턴
    def pay_fee(self):
        if self.balance >= 500:
            self.balance -= 500
            return True
        else:
            return False
