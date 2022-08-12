# -*- coding: utf-8 -*-
import datetime
from calendar import monthrange
from vkbottle import Keyboard, KeyboardButtonColor, Text, Callback, EMPTY_KEYBOARD
from database import isRoomFree

secret = 'vk1.a.tI4bogR0114_JxFen1jGpeAYhuTkH8dfhK0-ZS1QKcAsit550qo0lxD89V-FHtQDUSE_6D3pJWBmYeSihHJUtZT3WNNdG-K5SV2zCOTdt9MkJBpApZt1mRK5oyEvJTIQYFRZKlfcIIXPV67O251hzQn1VLjQXU2JWoySLxGjK-Wi4SG49PmDv2eDYSg3o_Wy'
phone_wl = ['949','071']


main_keyboard = (
	Keyboard()
	.add(Text('Общая информация 📜', {'func': 'mainInfo'}), color=KeyboardButtonColor.POSITIVE)
	.row()
	.add(Text('Галактика 🌌', {'func': 'room1'}), color=KeyboardButtonColor.PRIMARY)
	.add(Text('Грация 💃', {'func': 'room2'}), color=KeyboardButtonColor.PRIMARY)
	.row()
	.add(Text('Звёздное небо 🌃', {'func': 'room3'}), color=KeyboardButtonColor.PRIMARY)
	.add(Text('Оливковый рай 🌳', {'func': 'room4'}), color=KeyboardButtonColor.PRIMARY)
	.row()
	.add(Text('Согласовать звонок 🤙🏻', {'func': 'callme'}), color=KeyboardButtonColor.POSITIVE)
	)

on_date_keyboard = (
	Keyboard(one_time=True)
	.add(Text('Согласовать заезд 🚗', {'func': 'arriving'}))
	.row()
	.add(Text('Назад 👣', {'func': 'back'}))
	)

def monthDays():
	months_days=[]
	current_month = datetime.datetime.now().month - 1
	for i in range(1,13):
		months_days.append(monthrange(datetime.datetime.now().year, i))
	return list(range(1, months_days[current_month][1] + 1))

def datesOnMessage(room):
	keyboard = Keyboard(one_time=True)
	dates = isRoomFree(room) 
	days = monthDays()

	for i in range(len(days)):
		if days[i] in [6,11,16,21,26,31]: 
			keyboard.row()
		if days[i] in dates:
			keyboard.add(Text(f'{days[i]} ', {'date': 'unavailable'}), color=KeyboardButtonColor.NEGATIVE)
		else:
			keyboard.add(Text(days[i], {'date': (days[i])}), color=KeyboardButtonColor.POSITIVE)

	keyboard.row()
	keyboard.add(Text('Назад 👣', {'func': 'back'}), color=KeyboardButtonColor.PRIMARY)
	return keyboard