#2. 영단어를 인자로 받아,
# 모음인 a, e, i, o, u만 *로 대체하여 리턴
def encrypt(word):
    result = ''
    #영단어를 한글자씩 꺼내자
    for char in word:
        # print(char)
        #a인지 또는 e인지 또는 i인지 또는 o인지 또는 u인지 구분하자 맞으면
            if char == 'a' \
                or char == 'e' \
                or char == 'i' \
                or char == 'o' \
                or char == 'u':
                #별로 바꾸자
                char = '*'
                result += char
            #다르면
            else:
                # 그대로 쓰자
                result += char
    return result


        
    

print(encrypt('ive'))   #*v*

#문자열 리턴: 숫자 sum 과 비슷
# string = ''
# for 하나 in 덩어리:
#     string += 하나






