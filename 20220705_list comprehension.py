#1~10까지 홀수의 제곱 리스트 만들자
array = []
for n in range(1, 10, 2):
    array.append(n ** 2)    #(n * n)
print(array)

array = [n**2 for n in range(1, 10, 2)]
print(array)

array = []
for n in range(1, 10, 2):
    if n ** 2 > 30:
        array.append(n ** 2)
print(array)

array = [n ** 2 for n in range(1, 10, 2) if n ** 2 > 30]
print(array)