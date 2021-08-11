from tkinter import *
from tkinter import ttk
from car import car
from moto import motorcicle
from home import home


main = Tk()
main.title('test')
main.geometry('400x270')

l1 = Label(main, text='Что будем оценивать?', font=("Arial", 20)).place(x=55, y=30)


button = Button(main, text='Машина', fg='green', command=car).place(x=50, y=120, width=80, height = 40)
button = Button(main, text='Дом', fg='red', command=home).place(x=160, y=120, width=80, height = 40)
button = Button(main, text='Мотоцикл', fg='blue', command=motorcicle).place(x=270, y=120, width=80, height = 40)

main.mainloop()