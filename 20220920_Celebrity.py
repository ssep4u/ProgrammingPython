#연예인, 가수, 배우
class Celebrity:
    def __init__(self, name):
        self.name = name
        self.debut_date = None
        self.company = None

    def set_debut_date(self, debut_date):
        self.debut_date = debut_date

    def set_company(self, company):
        self.company = company

    def __str__(self):
        return f'{self.name}\t{self.debut_date}\t{self.company}'

아이유 = Celebrity('이지은')
아이유.set_debut_date('2008-09-18')
# 아이유.debut_date ='1900-01-01'  이렇게 하지마
아이유.set_company('이담엔터테인먼트')
print(아이유)

class Singer(Celebrity):
    def set_song(self, song):
        self.song = song
    def __str__(self):  #오버라이딩, 부모함수호출하는 방법
        return f'{super().__str__()}\t대표곡:{self.song}'

태민 = Singer('이태민')
태민.set_company('SM 엔터테인먼트')
태민.set_song('MOVE')
print(태민)

class Actor(Celebrity):
    def __init__(self, name):
        super().__init__(name)  #name, debut_date, company 초기화
        self.drama = None
    def set_drama(self, drama):
        self.drama = drama
    def __str__(self):
        return f'{super().__str__()}\t대표작:{self.drama}'

정경호 = Actor('정경호')
정경호.set_debut_date('2003-00-00')
정경호.set_drama('슬의생')
print(정경호)  #정경호    2003-00-00 None 슬의생

내아가들 = [태민, 정경호]
print(내아가들)
for 내아가 in 내아가들:
    print(내아가)