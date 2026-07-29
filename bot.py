import sqlite3

def init_db():
    conn = sqlite3.connect('valide_admin.db')
    cursor = conn.cursor()

    # Müştərilər cədvəli
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT UNIQUE NOT NULL
        )
    ''')

    # Rezervasiyalar cədvəli
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
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

if __name__ == '__main__':
    init_db()
    print("Məlumat bazası uğurla yaradıldı!")
if __name__ == "__main__":
    init_db()
    print("Məlumat bazası uğurla yaradıldı!")
    bot.infinity_polling()
