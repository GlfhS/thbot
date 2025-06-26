import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from config import BOT_TOKEN, ADMIN_ID

# ===== Flask-сервер для Replit =====
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Бот жив 👋"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ====================================

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 О кафедре")],
        [KeyboardButton(text="🎓 Поступление")],
        [KeyboardButton(text="📘 Дисциплины по курсам")],
        [KeyboardButton(text="❓ Частые вопросы")],
        [KeyboardButton(text="📞 Контакты")],
    ],
    resize_keyboard=True
)

courses_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1️⃣ Первый курс"), KeyboardButton(text="2️⃣ Второй курс")],
        [KeyboardButton(text="3️⃣ Третий курс"), KeyboardButton(text="4️⃣ Четвёртый курс")],
        [KeyboardButton(text="⬅️ Назад")],
    ],
    resize_keyboard=True
)

# Команды и кнопки
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Привет! Я — бот кафедры. Вот что я умею:",
        reply_markup=main_menu
    )

@dp.message(lambda msg: msg.text == "📚 О кафедре")
async def about_department(message: types.Message):
    await message.answer(
        "📚 *Кафедра информационных систем и технологий*\n\n"
        "🛠 Профиль: *Информационные системы и технологии в строительстве*\n"
        "👨‍💻 Обучение включает разработку, внедрение и сопровождение ИТ-решений в строительстве\n"
        "📈 Выпускники работают в IT-компаниях, инжиниринге, органах власти и проектных организациях\n"
        "🎯 Виды деятельности: проектная, производственно-технологическая, научная\n\n"
        "📍 Адрес: г. Макеевка, ул. Державина, 2, ауд. 1.563\n"
        "📞 Тел.: +7 (949) 370-63-25\n"
        "📧 ist@donnasa.ru\n"
        "🔗 Подробнее: https://donnasa.ru/?page_id=100947&lang=ru"
    )

@dp.message(lambda msg: msg.text == "🎓 Поступление")
async def admission_info(message: types.Message):
    await message.answer(
        "🎓 *Как поступить:*\n"
        "• Документ о среднем образовании\n"
        "• Вступительные экзамены / ЕГЭ\n"
        "• Зачисление — на бюджет или контракт\n\n"
        "📌 С 2025 года ДонНАСА стал филиалом НИУ МГСУ\n"
        "🔬 Новые возможности: стажировки, исследования, усиленная поддержка\n"
        "📝 Сохраняются формы и условия обучения, все права студентов защищены\n\n"
        "📅 Приёмная комиссия:\n"
        "Пн–Пт: 09:00–15:00, Сб: 09:00–14:00\n"
        "📧 vstup@donnasa.ru\n"
        "🌐 Подробнее: https://donnasa.ru/?page_id=111446&lang=ru"
    )

@dp.message(lambda msg: msg.text == "📘 Дисциплины по курсам")
async def show_course_menu(message: types.Message):
    await message.answer("Выберите курс:", reply_markup=courses_menu)

@dp.message(lambda msg: msg.text == "1️⃣ Первый курс")
async def first_course(message: types.Message):
    await message.answer(
        "📘 *1 курс:*\n"
        "• История, математика, физика, английский\n"
        "• Инженерная и компьютерная графика\n"
        "• Программирование, информатика\n"
        "• Ознакомительная практика"
    )

@dp.message(lambda msg: msg.text == "2️⃣ Второй курс")
async def second_course(message: types.Message):
    await message.answer(
        "📘 *2 курс:*\n"
        "• Философия, право, экономика\n"
        "• ООП, большие данные, ИИ\n"
        "• Дифф. уравнения, статистика\n"
        "• Технологическая практика"
    )

@dp.message(lambda msg: msg.text == "3️⃣ Третий курс")
async def third_course(message: types.Message):
    await message.answer(
        "📘 *3 курс:*\n"
        "• Базы данных, ОС, BIM\n"
        "• Автоматизация проектирования\n"
        "• Архитектура, логистика, управление\n"
        "• Эксплуатационная практика"
    )

@dp.message(lambda msg: msg.text == "4️⃣ Четвёртый курс")
async def fourth_course(message: types.Message):
    await message.answer(
        "📘 *4 курс:*\n"
        "• Системное администрирование\n"
        "• Web, GIS, защита информации\n"
        "• АСУ, моделирование\n"
        "• Преддипломная практика, ВКР"
    )

@dp.message(lambda msg: msg.text == "⬅️ Назад")
async def back_to_main(message: types.Message):
    await message.answer("Вы вернулись в главное меню:", reply_markup=main_menu)

@dp.message(lambda msg: msg.text == "❓ Частые вопросы")
async def faq(message: types.Message):
    await message.answer(
        "❓ *Частые вопросы:*\n"
        "— Есть ли общежитие? ✅ Да\n"
        "— Какие экзамены? 📘 Русский, математика, информатика/английский\n"
        "— Военная кафедра? ❌ Пока нет\n"
        "— Контракт/бюджет? ✅ Есть оба варианта"
    )

@dp.message(lambda msg: msg.text == "📞 Контакты")
async def contacts(message: types.Message):
    await message.answer(
        "📍 *Адрес:*\n"
        "286123, г. Макеевка, ул. Державина, д. 2\n"
        "ФГБОУ ВО «ДонНАСА» — филиал НИУ МГСУ\n"
        "1-й учебный корпус, ауд. 1-563\n\n"
        "✉️ ist@donnasa.ru\n"
        "📞 +7 (949) 370-63-25\n"
        "🕐 Пн–Пт: 09:00–15:00"
    )

@dp.message()
async def fallback(message: types.Message):
    await message.answer("👋 Нажмите /start для начала или выберите пункт из меню.")

# === Запуск ===
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    keep_alive()
    asyncio.run(main())
