#예약어
import keyword
print(keyword.kwlist)

print('-' * 200)
#달력 보기
import calendar
print(calendar.month(2022, 4))
print(calendar.month(2004, 9))
print(calendar.month(2022, 12))
print(calendar.month(19, 12))

print('-' * 200)
#현재 날짜와 시각 보기
import datetime
now = datetime.datetime.now()
print(now)
print(now.year, now.month, now.day, now.hour, now.minute, now.second)
birthday = datetime.datetime(2022, 4, 11)
print(now - birthday)
my_birthday = datetime.datetime(1980, 3, 31)
print(now - my_birthday)
christmas = datetime.datetime(2022, 12, 25)
print(christmas - now)

print('-' * 200)
#윈도우 보기
# import tkinter as tk
# base = tk.Tk()
# base.mainloop()

#turtle
import turtle as t
t.shape('turtle')
t.speed(100)

t.forward(100)
t.right(90)
t.fd(100)
t.rt(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)

t.mainloop()
