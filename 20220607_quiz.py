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
#>>7
number = 523523
#>>20

#4. 369게임(1~100)
#>>1 2 짝 4 5 짝 ... 짝짝 100









