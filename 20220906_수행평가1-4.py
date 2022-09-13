#4. 이니셜 abbreviate
def abbreviate(name):
    name = name.strip()
    #한 글자씩 꺼내기
    for index, sp in enumerate(name):
        #첫번째 글자 -> 대문자로 바꾸고 -> 저장
        if index == 0:
                result = sp.upper() + '. '
        #띄어쓰기! -> 한칸 뒤에 있는 글자를 -> 대문자로 바꾸고 -> 저장
        if sp == ' ':
            result += name[index + 1].upper() + '. '
    return result.strip()

def abbreviate2(name):
    result = '. '.join([word[0].upper() for word in name.split()])
    return result + '.'

print(abbreviate('Maverick'))   #M.
print(abbreviate('HAE CHAN'))   #H. C.
print(abbreviate('jin young park')) #J. Y. P.
print(abbreviate(' jin young park')) #J. Y. P.

# print(abbreviate2('Maverick'))   #M.
# print(abbreviate2('HAE CHAN'))   #H. C.
print(abbreviate2('jin young park')) #J. Y. P.
# print(abbreviate2(' jin young park')) #J. Y. P.
