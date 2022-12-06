print(abs(-10)) #10
#infinite : 무한
#finish: 유한
#never: 절대 ~ 아니다
#never give up: 절대 포기 하지 마!
#absolute: 절대

# + 연산자: 문자 + : 이어주는거
#문자*정수: 문자 반복 정수만큼
list1 = ['d', 'c', 'a', 'b']
print(list1)
list1.reverse()
print(list1)
list1.sort()    #오름차순 정렬
list1.reverse() #뒤집기: 내림차순X
print(list1)
list1 = ['d', 'c', 'a', 'b']
print(list1)
list1.sort(reverse=True)    #내림차순
print(list1)

import random
def rolling_dice(pip=6):
    n = random.randint(1, pip)
    print(n)
rolling_dice(10)
rolling_dice()

print('정가현', '조예서')
print('정가현', '조예서', '오킹')
def p(*names):
    print(names)
    print(type(names))
    for name in names:
        print(name)
p('정현진', '이예진', '오킹')

def fn(a, b=[]):
    b.append(a)
    print(b)

fn(3)   #[3]
fn(5)   #[5] X [3, 5] O

def hello(name, msg="안녕"):
    print(f'{name}아 {msg}')
hello(msg='가현님', name='하이')



