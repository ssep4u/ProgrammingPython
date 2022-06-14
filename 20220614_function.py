#예약어X
#snake_case
# sum = 0   TypeError: 'int' object is not callable
# def sum(x): #내장함수와 이름이 같으면 에러는 안 나지만, 내장함수를 호출할 수 없음
#     print(x)
a = sum([10, 20, 3])
print(a)
print('-' * 20)
'''
java 함수
접근제어자 리턴형 함수명(파라미터1, 파라미터2) {
    return 값;
}

C 함수
리턴형 함수명(파라미터1, 파라미터2) {
    return 값;
}

python 함수
def 함수명(파리미터1, 파라미터2):
    return 값
'''
def my_print(age):
    print('임정훈: ' + str(age) + '살입니다.')   #이름: 살입니다.
    print('임정훈: ', age, '살입니다.')   #이름:  20 살입니다.
    print(f'임정훈: {age}살입니다.')

def my_print2(name, age):
    print(name + ': ' + str(age) + '살입니다.')   #이름: 살입니다.
    print(name,': ', age, '살입니다.')   #이름:  20 살입니다.
    print(f'{name}: {age}살입니다.')

print(my_print(20))   #my_print() 실행, my_print()의 리턴값 출력
print(my_print2('안유진', 20))   #my_print() 실행, my_print()의 리턴값 출력
print(my_print2(age=20, name='안유진'))   #아규먼트 순서와 관계없이 파라미터 이름을 쓰면 거기에 들어감
print('-' * 20)
def my_print3(name, age, group):
    print(name + ': ' + str(age) + '살입니다.' + group + '소속입니다.')   #이름: 살입니다.
    print(name,': ', age, '살입니다.', group, '소속입니다.')   #이름:  20 살입니다.
    print(f'{name}: {age}살입니다. {group}소속입니다.')
    
my_print3(age=20, name='안유진', group='아이브')
#my_print3('안유진', age=20, '아이브') #키워드 인자 뒤에는 계속 키워드 인자 해야 함
my_print3('안유진', group='아이브', age=20)   #위치 인자는 무조건 키워드 인자 앞에 있어야 함
print('-' * 20)
def my_print4(name, age, group='아이브'):  #기본값있는 파라미터
    print(name + ': ' + str(age) + '살입니다.' + group + '소속입니다.')   #이름: 살입니다.
    print(name,': ', age, '살입니다.', group, '소속입니다.')   #이름:  20 살입니다.
    print(f'{name}: {age}살입니다. {group}소속입니다.')

my_print4('안유진', age=20, group='아이즈원')  # 위치 인자는 무조건 키워드 인자 앞에 있어야 함
print('-' * 20)
#가변인자
def my_print5(*args):   #args 자료형은 tuple
    print('정보: ')
    # print(type(args))
    for arg in args:
        print(arg)

def my_print6(name, *args):   #args 자료형은 tuple
    print(f'{name} 정보: ')
    # print(type(args))
    for arg in args:
        print(arg)
    
my_print5('안유진', 20, '아이브', '러브다이브')
my_print6('안유진', 20, '아이브', '러브다이브')
print('-' * 20)
# def my_print7(name, age=20, group):  #기본값있는 파라미터 뒤에는 무조건 기본값있는 파라미터
#     print(name + ': ' + str(age) + '살입니다.' + group + '소속입니다.')   #이름: 살입니다.
#     print(name,': ', age, '살입니다.', group, '소속입니다.')   #이름:  20 살입니다.
#     print(f'{name}: {age}살입니다. {group}소속입니다.')
# my_print7('CL', 21)
# print('-' * 20)
