from PyQt5.QtWidgets import *
from view import *
from song import Song
import random

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_Random.clicked.connect(lambda: self.random())

    def random(self):
        # i = random.randint(0, 515)
        # output = Song(artist_list[i])
        print(f'Test')
    #self.label_Song.setText(output)
    # def output(self):
    #     print(
    #         f'"{title_list[i]}" by {artist_list[i]} ({year_list[i]})\nGenre:{genre_list[i]} Time Period:{time_period_list[i]}\n'
    #         f'Range:{range_list[i]} Mood:{mood_list[i]}\nDifficulty:{difficulty_list[i]} {duet_group_list[i]}')
