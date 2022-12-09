import csv

class Song:
    def __init__(self, artist):
        #title, genre, time, year, mood, duet, difficulty):
        self.artist = artist
        # self.title = title
        # self.genre = genre
        # self.time = time
        # self.year = year
        # self.mood = mood
        # self.duet = duet
        # self.difficulty = difficulty

        artist_list = []
        # title_list = []
        # genre_list = []
        # time_period_list = []
        # year_list = []
        # mood_list = []
        # duet_group_list = []
        # difficulty_list = []
        # range_list = []
        with open('song_list.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                artist_list.append(line[0])
                # title_list.append(line[1])
                # genre_list.append(line[2])
                # time_period_list.append(line[3])
                # year_list.append(line[4])
                # mood_list.append(line[5])
                # duet_group_list.append(line[6])
                # difficulty_list.append(line[7])
                # range_list.append(line[8])

