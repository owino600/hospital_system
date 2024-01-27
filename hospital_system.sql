import sqlite3

# Establish a connection to the SQLite database
conn = sqlite3.connect('hospital_system.db')
cursor = conn.cursor()

# Creating tables for patient details, appointments, queue, and doctor's prescription
cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY,
        name TEXT,
        dob TEXT,
        contact TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY,
        patient_id INTEGER,
        doctor TEXT,
        date TEXT,
        FOREIGN KEY (patient_id) REFERENCES patients(id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS queue (
        id INTEGER PRIMARY KEY,
        patient_id INTEGER,
        position INTEGER,
        FOREIGN KEY (patient_id) REFERENCES patients(id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS prescriptions (
        id INTEGER PRIMARY KEY,
        patient_id INTEGER,
        doctor TEXT,
        medication TEXT,
        instructions TEXT,
        FOREIGN KEY (patient_id) REFERENCES patients(id)
    )
''')

# Committing changes and closing the connection
conn.commit()
conn.close()

