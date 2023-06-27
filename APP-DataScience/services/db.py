import sqlite3

DATABASE = 'proyecto.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS transacciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            x_pos TEXT,
            y_pos TEXT,
            month TEXT,
            day TEXT,
            hour TEXT,
            minute TEXT,
            monto REAL,
            nombre TEXT,
            fraudulenta INTEGER
        )
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS predicciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            x_pos TEXT,
            y_post TEXT,
            month TEXT,
            day TEXT,
            hour TEXT,
            minute TEXT
            fk_id_transaccion INTEGER
        )
    ''')

    conn.commit()
    conn.close()
    return True