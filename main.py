import telebot
from telebot import types
import os
import time

BOT_TOKEN = os.environ.get('BOT_TOKEN', '7501309140:AAHKx7Pa5Oz52I6Fo_2YP3Moe9hfq6ukfO4')
bot = telebot.TeleBot(BOT_TOKEN)

def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("👥 Связь с оператором", callback_data="operator")
    btn2 = types.InlineKeyboardButton("💰 Кешбек за отзыв", callback_data="cashback")
    btn3 = types.InlineKeyboardButton("🛡️ Гарантия от производителя", callback_data="warranty")
    btn4 = types.InlineKeyboardButton("💃 Курс интимная гимнастика", callback_data="course")
    markup.add(btn1, btn2, btn3, btn4)
    return markup

def back_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_back = types.InlineKeyboardButton("⬅️ Назад", callback_data="back")
    markup.add(btn_back)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = """Что умеет бот?

Бренд Pushka Tuki-tuki приветствует Вас!
Здесь вы можете задать свой вопрос, получить кешбек за покупку, а так же ознакомиться с инструкциями и видео-курсами с использованием нашей продукции"""
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: call.data == "operator")
def contact_operator(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Для связи с оператором обратитесь к @pushka_tuki_tuki_manager", reply_markup=back_menu())

@bot.callback_query_handler(func=lambda call: call.data == "cashback")
def cashback_review(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Информация о кешбеке за отзыв", reply_markup=back_menu())

@bot.callback_query_handler(func=lambda call: call.data == "warranty")
def warranty(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Информация о гарантии от производителя", reply_markup=back_menu())

@bot.callback_query_handler(func=lambda call: call.data == "course")
def intimate_gymnastics(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Информация о курсе интимной гимнастики", reply_markup=back_menu())

@bot.callback_query_handler(func=lambda call: call.data == "back")
def back_to_menu(call):
    bot.answer_callback_query(call.id)
    welcome_text = """Что умеет бот?

Бренд Pushka Tuki-tuki приветствует Вас!
Здесь вы можете задать свой вопрос, получить кешбек за покупку, а так же ознакомиться с инструкциями и видео-курсами с использованием нашей продукции"""
    
    bot.send_message(call.message.chat.id, welcome_text, reply_markup=main_menu())

@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    welcome_text = """Что умеет бот?

Бренд Pushka Tuki-tuki приветствует Вас!
Здесь вы можете задать свой вопрос, получить кешбек за покупку, а так же ознакомиться с инструкциями и видео-курсами с использованием нашей продукции"""
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu())

if __name__ == "__main__":
    print("🚀 Бот Pushka Tuki-tuki запущен на Render!")
    while True:
        try:
            bot.polling(none_stop=True, timeout=60)
        except Exception as e:
            print(f"Ошибка: {e}")
            time.sleep(5)
