from tkinter import *
from tkinter import ttk
import pandas as pd
import pip
pip.main(['install', 'catboost'])
from catboost import CatBoostRegressor

def car():

    def test():


        fuel = {'CNG': 0, 'Diesel': 1, 'LPG': 2, 'Petrol': 3}
        transmission = {'Automatic': 0, 'Manual': 1}
        brands = {'Ambassador': 0,
 'Audi': 1,
 'BMW': 2,
 'Bentley': 3,
 'Chevrolet': 4,
 'Datsun': 5,
 'Fiat': 6,
 'Force': 7,
 'Ford': 8,
 'Honda': 9,
 'Hyundai': 10,
 'Isuzu': 11,
 'Jaguar': 12,
 'Jeep': 13,
 'Lamborghini': 14,
 'Land': 15,
 'Mahindra': 16,
 'Maruti': 17,
 'Mercedes-Benz': 18,
 'Mini': 19,
 'Mitsubishi': 20,
 'Nissan': 21,
 'Porsche': 22,
 'Renault': 23,
 'Skoda': 24,
 'Tata': 25,
 'Toyota': 26,
 'Volkswagen': 27,
 'Volvo': 28}
        owner = {'First': 0, 'Fourth & Above': 1, 'Second': 2, 'Third': 3}
        data = pd.DataFrame([[float(message1.get()), float(message2.get()), fuel[variable.get()], transmission[variable1.get()],
                             owner[variable2.get()], float(message3.get()), float(message4.get()),
                             float(message5.get()), brands[car_brand.get()]]])
        one_hot = pd.read_csv('one_hot.csv')
        all_data = data.join(one_hot)
        all_data[car_model.get()] = 1
        print(all_data)
        model = CatBoostRegressor()
        model.load_model('car')
        pred = model.predict(all_data.values)
        Label(carwind, text='Цена:' + str(round(pred[0])), font=("Arial", 12)).place(x=50, y=200)
        print(pred)




    carwind = Tk()
    carwind.title('car')
    carwind.geometry('600x270')
    l1 = Label(carwind, text='Год :').place(x=50, y=30)
    l2 = Label(carwind, text='Пробег :').place(x=150, y=30)
    l3 = Label(carwind, text='Тип топлива :').place(x=250, y=30)
    l4 = Label(carwind, text='Трансмиссия :').place(x=350, y=30)
    l5 = Label(carwind, text='Владелец :').place(x=450, y=30)
    l7 = Label(carwind, text='Объем Двигателя :').place(x=50, y=120)
    l9 = Label(carwind, text='Лошадиные силы:').place(x=200, y=120)
    l10 = Label(carwind, text='Кол-во мест:').place(x=350, y=120)
    l11 = Label(carwind, text='Марка:').place(x=200, y=200)
    l12 = Label(carwind, text='Модель:').place(x=350, y=200)

    message1 = StringVar(carwind)
    message2 = StringVar(carwind)
    message3 = StringVar(carwind)
    message4 = StringVar(carwind)
    message5 = StringVar(carwind)

    message_entry1 = Entry(carwind, textvariable=message1).place(x=50, y=60, width=60)#god
    message_entry2 = Entry(carwind, textvariable=message2).place(x=150, y=60, width=60)#probeg
    message_entry3 = Entry(carwind, textvariable=message3).place(x=50, y=150, width=60)#ob dv
    message_entry4 = Entry(carwind, textvariable=message4).place(x=200, y=150, width=60)# l sil
    message_entry5 = Entry(carwind, textvariable=message5).place(x=350, y=150, width=60)# kol-vo mest
    variable = StringVar(carwind)
    opt = OptionMenu(
        carwind, variable, *[
            'Diesel', 'Petrol', 'CNG', 'LPG'
        ]
    ).place(x = 250, y = 60, width=90)

    variable1 = StringVar(carwind)
    opt = OptionMenu(
        carwind, variable1, *[
            'Manual', 'Automatic'
        ]
    ).place(x=350, y=60, width=90)

    variable2 = StringVar(carwind)
    opt = OptionMenu(
        carwind, variable2, *[
            'First', 'Second', 'Third', 'Fourth & Above'
        ]
    ).place(x=450, y=60, width=90)

    brands = ['Maruti',
 'Hyundai',
 'Honda',
 'Toyota',
 'Mercedes-Benz',
 'Volkswagen',
 'Ford',
 'Mahindra',
 'BMW',
 'Audi',
 'Tata',
 'Skoda',
 'Renault',
 'Chevrolet',
 'Nissan',
 'Land',
 'Jaguar',
 'Mitsubishi',
 'Mini',
 'Fiat',
 'Volvo',
 'Porsche',
 'Jeep',
 'Datsun',
 'Isuzu',
 'Force',
 'Ambassador',
 'Lamborghini',
 'Bentley']

    models = [['Swift',
  'Wagon',
  'Alto',
  'Ertiga',
  'Ciaz',
  'Ritz',
  'Baleno',
  'Celerio',
  'Vitara',
  'SX4',
  'Zen',
  'Dzire',
  'Omni',
  'Eeco',
  'A-Star',
  '800',
  'S',
  'Ignis',
  'Grand',
  'S-Cross',
  'Esteem',
  'Versa'],
 ['i20',
  'Verna',
  'i10',
  'Grand',
  'Creta',
  'EON',
  'Xcent',
  'Santro',
  'Elantra',
  'Accent',
  'Santa',
  'Elite',
  'Getz',
  'Sonata',
  'Tucson'],
 ['City',
  'Amaze',
  'Brio',
  'Jazz',
  'Civic',
  'Accord',
  'CR-V',
  'Mobilio',
  'BRV',
  'WRV',
  'BR-V',
  'WR-V'],
 ['Innova', 'Fortuner', 'Corolla', 'Etios', 'Camry', 'Qualis', 'Platinum'],
 ['New',
  'E-Class',
  'M-Class',
  'GLA',
  'CLA',
  'B',
  'GLE',
  'GL-Class',
  'S',
  'A',
  'GLC',
  'S-Class',
  'R-Class',
  'C-Class',
  'SLK-Class',
  'GLS',
  'SLC',
  'CLS-Class',
  'SL-Class'],
 ['Polo', 'Vento', 'Jetta', 'Ameo', 'Passat', 'CrossPolo', 'Tiguan', 'Beetle'],
 ['Figo',
  'Ecosport',
  'EcoSport',
  'Fiesta',
  'Endeavour',
  'Ikon',
  'Aspire',
  'Freestyle',
  'Classic',
  'Fusion',
  'Mustang'],
 ['XUV500',
  'Scorpio',
  'Xylo',
  'KUV',
  'Bolero',
  'Ssangyong',
  'TUV',
  'Thar',
  'Quanto',
  'Verito',
  'NuvoSport',
  'Logan',
  'Renault',
  'XUV300'],
 ['3', '5', 'X1', 'X5', 'X3', '7', '6', 'X6', '1', 'Z4'],
 ['A4', 'A6', 'Q7', 'Q5', 'Q3', 'A3', 'TT', 'A7', 'A8', 'RS5'],
 ['Indica',
  'Indigo',
  'Nano',
  'Zest',
  'Manza',
  'Tiago',
  'Safari',
  'New',
  'Sumo',
  'Tigor',
  'Bolt',
  'Hexa',
  'Nexon',
  'Xenon',
  'Venture'],
 ['Superb', 'Rapid', 'Octavia', 'Laura', 'Fabia', 'Yeti'],
 ['Duster', 'KWID', 'Scala', 'Pulse', 'Fluence', 'Captur', 'Koleos', 'Lodgy'],
 ['Beat',
  'Cruze',
  'Aveo',
  'Optra',
  'Spark',
  'Enjoy',
  'Sail',
  'Tavera',
  'Captiva'],
 ['Micra', 'Sunny', 'Terrano', 'X-Trail', 'Evalia', 'Teana'],
 ['Rover'],
 ['XF', 'XJ', 'XE', 'F'],
 ['Pajero', 'Outlander', 'Cedia', 'Lancer', 'Montero'],
 ['Cooper', 'Countryman', 'Clubman'],
 ['Linea', 'Grande', 'Avventura', 'Punto'],
 ['S60', 'XC60', 'V40', 'XC90', 'S80'],
 ['Panamera', 'Cayenne', 'Boxster'],
 ['Compass'],
 ['GO', 'redi-GO', 'Redi'],
 ['D-MAX', 'MUX'],
 ['One'],
 ['Classic'],
 ['Gallardo'],
 ['Continental']]

    car_brand = ttk.Combobox(carwind, width=10, value=(brands))
    car_brand.place(x=200, y=230)

    def callback(eventObject):
        abc = eventObject.widget.get()
        car = car_brand.get()
        index = brands.index(car)
        car_model.config(values=models[index])

    car_model = ttk.Combobox(carwind, width=10)
    car_model.place(x=350, y=230)
    car_model.bind('<Button-1>', callback)
    button = Button(carwind, text='Оценить', fg='green', command=test).place(x=500, y = 200, width=60, height = 30)
    carwind.mainloop()
