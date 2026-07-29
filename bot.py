import os
import telebot
import sqlite3

# Tokenin oxunması
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    print("XƏTA: BOT_TOKEN tapılmadı!")
    exit(1)

bot = telebot.TeleBot(TOKEN)

# Məlumat bazasının yaradılması
def init_db():
    conn = sqlite3.connect('valide_admin.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT UNIQUE NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_phone TEXT,
            date TEXT,
            time TEXT,
            guests INTEGER,
            note TEXT,
            FOREIGN KEY(customer_phone) REFERENCES customers(phone)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Məlumat bazası uğurla yaradıldı!")

# /start əmri
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salam! Valide Xanım Restoranının idarəetmə botu işlək vəziyyətdədir.")

if __name__ == "__main__":
    init_db()
    print("Bot işə düşdü və mesajları gözləyir...")
    bot.infinity_polling()
