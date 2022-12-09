from PyQt5.QtWidgets import *
from view import *
import csv
import random

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


artist_list = []
title_list = []
genre_list = []
time_period_list = []
year_list = []
mood_list = []
duet_group_list = []
difficulty_list = []
range_list = []

with open('song_list.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        artist_list.append(line[0])
        title_list.append(line[1])
        genre_list.append(line[2])
        time_period_list.append(line[3])
        year_list.append(line[4])
        mood_list.append(line[5])
        duet_group_list.append(line[6])
        difficulty_list.append(line[7])
        range_list.append(line[8])

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton_Random.clicked.connect(lambda: self.random())
        self.pushButton_Song.clicked.connect(lambda: self.output())

    def random(self):
        i = random.randint(0, 515)
        self.label_Song.setText(f'"{title_list[i]}"\n{artist_list[i]}')

    def output(self):
        sorted_list = []
        year = ''
        range = ''
        mood = ''

        match self.slider_Years.sliderPosition():
            case 0:
                year = '60s'
            case 1:
                year = '70s'
            case 2:
                year = '80s'
            case 3:
                year = '90s'
            case 4:
                year = '2000s'
            case 5:
                year = '2010s'
            case _:
                print("None")
        print(year)

        match self.slider_Range.sliderPosition():
            case 0:
                range = 'Bass'
            case 1:
                range = 'Baritone'
            case 2:
                range = 'Tenor'
            case 3:
                range = 'Alto'
            case 4:
                range = 'Mezzo'
            case 5:
                range = 'Soprano'
            case _:
                print("None")
        print(range)

        match self.slider_Mood.sliderPosition():
            case 0:
                mood = 'Bare your soul'
            case 1:
                mood = 'Swagger'
            case 2:
                mood = 'Get happy'
            case 3:
                mood = 'Just dance'
            case 4:
                mood = 'Rage on'
            case _:
                print("Unsure")
        print(mood)



#         f'"{title_list[i]} by {artist_list[i]} ({year_list[i]})\nGenre:{genre_list[i]} Time Period:{time_period_list[i]}\n'
#         f'Range:{range_list[i]} Mood:{mood_list[i]}\nDifficulty:{difficulty_list[i]} {duet_group_list[i]}')
