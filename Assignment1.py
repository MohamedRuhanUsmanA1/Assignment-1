import csv


# function to list songs
def song_list():
    with open('songs.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        for row in readCSV:
            if row[4] == 'N ':
                completed = "*"
                print("{} --{} {} -----> {} ----> {}".format(row[0], completed, row[1], row[2], row[3]))
            else:
                print("{} -- {} -----> {} ----> {}".format(row[0], row[1], row[2], row[3]))


# function showing the amount of songs loaded and the amount of songs learned
# load song opens csv file
# for loop to convert the list into string to print
# using .format to print file to achieve best format
def load_song():
    with open('songs.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        learned = [] # list to store learned and unlearned songs
        for row in readCSV:
            learn = row[4]
            learned.append(learn)
        print("{} songs learned {} songs still to learn".format(learned.count('N '), learned.count("Y")))
        print("Songs loaded", len(learned))


def add_song():
    song_name = input("Enter name of song: ")
    artist = input("Enter name of Artist: ")
    song_year = input("Year: ")
    with open('songs.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        learned = []      # new list to save data
        for row in readCSV:
            learn = row[4]
            learned.append(learn)

    num_song = (len(learned))    # adding new data to file
    with open("songs.csv", "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([num_song, song_name, artist, song_year, "N"])

# read file
# add file into a list to store into memory
# for loop to append new file
# int as input to avoid errors
#

def complete_song():
    file = open("songs.csv", "r")

    new_file = []
    song_num = int(input("Enter the song to be learned: "))

    for line in file:
        data = line.split(",")
        if data[4] == "N ":
            print("song already learned")
        elif data[0] == song_num:
            newLine = "%s,%s,%s,%s,%s \n" % (data[0], data[1], data[2], data[3], 'N')  # adding N to learned song
            new_file.append(newLine)

        else:
            new_file.append(line)

    file.close()  # close read file

    file = open("songs.csv", "w") # open as write file in order to change the data

    for line in new_file:
        file.write(line)

    file.close()

# main function showing menu and calling functions
def main():
    print("Songs to learn 1.0 by Mohamed Ruhan Usman ")
    while True:        # while True for error checking
        try:

            print("Please select an option \n 1 - List songs \n 2 - Add song \n 3 - Complete song \n 4 - Quit")
            choice = int(input(">>> "))

            if choice == 1:
                song_list()
                load_song()
            elif choice == 2:
                add_song()
            elif choice == 3:
                complete_song()
            elif choice == 4:
                print("Have a nice day")
                break          # break to stop loop when user quits
            else:
                print("You have entered a Wrong command")
        except ValueError:      # value error so string inputs will not be taken
            print("Please enter a  valid number")


main()
