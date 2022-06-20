#1. 휴대전화번호 입력하면 -, /, 띄어쓰기 없애고 숫자만 출력하자
phone_number = '010-7240-4658'
for n in phone_number:
    if n == '-' or n == '/' or n == ' ':
        continue
    print(n, end='')
print()
phone_number = phone_number.replace('-', '')
phone_number = phone_number.replace('/', '')
phone_number = phone_number.replace(' ', '')
print(phone_number)

#>> 01072404658
print('-'*20)

#2. 학번 -> 학년, 반, 학과, 번호 출력하기
student_number = '2108'
# if student_number[1] == '1' or student_number[1] == '2':
#     g = '뉴미디어소프트웨어과'
# elif student_number[1] == '3' or student_number[1] == '4':
#     g = '뉴미디어웹솔루션과'
# elif student_number[1] == '5' or student_number[1] == '6':
#     g = '뉴미디어디자인과'
majors = ['뉴미디어소프트웨어과', '뉴미디어소프트웨어과',
          '뉴미디어웹솔루션과', '뉴미디어웹솔루션과',
          '뉴미디어디자인과', '뉴미디어디자인과']
index = int(student_number[1])
g = majors[index-1]
print(f'{student_number[0]}학년 {student_number[1]}반')
print(f'{g} {int(student_number[2:])}번')
#>> 2학년 1반 뉴미디어소프트웨어과 08번
#-> 2학년 1반 뉴미디어소프트웨어과 8번
#-> if문 안 쓰고
print('-'*20)

#3. N-sum
number = 331
n1 = int(number % 1000 / 100)
n2 = int(number % 100 /10)
n3 = int(number % 10)
print(n1+n2+n3)
#>>7
number = 523523
#숫자 한자리씩 빼서 계산하자
sum_val = 0
while True: #while number!=0
    if number == 0:
        break
    sum_val += number % 10
    number = number // 10
print(sum_val)
#문자 한자리씩 빼서 계산하자
number = 523523
number_s = str(number)  #'523523'
sum_val2 = 0
for n in number_s:
    sum_val2 += int(n)
print(sum_val2)
# sum_val3 = 0
# for index in range(len(number_s)):
#     sum_val3 += int(number_s[index])
# print(sum_val3)
# 나머지 = number % 10   #3
# number = number // 10   #523523 -> 52352
# 나머지 = number % 10   #2
# number = number // 10   #52352 -> 5235
# 나머지 = number % 10   #5
# number = number // 10   #5235 -> 523
# 나머지 = number % 10   #3
# number = number // 10   #523 -> 52
# 나머지 = number % 10   #2
# number = number // 10   #52 -> 5
# 나머지 = number % 10   #5
# number = number // 10   #5 -> 0
#
# 20
# 나머지 = number % 10   #0
# number = number // 10   #2
# 나머지 = number % 10   #2
# number = number // 10   #0

#>>20
print('-'*20)
#4. 369게임(1~100)
#>>1 2 짝 4 5 짝 ... 짝짝 100
for number in range(1, 100+1):  #1~100
    number_s = str(number)
    #'3', '6', '9' 를 세자 => count
    count = 0
    count += number_s.count('3')
    count += number_s.count('6')
    count += number_s.count('9')

    if count == 0:  #count == 0: 숫자 출력하자
        print(number)
    else:   #count != 0: count만큼 '짝' 출력하자
        print('짝' * count)
# gugudan(): 구구단 2단 출력하자
# gugudan(5): 구구단 5단 출력하자
def gugudan(dan=2):
    for n in range(1, 9 + 1):   # 1 <= n <= 9
        print(f'{dan} x {n} = {dan*n}')
gugudan(5)
gugudan()









