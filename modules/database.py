# -*- coding: utf-8 -*-
import sqlite3

def OpenConnection(name):
	return sqlite3.connect(name, check_same_thread=False)

def CreateCursor(connection):
	return connection.cursor()

def CloseConnection(connection):
	connection.close()

def isRoomFree(room):
	connection = OpenConnection('rooms.db')
	cursor = CreateCursor(connection)

	cursor.execute(f"SELECT * FROM {room};")
	get_all_values = cursor.fetchall()
	data = []
	for i in range(len(get_all_values)):
		startdate = get_all_values[i][1]
		finaldate = get_all_values[i][2]
		data.append(room)
		for i in range(int(startdate), int(finaldate)+1):
			data.append(i)
	CloseConnection(connection)
	return data

	"""c = OpenConnection('rooms.db')
	cr = CreateCursor(c)
	c.execute("INSERT INTO dates(room, sdate, fdate) VALUES('1','25.07','27.07');")
	c.commit()"""