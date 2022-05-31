from sql_conn import *
from test import *


db = DB()


def upload():
    for title in range(len(sulTitle)):
        Title = sulTitle[title]
        print(Title)
        db.insertTitle(Title)

        choruz = chorus[title]

        db.insertChorus(choruz)

        verse = verses[title]
        for verseno in range(len(verse)):
            temp = [sulTitle[title][0], verseno + 1, verse[verseno]]
            db.insertVerse(temp)
            print(temp)


def getSul(no):
    #title
    title = db.getTitle(no)[0]
    print(title)
    print(f"Sul Number {title[0]} {title[1]}")
    print(f"Category {title[2]}")
    if title[3] != "none":
        print(f"SubCategory {title[3]}")

    #chorus
    chorusrecv = db.getChorus(no)[0]


    #verse
    verse = db.getVerses(no)

    for v in range(len(verse)):
        print(f"Verse {verse[v][2]}")
        print(f"\t{verse[v][3]}")
        if chorusrecv[1] != "none":
            print("Chorus:")
            print(f"\t{chorusrecv[1]}")

def availableSul():
    availableTitle =db.getAllTitles()
    for availableTitles in availableTitle:
        print(f"Sul Number: {availableTitles[0]}")
        print(f"Sul Title: {availableTitles[1].title()}")
        print(f"Sul Category: {availableTitles[2]}")
        print(f"Sul SubCategory: {availableTitles[3]}")
        print("===============================================================================================================================")

#upload()
availableSul()
sulTarget = input("Enter Sul Number: ")
getSul(int(sulTarget))

