#3. 십진수를 2진수로
def dec_to_bin2(number):
    # return bin(number)[2:]
    return bin(number).replace('0b', '')
'''
def dec_to_bin(number):
    #share: 몫, reminder: 나머지
    #number를 2로 나누자
    #number이 0이면, 끝내고 결과 리턴
    #아니면, number를 2로 나눈 나머지를 앞으로 보관하자 s = '1' + s
        #number는 number를 2로 나눈 몫으로 설정하자
'''

def dec_to_bin(number):
    #share: 몫, reminder: 나머지
    s = ''
    #무한반복
    while True:
        #number이 0이면, 끝내고 결과 리턴
        if number == 0:
            return s
        #아니면, number를 2로 나눈 나머지를 앞으로 보관하자 s = '1' + s
        else:
            reminder = number % 2
            s = str(reminder) + s
            #number는 number를 2로 나눈 몫으로 설정하자
            number = number // 2

print(dec_to_bin(10))   #1010
print(dec_to_bin(2))    #10
print(dec_to_bin(77))   #1001101
print(dec_to_bin(1024))   #1000000000
print(type(dec_to_bin(10)))   #1010

print('0b1010'[2:])
s = '0'


#'10'