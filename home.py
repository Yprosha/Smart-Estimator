from tkinter import *
from tkinter import ttk
import pandas as pd
import pip
pip.main(['install', 'catboost'])
from catboost import CatBoostRegressor
import numpy as np

def home():

    def test():


        watefront = {'Да': 1, 'Нет': 0}

        data = np.array([[float(message6.get()), float(message7.get()), float(message3.get()), float(message4.get()),
                             float(message2.get()), watefront[variable.get()], float(variable1.get()),
                             float(variable2.get()), float(grade.get()), float(message5.get()), float(message8.get()), float(message1.get())]])

        model = CatBoostRegressor()
        model.load_model('home_model')
        pred = model.predict(data)
        Label(carwind, text='Цена:' + str(round(pred[0])), font=("Arial", 12)).place(x=50, y=200)
        print(pred)




    carwind = Tk()
    carwind.title('car')
    carwind.geometry('600x270')
    l1 = Label(carwind, text='Год :').place(x=50, y=30)
    l2 = Label(carwind, text='Этажей :').place(x=150, y=30)
    l3 = Label(carwind, text='Вид на воду :').place(x=250, y=30)
    l4 = Label(carwind, text='Вид :').place(x=350, y=30)
    l5 = Label(carwind, text='Состояние :').place(x=450, y=30)
    l7 = Label(carwind, text='Жилая пл. :').place(x=50, y=120)
    l9 = Label(carwind, text='Общая пл.:').place(x=150, y=120)
    l10 = Label(carwind, text='Пл. без подвала:').place(x=250, y=120)
    l11 = Label(carwind, text='Оценка:').place(x=200, y=200)
    l12 = Label(carwind, text='Пл. подвала:').place(x=350, y=200)
    l13 = Label(carwind, text='Кол-во спален:').place(x=370, y=120)
    l14 = Label(carwind, text='Кол-во санузлов:').place(x=480, y=120)

    message1 = StringVar(carwind)
    message2 = StringVar(carwind)
    message3 = StringVar(carwind)
    message4 = StringVar(carwind)
    message5 = StringVar(carwind)
    message6 = StringVar(carwind)
    message7 = StringVar(carwind)
    message8 = StringVar(carwind)

    message_entry1 = Entry(carwind, textvariable=message1).place(x=50, y=60, width=60)
    message_entry2 = Entry(carwind, textvariable=message2).place(x=150, y=60, width=60)
    message_entry3 = Entry(carwind, textvariable=message3).place(x=50, y=150, width=60)
    message_entry4 = Entry(carwind, textvariable=message4).place(x=150, y=150, width=60)
    message_entry5 = Entry(carwind, textvariable=message5).place(x=250, y=150, width=60)
    message_entry6 = Entry(carwind, textvariable=message6).place(x=370, y=150, width=60)
    message_entry7 = Entry(carwind, textvariable=message7).place(x=480, y=150, width=60)
    message_entry8 = Entry(carwind, textvariable=message8).place(x=350, y=230, width=60)
    variable = StringVar(carwind)
    opt = OptionMenu(
        carwind, variable, *[
            'Да', 'Нет'
        ]
    ).place(x = 250, y = 60, width=90)

    variable1 = StringVar(carwind)
    opt = OptionMenu(
        carwind, variable1, *[
            0,1,2,3,4
        ]
    ).place(x=350, y=60, width=90)

    variable2 = StringVar(carwind)
    opt = OptionMenu(
        carwind, variable2, *[
            1,2,3,4,5
        ]
    ).place(x=450, y=60, width=90)

    grades = [1,2,3,4,5,6,7,8,9,10,11,12,13]



    grade = ttk.Combobox(carwind, width=10, value=(grades))
    grade.place(x=200, y=230)


    button = Button(carwind, text='Оценить', fg='green', command=test).place(x=500, y = 200, width=60, height = 30)
    carwind.mainloop()
