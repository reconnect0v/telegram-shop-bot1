from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import sqlite3

API_TOKEN = 'твой_токен_бота'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать в магазин! Выберите команду:\n/catalog — Посмотреть товары\n/cart — Корзина")

@dp.message_handler(commands=['catalog'])
async def catalog_command(message: types.Message):
    # Подключение к базе и вывод товаров
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, price FROM products")
    products = cursor.fetchall()
    catalog = "\n".join([f"{name} - {price} руб." for name, price in products])
    conn.close()
    await message.answer(f"Каталог товаров:\n\n{catalog}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
