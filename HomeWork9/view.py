from bot import bot

async def  start_game(message):
    await bot.send_message(message.from_user.id,f'Привет, {message.from_user.first_name}\n'
                        f'Правила игры:\n На столе лежит 150 конфет.\n'
                        f'Играют два игрока делая ход друг после друга.\n' 
                        f'Первый ход определяется жеребьевкой.\n '
                        f'За один ход можно забрать не более 28 конфет.\n '
                        f'Все конфеты достанутся игроку сделавшему последний ход.')

async def player_take(message):
    await bot.send_message(message.from_user.id,f'Возьмите конфеты, но не больше 28:')

async def table_info(message, name1, take, total_count, name2):
    await bot.send_message(message.from_user.id,f'{name1} взял {take} конфет,\n'
                                                f'на столе осталось {total_count} конфет.\n'
                                                f'Ход {name2}.')

async def win(message, name, take, total_count):
    await bot.send_message(message.from_user.id,f'{name} взял {take} конфет,\n'
                                                f'на столе осталось {total_count} конфет.\n'
                                                f'{name} победил.')

async def wrong_take(message):
    await bot.send_message(message.from_user.id,f'Вы взяли слишком много конфет, попробуйте снова!')

