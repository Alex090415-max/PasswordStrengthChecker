import sqlite3

def setup_db(db_path='common_passwords.db'):
    common_passwords = ['password123', 'qwerty', '123456', 'password', '12345678', 'abc123', 'password1', 'admin', 'letmein', 'welcome']

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS passwords (password TEXT)")

    for password in common_passwords:
        cursor.execute("INSERT INTO passwords (password) VALUES (?)", (password,))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_db()
