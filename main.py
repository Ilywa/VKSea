from sys import path

path.insert(0, "modules")

from json import loads
from cfg import secret, phone_wl, main_keyboard, on_date_keyboard, datesOnMessage
from vkbottle.bot import Bot, Message
from vkbottle import GroupEventType, GroupTypes

messages_by_bot = {
	'greet': 'Привет, {}!\nВнизу чата можно нажимать на кнопки!\nНа выбор есть 4 комнаты:\nГалактика - трёхместная\nГрация - двухместная\nЗвёздное небо - двухместная\nОливковый рай - четырёхместная\nНажми на кнопку с названием, чтобы получить больше информации.',
	'info': 'Мы недорого сдаём комнаты, недалеко от моря.\nУ нас есть:\n- общая кухня,\n- летний душ и туалеты,\n- место для парковки машины,\n- большой двор,\n- мангал,\n- мощный Wi-Fi.\nКаждая комната оборудована холодильником и вентилятором.',
	'r1': 'Галактика - прекрасный выбор для небольшой семьи.\nВ комнате три кровати, тумба, холодильник и вентилятор...', #дописать
	'r2': 'Грация - великолепный выбор для двух человек.\nКомната оборудована двумя кроватями, тумбой, холодильником и вентилятором...', #дописать
	'r3': 'Звёздное небо - выгодный вариант для двух человек.\nКомната небольшая, но уютная и практичная, оборудована двумя кроватями, тумбой, холодильником и вентилятором...', #дописать
	'r4': 'Оливковый рай - отличный выбор для большой семьи.\nВ комнате две обычные кровати и одна двухэтажная, холодильник и вентилятор...', #дописать
	'radd': 'На кнопках появились даты.\nНажмите на кнопку с необходимым числом, чтобы забронировать комнату на этот день.\nКрасные числа означают то, что комната уже занята в этот день.',
	'q': 'У вас остались вопросы или хотите согласовать дату заезда?\nОтправьте сюда ваш номер телефона и удобное время для звонка, наш менеджер постарается связаться с вами как можно скорее.',
	'arriving': 'Отправьте сюда ваш номер телефона и удобное время для звонка, наш менеджер постарается связаться с вами как можно скорее.',
	'unv': 'К сожалению, в этот день комната занята, выберите другой.',
	'mback': 'Кнопки возвращены.',
}

bot = Bot(secret)
bot.labeler.vbml_ignore_case = True

@bot.on.private_message(text='Привет')
async def greet(message: Message):
	user = await bot.api.users.get(message.from_id)
	await message.answer(messages_by_bot['greet'].format(user[0].first_name), keyboard=main_keyboard)

@bot.on.private_message(payload={'func': 'mainInfo'})
async def info(message: Message):
	await message.answer(messages_by_bot['info'])

@bot.on.private_message(payload={'func': 'room1'})
async def room1(message: Message):
	dateKeyB = datesOnMessage('r1')
	await message.answer(messages_by_bot['r1'], keyboard=dateKeyB)
	await message.answer(messages_by_bot['radd'])

@bot.on.private_message(payload={'func': 'room2'})
async def room2(message: Message):
	dateKeyB = datesOnMessage('r2')
	await message.answer(messages_by_bot['r2'], keyboard=dateKeyB)
	await message.answer(messages_by_bot['radd'])

@bot.on.private_message(payload={'func': 'room3'})
async def room3(message: Message):
	dateKeyB = datesOnMessage('r3')
	await message.answer(messages_by_bot['r3'], keyboard=dateKeyB)
	await message.answer(messages_by_bot['radd'])

@bot.on.private_message(payload={'func': 'room4'})
async def room4(message: Message):
	dateKeyB = datesOnMessage('r4')
	await message.answer(messages_by_bot['r4'], keyboard=dateKeyB)
	await message.answer(messages_by_bot['radd'])

@bot.on.private_message(payload={'func': 'callme'})
async def callme(message: Message):
	await message.answer(messages_by_bot['q'])

@bot.on.private_message(payload={'date': 'unavailable'})
async def unavailableDate(message: Message):
	await message.answer(messages_by_bot['unv'], keyboard=main_keyboard)

@bot.on.private_message(payload={'func': 'back'})
async def back(message: Message):
	await message.answer(messages_by_bot['mback'], keyboard=main_keyboard)

@bot.on.private_message()
async def onMessage(message: Message):
	if message.payload is not None:
		day = loads(message.payload)
		day = day['date']
		await message.answer(messages_by_bot['arriving'], keyboard=main_keyboard)
		return
	for i in phone_wl:
		if message.text.find(i) >= 0:
			return
	await message.answer('Я тебя не понимаю :(\nВоспользуйся кнопками в чате.', keyboard=main_keyboard)

bot.run_forever()