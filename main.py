import discord
from discord.ext import commands
import sqlite3

# Создаем объект бота
bot = commands.Bot(command_prefix='!')
db_connection = sqlite3.connect('ecology_bot.db')
cursor = db_connection.cursor()

# Создаем таблицу для хранения баллов
cursor.execute('''CREATE TABLE IF NOT EXISTS scores (
                    user_id TEXT PRIMARY KEY,
                    points INTEGER DEFAULT 0
                )''')
db_connection.commit()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "ecology":
        user_id = str(message.author.id)

        # Получаем количество баллов пользователя
        cursor.execute("SELECT points FROM scores WHERE user_id=?", (user_id,))
        result = cursor.fetchone()

        if result is None:
            # Если пользователя нет в базе данных, добавляем его
            cursor.execute("INSERT INTO scores (user_id) VALUES (?)", (user_id,))
            db_connection.commit()
            points = 0
        else:
            points = result[0]

        # Выдаем баллы
        points += 1

        # Обновляем количество баллов в базе данных
        cursor.execute("UPDATE scores SET points=? WHERE user_id=?", (points, user_id))
        db_connection.commit()

        # Список заданий
        tasks = [
            "Задание 1: Изучите влияние человеческой деятельности на окружающую среду.",
            "Задание 2: Проведите исследование о важности переработки отходов.",
            "Задание 3: Расскажите о растениях и животных, находящихся под угрозой исчезновения."
        ]

        # Отправляем список заданий в чат
        task_list = "\n".join(tasks)
        await message.channel.send(f"Список заданий по экологии:\n{task_list}")

        # Отправляем количество баллов в чат
        await message.channel.send(f"{message.author.mention}, у вас {points} баллов!")

    await bot.process_commands(message)

# Запускаем бота
bot.run('ТВОЙ_ТОКЕН_БОТА')
