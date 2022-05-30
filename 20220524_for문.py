# 문자열
for ch in "SORI":
    print(ch,end='*')
print()
# 리스트
for item in ["힙합","발라드"]:
    print(item)

# 튜플
for item in (12,393):
    print(item)
for a,b in ((12,33),(2,35)):
    print(a,b)

# 셋
for item in {"WSM","JAVA","Python"}:
    print(item)

# 딕셔너리
pl = {"C":1972,"JAVA":1995,"Python":1991, "유솔":2004, "예서": 2005}
for item in pl:
    print(item)
for key in pl.keys():
    print(key)
for val in pl.values():
    print(val)
for key,val in pl.items():
    print(key, val)

# num_list문제
num_list = [-5,127,-13,9,-21,100]
for num in num_list:
    if num > 0:
        print(num)
# 짝수, 홀수
num_list = [13,8,7,55,100,2,12,10,17]
for num in num_list:
    if num % 2 == 0:
        print("{}은 짝수이다".format(num))
    else:
        print("{}은 홀수이다".format(num))
print('-------------------------')
holzzak = ["짝수","홀수"]
for num in num_list:
    print("{}은 {}이다.".format(num,holzzak[num%2]))
print('---------------')
# 자리수
for num in num_list:
    print('{}은 {}자리수이다.'.format(num,len(str(num))))

# 세봉고등학교
svt = {'에스쿱스':90,'승관':85,'우지':75,'버논':30,'디노':25}
for name,score in svt.items():
    if score >= 60:
        print('{}은/는 합격이다.'.format(name))
    else:
        print('{}은/는 불합격이다.'.format(name))

# range()함수
# range(시작값, 종료값, 단계)
# range(기본값 0, 종료값, 기본값 1)
print(list(range(0,10,1)))
print(list(range(10,0,-1))) # 단계값이 음수면 역순
print(list(range(0,10,5)))

print(list(range(0,10)))
print(list(range(10)))

# 리스트
nctdream = ['런쥔','제노','해찬','마크','재민','지성','천러']
for member in nctdream:
    print(member)
for i in range(0,len(nctdream)):
    print(i+1, nctdream[i])
print('--------------')
for i,member in enumerate(nctdream):
    print(i+1,member)

# range함수 문제
total = 0
for i in range(1,200):
    if i % 3 == 0:
        total += i
print(total)

total = 0
for i in range(0,200,3):
    total += i
print(total)

sum_val = 0
for i in range(500,1000,5):
    sum_val += i
print(sum_val)

print(sum(list(range(500,1000,5))))

# sum,max,min함수
l = [1,2,3,4,5]
print(sum(l))
print(max(l))
print(min(l))
