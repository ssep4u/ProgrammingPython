games = {"LOL", "Overwatch", "Tetris", 1942, 2048}
print(games)    #{2048, 'Tetris', 'LOL', 'Overwatch', 1942}
                #{2048, 'LOL', 1942, 'Overwatch', 'Tetris'}
empty_set = {}  #빈 딕셔너리
empty_set = set()   #빈 셋
print(set({'google': 'google.com', 18: 'unesco.org'}))  #{18, 'google'}
#요소 추가
games.add("테일즈러너")
print(games)
games.update(("카트라이더", "지렁이"))
print(games)
#요소 제거
games.remove("LOL")
print(games)
#셋 연산
#교집합
#합집합
#차집합
#대칭 차집합
#p56, 57 실습 하자
#p57 표  *****
a = set()
a.add('밥')
a.add('국')
print(a)
a.add('밥')
print(a)
idol = ['세븐틴', '스트레이키즈', '악뮤', '방탄소년단', '방탄소년단']
print(idol)
print(list(set(idol)))  #중복제거: set() -> list()
