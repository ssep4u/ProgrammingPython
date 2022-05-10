#dictionary: 사전: '단어': '뜻': key: value
d = {}
urls = {'google': 'google.com', 18: 'unesco.org'}
print(d)
print(urls)
#요소 추가
urls['유튜브'] = 'youtube.com'
print(urls) #{'google': 'google.com', 18: 'unesco.org', '유튜브': 'youtube.com'}
#요소 수정
urls['google'] = 'google.co.kr'
print(urls) #{'google': 'google.co.kr', 18: 'unesco.org', '유튜브': 'youtube.com'}
#요소 출력
print(urls['google'])
print(urls[18]) #18: 키
#요소 제거
del urls['유튜브'] #{'google': 'google.co.kr', 18: 'unesco.org'}
print(urls)
# urls.pop()  #TypeError: pop expected at least 1 argument, got 0
urls.pop(18)    #키값을 안주면, 위처럼 에러
print(urls) #{'google': 'google.co.kr'}
birthdays = {'다연': 5, '자윤': 11}
birthdays_list = [5, 11]
print(birthdays['다연'])
print(birthdays.get('다연'))
print('google.co.kr' in urls)   #False
print('google' in urls) #True
print('google.co.kr' in urls.values())  #True
urls['유튜브'] = 'youtube.com'
print(urls.values())    #값들 dict_values 객체
print(urls.keys())      #키들 dict_keys 객체
print(urls.items())     #(키, 값) 튜플들 dict_items 객체