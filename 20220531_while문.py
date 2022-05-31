'''
JAVA
while(조건식) {
    실행문;
    증감식;
}

python
while 조건식:
    실행문
    증감식
'''
x = 3
while x < 5:
    print(x)    #무한루프 멈추는 방법: ctrl+c    KeyboardInterrupt
    x += 1
print("-"*20)
# echo = input()
# while echo != 'exit':
#     print(echo)
#     echo = input()
print("-"*20)
echo = input()
while True: #무한루프
    if echo == 'exit':  #탈출조건
        break
    print(echo)
    echo = input()


