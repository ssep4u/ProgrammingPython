# 클래스 연습 1
# 1. 요리 2. 연예인 3. 자동차 4. 게임

'''
속성
title: 제목
genre: 장르
platform: 플랫폼

행동
실행하다()
로그인하다()
저장하다()

객체
World of Warcraft, 마인크래프트, 배틀그라운드

java
class Game {
    String title;
    public String genre;
    int platform;   //0: Windows 1: macOS 2: iOS 3: Android 4: Nintendo
    public Game(title) {    #특수메소드: 생성자
        this.title = title;
        this.genre = "MMORPG";
        this.platform = 0;
    }
    public void run() {
    }
    public boolean login(String id, String password) {
    }
    public int save() {
    }
    public toString() { #특수 메소드
        return title + genre;
    }
}
예서게임 = new Game("World of Warcraft");
채영게임 = new Game("배틀 그라운드");
채영게임.genre = "FPS";
'''


class Game:
    def __init__(self, title):  # 특수메소드: 생성자
        self.title = title
        self.genre = 'MMORPG'
        self.platform = 0
    def set_genre (self, genre):
        genres = ['FPS', 'MMORPG', 'Action', 'SPORTS']
        if genre in genres:
            self.genre = genre

    def run(self):
        print('실행')

    def login(self, id, password):
        print(f'{id}님 환영합니다')

    def save(self):
        print('저장완료')

    def __str__(self):  #특수메소드: 문자열표현
        return f'{self.title} {self.genre}'

#class -> object: 객체화
예서게임 = Game('World of Warcraft')
채영게임 = Game('마인크래프트')
채영게임.genre = '샌드박스'
print(예서게임)
print(채영게임)