greeting = 'hello'
to = 'world!'
say_hello = greeting + ', ' + to
print(say_hello)
print(greeting * 5)
print(greeting + '\n' + to)
print("\"" + greeting + "\"")
print('\'' + greeting + '\'')
names = '''양다연
인소리
이예진
'''
print(names)

# *** indexing, slicing
names = '양다연인소리이예진'
print(names[2]) #'연'
print(names[4])  #'소'
print(names[8]) #'진'
print(names[-1])    #'진'
print(names[-2])    #'예'
print(names[-9])    #'양'
student_number = '2112'
print(student_number[0] + '학년')
print(f'{student_number[0]}학년')
print(f'{student_number[1]}반')
#'양다연인소리이예진'
print(names[2:5])   #[2]~[4]
print(names[2:4])   #연인
print(names[-7:-5])
print(names[4:7])   #소리이
print(names[7:9])   #예진
print(f'{student_number[2:4]}번')
print(f'{student_number[-2:]}번')    #start:end-1    [start:]: 끝까지
print(f'{student_number[0:2]}학년반')
print(f'{student_number[0:-2]}학년반')
print(f'{student_number[:-2]}학년반')  #start:end-1    [:end-1]: 앞에서
print(f'{student_number[:]}')  #start:end-1    [:]: 앞~끝까지

#문자열 함수
print(f'길이: {len(student_number)}')  #4
print(f'2 개수: {student_number.count("2")}') #2
print(f'{"NCT dream darling".upper()}')
print(f'{"NCT dream darling".lower()}')
s = "   NCT dream buffering     "
print(f'{s.strip()}')
print(f'{s.lstrip()}')
print(f'{s.rstrip()}')
print(f'{s.find("e")}') #9
print(f'{s.find("z")}') #없으면 -1
print(f'{s.rfind("e")}') #17
print(f'{s.count("e")}')    #2
print(f'{s.index("d")}') #7
#print(f'{s.index("z")}')    #없으면 ValueError: substring not found
print(f'{s.replace("buffering", "hello future")}')  #replace하면 바뀐 문자열 리턴하지만 원본은 바뀌지 않음
print(s)
#"   NCT dream buffering     "
print('e' in s) #True
print('z' in s) #False

#split, join
ip = '10.253.123.119'
ip_list = ip.split('.')
print(ip_list)
names = '양다연, 최자윤, 임채영, 이예진, 인소리'
name_list = names.split(', ')
print(name_list)
print(name_list[2])
print(name_list[2:4])
ip_list_str = '::'.join(ip_list)
print(ip_list_str)
name_list_str = ' | '.join(name_list)
print(name_list_str)
print(",".join(name_list))