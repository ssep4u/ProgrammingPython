from copy import copy

from coffee import Coffee   #coffee: 모듈(.py), Coffee: 클래스
from bubbletea import Bubbletea


class Order:
    def __init__(self):
        self.menu = []  #메뉴판
        self.init_menu()    #메뉴판 초기화
        
        self.order_menu = []     #주문한 음료수 리스트

    def __str__(self):
        #self.order_menu에서 drink 하나씩 꺼내서 출력하자
        # 총 주문금액 출력하자

        return '\n'.join(str(drink) for drink in self.order_menu)

    def init_menu(self):    #메뉴판 초기화
        new_menu = Bubbletea("하동녹차오레오", 4500)
        self.menu.append(new_menu)
        new_menu = Coffee("카페 모카", 3000)
        self.menu.append(new_menu)
        new_menu = Bubbletea("라즈베리소다", 2900)
        self.menu.append(new_menu)

    def order(self):
        #반복
        while True:
            self.show_menu()    #메뉴판 보여주자
            #음료수 고르자(사용자 입력받자)
            choice = input("원하는 음료수를 고르세요(엔터치면 끝): ")
            #엔터치면 끝
            if choice == '':
                break
            #새로운 음료수로 생성하고, 옵션들 주문받자
            new_drink = copy(self.menu[int(choice) - 1])
                        #메뉴 그대로 가져오면, 옵션에 따라 메뉴가 바뀌어있음
                        #메뉴는 기본으로 놔두고, 복사해와서 그것의 옵션을 바꾸자
            new_drink.order()
            # print(new_drink)
            #주문한 음료수 리스트에 새로운 음료수 추가하자
            self.order_menu.append(new_drink)
        #주문한 음료수 리스트 출력하자

    def show_menu(self):
        for index, drink in enumerate(self.menu):
            print(f'{index + 1}. {drink.name}\t{drink.price}원')

if __name__ == '__main__':
    order = Order()
    order.order()
    print(order)

