from drink import Drink


class Coffee(Drink):
    pass

if __name__ == '__main__':
    커피1 = Coffee('카페모카', 3500)
    커피1.order()
    print(커피1)