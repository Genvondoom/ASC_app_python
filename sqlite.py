import sqlite3
conn = sqlite3.connect('/home/vdprime/Videos/wj/backup/Softouch/Easyworship/Default/v6.1/Databases/Data/SongWords.db')
cursorObj = conn.cursor()
cursorObj.execute("SELECT name from sqlite_master")
print(cursorObj.fetchall())
cursorObj.execute("SELECT * from word")
test = cursorObj.fetchall()
print(test[0])

print(len("Praise God from whom all blessings flow; Praise Him all creatures here below; O praise Him! Alleluia! Praise Him above ye heavenly hosts, Praise Father, Son, and Holy Ghost. O praise Him, O praise Him! Alleluia! Alleluia! Alleluia!"))