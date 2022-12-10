from PyQt5.QtWidgets import *
from view import *
import csv
import random

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
# Global lists to access data
artist_list = []
title_list = []
genre_list = []
time_period_list = []
year_list = []
mood_list = []
duet_list = []
difficulty_list = []
range_list = []

# Reads each line and separates values based on position to individual lists
with open('song_list.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        artist_list.append(line[0])
        title_list.append(line[1])
        genre_list.append(line[2])
        time_period_list.append(line[3])
        year_list.append(line[4])
        mood_list.append(line[5])
        duet_list.append(line[6])
        difficulty_list.append(line[7])
        range_list.append(line[8])


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Connects button functionality
        self.pushButton_Random.clicked.connect(lambda: self.random())
        self.pushButton_Song.clicked.connect(lambda: self.output())

    # Random song selection
    def random(self):
        i = random.randint(0, 515)
        self.label_Song.setText(f'"{title_list[i]}"\n{artist_list[i]}')

    # Song selection based on input
    def output(self):
        year = ''
        ranges = ''
        mood = ''
        difficulty = ''

        # match takes place of if/else statements
        match self.slider_Years.sliderPosition():
            case 0:
                year = '60s and earlier'
            case 1:
                year = '70s'
            case 2:
                year = '80s'
            case 3:
                year = '90s'
            case 4:
                year = '2000s'
            case 5:
                year = '2010s and beyond'

        match self.slider_Range.sliderPosition():
            case 0:
                ranges = 'Bass'
            case 1:
                ranges = 'Baritone'
            case 2:
                ranges = 'Tenor'
            case 3:
                ranges = 'Alto'
            case 4:
                ranges = 'Mezzo'
            case 5:
                ranges = 'Soprano'

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
            case 5:
                mood = 'All'

        match self.slider_Difficulty.sliderPosition():
            case 0:
                difficulty = 'Easy'
            case 1:
                difficulty = 'Medium'
            case 2:
                difficulty = 'Hard'

        match self.checkBox_Duet.isChecked():
            case True:
                duet = 'Duet'
            case _:
                duet = ''

        # makes sub-lists of indexes from gui selections
        time_period_indexes = [item for item in range(len(time_period_list)) if time_period_list[item] == year]
        range_indexes = [item for item in range(len(range_list)) if range_list[item] == ranges]
        difficulty_indexes = [item for item in range(len(difficulty_list)) if difficulty_list[item] == difficulty]
        mood_indexes = [item for item in range(len(mood_list)) if mood in mood_list[item]]
        duet_indexes = [item for item in range(len(duet_list)) if duet_list[item] == duet]
        if mood != 'All':
            sorted_list = set(time_period_indexes) & set(range_indexes) & set(difficulty_indexes) & set(
                mood_indexes) & set(duet_indexes)
            selection = random.choice(tuple(sorted_list))
        else:
            sorted_list = set(time_period_indexes) & set(range_indexes) & set(difficulty_indexes) & set(duet_indexes)
            selection = random.choice(tuple(sorted_list))

        if sorted_list == 0:
            self.label_Song.setText(f'Sorry! Try again!')
        else:
            self.label_Song.setText(f'"{title_list[selection]}"\n{artist_list[selection]}')
