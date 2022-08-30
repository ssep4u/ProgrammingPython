#1. 전화번호를 인자로 받아,
# 각 숫자 중 홀수만 더해서 합계를 리턴하는 함수
def sum_odd(phone_number):
    sum_value = 0
    #전화번호에서 하나씩 꺼내자
    for number in phone_number:
        # print(number)
        #문자 -> 숫자
        number = int(number)
        #홀수인지 구분하자
        if number % 2 != 0:
            # print(number)
            #합계 구하자
            sum_value += number
    return sum_value

def sum_odd2(phone_number):
    return sum([int(number) for number in phone_number if int(number) % 2 != 0])

result = sum_odd('01012345678')
print(result)
result = sum_odd('01022224444')
print(result)
result = sum_odd2('01012345678')
print(result)
result = sum_odd2('01022224444')
print(result)

# sum_value = 0
# for 하나 in 덩어리:
#     sum_value += 하나
#
# count_value = 0
# for 하나 in 덩어리:
#     count_value += 1
