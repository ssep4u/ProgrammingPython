'''
사람 - 이름, 나이, 성별
선생님 - 과목, 담임반
'''
'''
클래스는 웬만하면 단수. 단 여러개 담으면 복수
수치가 들어오는 값이면, 가능하면 숫자로 세팅하자
    나이, 생년 등은 숫자, 핸드폰번호는 문자로 처리하자
    01012345678은 10억 1234만 5678이 아님 => '01012345678'
    
변수, 함수, 클래스명 명확하게

이제 더이상 내 코드는 나만 보지 않는다. 누구나 내 코드를 읽을 수 있도록 
'''

class Person:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.gender = None

    def set_age(self, age):#매개변수와 함수이름을 같게하지말것
        self.age = age

    def set_gender(self, gender):
        genders = ['여자','남자']
        if gender in genders:
            self.gender = gender
    def __str__(self):
        return f'{self.name}\t{self.age}\t{self.gender}'

# people에 값넣기
고나근샘 = Person('고낙은')
고나근샘.set_age(34)
고나근샘.set_gender('남자')
print(고나근샘)

class Teacher(Person):
    def set_subject(self, subject):
        self.subject = subject
    def set_homeroom_teacher(self, homeroom_teacher):
        self.homeroom_teacher = homeroom_teacher
    def __str__(self):
        return f'{super().__str__()}\t담당과목: {self.subject}\t담임반: {self.homeroom_teacher}'


#Teacher에 값넣기
고낙은샘 = Teacher('고낙은')
고낙은샘.set_subject('체육')
고낙은샘.set_homeroom_teacher('2-2')
print(고낙은샘)