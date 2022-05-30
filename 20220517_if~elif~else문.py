# # 교통수단 문제
# money = int(input('돈을 입력하시오 : '))
# if money >= 10000:
#     print("택시를 타라")
# elif money >= 720:
#     print("버스를 타라")
# else:
#     print("그냥 걸어가라")
# 배수 판별 문제
# num = int(input('정수를 입력하시오 : '))
# if num % 4 == 0:
#     print("4의 배수")
# elif num % 3 == 0:
#     print("3의 배수")
# elif num % 2 == 0:
#     print("2의 배수")
# print("--------------")
# if num % 4 == 0:
#     print("4의 배수")
# #-------------------
# if num % 3 == 0:
#     print("3의 배수")
# #-------------------
# if num % 2 == 0:
#     print("2의 배수")
#
# # 나이대 판별 문제
# age = int(input('나이를 입력하시오 : '))
# if 10 <= age and age < 20: # 10 <= age < 20
#     print("10대")
# elif 30 <= age and age < 40: # 30 <= age < 40
#     print("30대")
# else:
#     print("10대,30대 모두 아님")
#
# print("---------------------")
# print(str(age//10*10) + "대")
#
# # 논리연산자 문제
# x = int(input('정수를 입력하시오 : '))
# if x > 10 and x % 2 == 0:
#     print("10 초과 짝수")
#
#
# # 등급 출력 문제
# score = int(input('점수를 입력하시오 : '))
# if 90 <= score <= 100:
#     print("A")
# elif 80 <= score < 90: # 80 <= score
#     print("B")
# elif 70 <= score < 80:
#     print("C")
# elif 60 <= score < 70:
#     print("D")
# elif 0 <= score < 60:
#     print("F")
#
# # MBTI 문제
# mbti = input('당신의 mbti를 입력하시오 : ')
# if mbti == 'INFP' or mbti == 'infp': # mbti.upper() == 'INFP'
#     print("블록체인형")
# elif mbti == 'ENFP' or mbti == 'enfp':
#     print("AI형")
# else:
#     print("아직 개발중입니다.")
#
# # 중첩 제어문
# x = int(input('정수를 입력하시오 : '))
# if x > 10:
#     if x % 2 == 0:
#         print("10초과 짝수")
#     else:
#         print("10초과 홀수")
# else:
#     print("10이하")

# 아이디, 패스워드 검사 프로그램
nickname = "yejin"
user_id = "yejin18"
user_pw = "12345"
id = input('ID를 입력하시오 : ')
if id == user_id:
    pw = input('PW를 입력하시오 : ')
    if pw == user_pw:
        print('환영합니다. {}님'.format(nickname))
    else:
        print("패스워드가 틀렸습니다.")
else:
    print("알 수 없는 사용자입니다.")
