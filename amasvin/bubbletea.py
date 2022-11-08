from drink import Drink #나와 같은 폴더에 있는 drink.py 파일에서 Drink 가져오자


class Bubbletea(Drink):
    #클래스변수
    _PEARLS = ('타피오카', '코코', '알로에', '곤약')
    def __init__(self, name, price):
        super().__init__(name, price)   #부모의 생성자 호출하자
        self.pearl = 0  #0: 타피오카, 1: 코코, 2: 알로에, 3: 곤약
        
    def __str__(self):
        return super().__str__() \
               + f'\t펄: {Bubbletea._PEARLS[self.pearl]} 펄'
    def set_pearl(self):
        #펄 종류 출력하자 1. ~, 2. ~
        for index, pearl in enumerate(Bubbletea._PEARLS):
            print(f'{index + 1}. {pearl} 펄')    #1. 타피오카 펄, ...
        #사용자에게 입력받자
        pearl = input("펄을 선택하세요: ")
        #그냥 엔터면 기본값, 숫자 입력받은 것은 index로 변경하자
        # if pearl == '':
        #     self.pearl = 0
        # else:
        #     self.pearl = int(pearl) - 1
        self.pearl = 0 if pearl == '' else int(pearl) - 1
    def order(self):
        #부모 order() 호출하자
        super().order() #컵사이즈, 당도, 얼음량을 설정하자
        #내 set_pearl() 호출하자
        self.set_pearl()

버블티1 = Bubbletea('타로버블티', 3700)
버블티1.order()
print(버블티1)

